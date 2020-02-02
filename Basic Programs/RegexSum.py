import re
fname = input("Enter file name: ")
if len(fname) < 1 : fname = "regex2.txt"
fhand = open(fname)
sumlist = list()
for line in fhand :
    y = re.findall('[0-9]+',line)
    if len(y) > 0 :
        sumlist.append(y)

#Changing list of list to a list of numbers
numbers1 = list()
for i in sumlist :
    for j in i :
        numbers1.append(j)

sumation1 = 0
for int1 in numbers1 :
    sumation1 = sumation1 + int(int1)

print(sumation1)