import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
jsondata = urllib.request.urlopen(url)
print("Retrieving "+url)
data = jsondata.read().decode()
js = json.loads(data)
print(json.dumps(js, indent=2))
sum = 0
for item in js["comments"] :
    sum = sum + int(item["count"])
print(sum)
