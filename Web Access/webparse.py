import urllib.request, urllib.parse, urllib.error

from bs4 import BeautifulSoup

url = input("Enter URL :")
#https://en.wikipedia.org/wiki/United_Kingdom
html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, 'html.parser')

print(soup)
#tags = soup('a')
#for tag in tags :
#    print(tag.get('href ', None))
