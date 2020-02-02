fname = input("Enter the name of the File : ")

try :
    fhand = open(fname)
except :
    print ("File not found")

countdist = dict()

for line in fhand :
    words = line.split()
    for word in words :
        countdist[word] = countdist.get(word,0) + 1


print(countdist)

bigv = None
bigk = None

for k,v in countdist.items() :
    if bigv is None or v > bigv :
        bigk = k
        bigv = v

print(bigk,bigv)