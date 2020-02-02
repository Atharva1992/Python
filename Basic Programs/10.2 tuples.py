#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
#You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.



name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
fhand = open(name)
dicthrs = dict()
lst = list()
hour = list()
for line in fhand :
    if len(line) > 3 and line.startswith("From ") :
        row = line.split()
        lst.append(row[5])
for date in lst :
    row = date.split(':')
    hour.append(row[0])
for hrs in hour :
    dicthrs[hrs] = dicthrs.get(hrs,0) + 1 
newtup = tuple()
lst = list()
for key,val in dicthrs.items() :
    newtup = (key,val)
    lst.append(newtup)
#print(lst)
lst = sorted(lst,reverse=False)
#print(lst)
for key,val in lst :
    print (key,val)
    
