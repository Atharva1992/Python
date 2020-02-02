import re
#x = "From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008"
#z = "X-DSPAM-Confidence: 0.8475"
#y = re.findall('^From .*@(\S+)',x)
# o/p = ['media.berkeley.edu']
#y = re.findall('^From .*@([^ ]*)',x)
# o/p = ['media.berkeley.edu']
#y = re.findall('^X-DSPAM-Confidence: (\S*)',z)
#o/p = ['0.8475']
#y = re.findall('^X-DSPAM-Confidence: [0-9.]*',z)
#o/p = ['X-DSPAM-Confidence: 0.8475']


#y = re.findall('^X-DSPAM-Confidence: ([0-9.]*)',z)
#o/p = ['0.8475']

#y = re.findall('^X-DSPAM-Confidence: .\S([0-9]*)',z)
#o/p = ['8475']

#y = re.findall('^From .*:(\S+:\S)',x)
#o/p = ['10:4']

#y = re.findall('^From .*:(\S+):\S',x)
#o/p = ['10']
#print(y)

#x = 'From: Using the : character'
#y = re.findall('^F.+:', x)
#print(y)

x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('\S+?@\S+', x)
print(y)
