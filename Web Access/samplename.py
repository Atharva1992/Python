import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input ("Enter the URL :")
url = "http://py4e-data.dr-chuck.net/known_by_Krish.html"
inputturn = input("Turn : ")
#Adding one as the first one doesn't count. 4 times after Krish
turn = int(inputturn) + 1
#subtracting one as the counting is from 0 to count
inputcount = input("Count : ")
counter = int(inputcount) - 1

while turn > 0 :
    name = re.findall('known_by_(.+).html',url)
    print (name)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    count = counter
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
