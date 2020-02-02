fname = input("Enter the name of the file : ")
#fname = "mbox-short.txt"
try :
    fhand = open(fname)
except :
    print ("Wrong Filename ")
    quit()

dictmails = dict()
lst = list()
for line in fhand :
    if len(line) > 3 and line.startswith("From ") :
        row = line.split()
        lst.append(row[1])

for word in lst :
    dictmails[word] = dictmails.get(word,0) + 1

BigKey = None
BigVal = None
for ke,va in dictmails.items() :
    if BigVal is None or va > BigVal :
        BigKey = ke
        BigVal = va


print(BigKey,BigVal)
