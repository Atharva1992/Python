import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Krish.html"
#Turn is the number of times the links should be called.
inp1 = input("Turn : ")
turn = int(inp1)
inp2 = input("Count : ")
count = int(inp2)
while turn > 0 :
    name = re.findall('known_by_(.+).html',url)
    print (name)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    #The number of line that needs to be called is 18th
    #Count is 16 as the first link is the one called itself. And next is 0-16. So total 18
    count = 17
    for tag in tags :
        if count > 0 :
            count = count - 1
        else :
            str = tag.get('href', None)
            y = re.findall('known_by_(.+).html',str)
            urlnew = "http://py4e-data.dr-chuck.net/known_by_"+y[0]+".html"
            url = urlnew
            break
    turn = turn - 1
    continue

#Krish
#Dermot - Katrianne
#Caedyn - Milena
#Zaina - Muryam
#Dregan -Caelainn
#Bryan - Muran
#Alyth - Maggi
