import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter location: ")
#url = "http://py4e-data.dr-chuck.net/comments_42.json"
#url = http://py4e-data.dr-chuck.net/comments_169730.json
jsondata = urllib.request.urlopen(url)
print("Retrieving "+url)
data = jsondata.read().decode()
js = json.loads(data)
#print(json.dumps(js, indent=2))
sum = 0
for item in js["comments"] :
    sum = sum + int(item["count"])
print(sum)
