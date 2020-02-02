fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

try :
    fh = open(fname)
except :
    print("File Doesn't Exist")
    quit()
    
#checklst = list()
#final = list()
#count = 0
#
#for line in fh :
#    if line.startswith("From ") :
#        count = count + 1
#        checklst = line.split()
#        final.append(checklst[1])
#
#print(final)
#print("There were", count, "lines in the file with From as the first word")
#
checklst = list()
count = 0

for line in fh :
    if line.startswith("From ") :
        count = count + 1
        checklst = line.split()
        print(checklst[1])

print("There were", count, "lines in the file with From as the first word")