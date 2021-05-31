# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 15:42:35 2020

@author: satya
"""

import sqlite3
conn=sqlite3.connect('emaildb.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS COUNTS')

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
sum=0
fname='mbox.txt'
fh=open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces=line.split()
    email=pieces[1]
    orgs=email.split('@')
    org=orgs[1]
    cur.execute('SELECT count FROM Counts WHERE org=? ',(org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(org,))
    else:
        cur.execute('UPDATE COUNTS SET count = count +1 WHERE org = ?', (org,))
    
conn.commit()

sqlstr='SELECT org, count FROM Counts'

for row in cur.execute(sqlstr):
    print(str(row[0]),row[1])
    sum=sum+row[1]
    
cur.close()
print(sum)