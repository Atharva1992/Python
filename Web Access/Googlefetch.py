import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('https://www.google.co.in/')
for line in fhand :
    print (line)
