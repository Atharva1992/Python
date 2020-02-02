import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
print(type(soup))

countinp = input("Count : ")
count = int(countinp) - 1
tags = soup('a')
for tag in tags :
    if count > 0 :
        print(tag.get('href', None))
        count = count - 1
    else :
        str = tag.get('href', None)
        y = re.findall('known_by_(.+).html',str)
        urlnew = "New : http://py4e-data.dr-chuck.net/known_by_"+y[0]+".html"
        print (urlnew)
        break
