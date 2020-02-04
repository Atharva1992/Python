import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True :
    address = input("Enter the Address : ")
    print(address)
    if len(address) < 1 :
        break
    parm = dict()
    parm['address'] = address
    parm['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parm)
    jsondata = urllib.request.urlopen(url)
    data = jsondata.read().decode()
    js = json.loads(data)
    place = js["results"][0]["place_id"]
    print("Place ID is :",place)
