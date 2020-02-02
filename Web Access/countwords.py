import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
counter = dict()
for line in fhand :
    words = line.decode().split()
    for word in words :
        counter[word] = counter.get(word, 0) + 1
print(counter)
