# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
numbers = list()
# Retrieve all of the anchor tags
tags = soup('td')
for tag in tags:
    y = re.findall('[0-9]+',tag.decode())
    if len(y) > 0 :
        numbers.append(y)
print (numbers)
sum = 0

#for number in numbers :
#    if number > 0 :
#        sum = sum + int(number)

print (dir(numbers))
print (sum)
