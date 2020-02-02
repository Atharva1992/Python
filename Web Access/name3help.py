import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Krish.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
soup = BeautifulSoup(html, 'html.parser')
tags = soup('a')
print("1",url)
count = 1
for tag in tags :
    count = count + 1
    print(count,tag.get('href', None))
