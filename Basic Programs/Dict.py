#dct = dict()
#dct["Atharv"] = 123
#dct["Ameya"] = 923
#
#print(dct)
#print(type(dct))
#
#x =123
#print(type(x))
#
#rawdata = list()
#rawdata = ['Atharv',"Ameya","Uma","Shraddha","Mangesh","Rama","Ameya","Uma","Atharv","Ameya"]
#print(type(rawdata))
#print(rawdata)
#
#namedict = dict()
#for name in rawdata :
#    if name not in namedict :
#        namedict[name] = 1
#    else :
#        namedict[name] = namedict[name] + 1
#
#print(namedict)


rawdata = list()
rawdata = ['Atharv',"Ameya","Uma","Shraddha","Mangesh","Rama","Ameya","Uma","Atharv","Ameya"]
print(type(rawdata))
print(rawdata)

namedict = dict()
for name in rawdata :
    namedict[name] = namedict.get(name,0) + 1

print(namedict)