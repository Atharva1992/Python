import sqlite3
import re

conn = sqlite3.connect('assigndb.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file:')
if len(fname) < 1 : fname = 'mbox.txt'
fhand = open(fname)
for line in fhand :
    if not line.startswith('From:') : continue
    pieces = line.split()
    email = pieces[1]
    organ = re.findall ('@(.+)',email)
    org1 = organ[0]
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org1,))
    row = cur.fetchone()
    if row is None :
        cur.execute('INSERT INTO Counts (org,count) VALUES(?,1)', (org1,))
    else :
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org1,))
    conn.commit()

output = cur.execute('SELECT org,count FROM Counts ORDER BY count DESC LIMIT 10')
for line in output:
    print("Email :",line[0],"\tCount :", line[1])
