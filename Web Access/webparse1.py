import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input("Enter URL :")
#url = "http://www.dr-chuck.com/page1.htm"
#https://en.wikipedia.org/wiki/United_Kingdom
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#print(soup)
tags = soup('a')
for tag in tags :
    print(tag.get('href', None))
# Important note : I was not getting output because I had used print(tag.get('href ', None))
# The issue was that there was a space after href. Be careful
