import urllib.request, urllib.parse, urllib.error
import json

address = input("Enter the Address : ")

urlinit = "https://maps.googleapis.com/maps/api/geocode/json?"
key = "Enter the API key here"
parm = dict()
parm['address'] = address
parm['key'] = "Enter the API key here"


url = urlinit + urllib.parse.urlencode(parm)
jsondata = urllib.request.urlopen(url)

data = jsondata.read().decode()

#print(data)

try :
    js = json.loads(data)
except :
    js = None

if not js or 'status' not in js or js['status'] != 'OK' :
    print("Failure to retrieve data")

lat = js["results"][0]["geometry"]["bounds"]["northeast"]["lat"]
lng = js["results"][0]["geometry"]["bounds"]["northeast"]["lng"]

print(lat,lng)
