import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_169729.xml"
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

sum = 0
tree = ET.fromstring(data)
results = tree.findall('comments/comment')

for item in results :
    count = item.find("count").text
    sum = sum + int(count)

print(sum)
