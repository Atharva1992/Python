fname = input("Enter file name: ")
try :
    fh = open(fname)
except :
    print("File Doesn't Exist")
    quit()
    

lst = list()
print(type(lst))
checklst = list()
print(type(checklst))
for line in fh:
    checklst = line.split()
#    print(checklst)
    for word in checklst :
#        print(word)
        if word not in lst : lst.append(word)
#print(lst)
#print(len(lst))
lst.sort()
print(lst)
