# importing the requests library
import requests
  
# send request to url with params
URL = ""
params="arg=value"
r = requests.get(url = URL, params = params)

# get details about request
#r = requests.Request('GET', url = URL, params = params)
#print(r.prepare().url)

# extracting data in json format
print(r.text)


  

