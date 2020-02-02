import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_42.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
numbers = list()

tags = soup('span')
for tag in tags:
    str = re.findall('[0-9]+',tag.decode())
    if len(str) > 0 :
        numbers.append(str)

#To convert list of list to list of numbers
counter = list()
for i in numbers :
    for j in i :
        counter.append(j)
# Sum of all the numbers in list counter
sum = 0
for number in counter :
    sum = sum + int(number)
print (sum)
