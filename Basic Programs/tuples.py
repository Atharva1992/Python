#lst = ["Atharv","Ameya","Mangesh"]
#tpl = ("Atharv","Ameya","Mangesh")
#
#print(type(lst))
#print(type(tpl))    


fhand = open("romeo.txt")
dct1 = dict()
for line in fhand : 
    words1 = line.split()
    for wrd1 in words1 :
        dct1[wrd1] = dct1.get(wrd1,0) + 1


#print(dct1)

lst = list()

for key,val in dct1.items() :
    newtup = (val,key)
    lst.append(newtup)
    
lst = sorted(lst, reverse=True)
print(lst)


for val,key in lst[:10] :
    print(key,val)