# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 18:26:55 2020

@author: satya
"""
import json
import sqlite3

conn=sqlite3.connect('rosterdb.sqlite')
cur=conn.cursor()

cur.executescript('''DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname="roster_data.json"

data=open(fname).read()
json_data=json.loads(data)

for entry in json_data:
    name=entry[0]
    title=entry[1]
    role=entry[2]
    
    print("Name: "+name+"  Couse: "+title+"  Role: "+str(role) )
    
    cur.execute("INSERT OR IGNORE INTO User(name) VALUES(?)",(name,))
    cur.execute("SELECT id FROM User WHERE name=?",(name,))
    user_id=cur.fetchone()[0]
    
    cur.execute("INSERT OR IGNORE INTO Course(title) VALUES(?)",(title,))
    cur.execute("SELECT id FROM Course WHERE title=?",(title,))
    course_id=cur.fetchone()[0]
    
    cur.execute("INSERT OR IGNORE INTO Member(user_id,course_id,role) VALUES(?,?,?)",(user_id,course_id,role))
    
    conn.commit()
    
cur.execute('''SELECT hex(User.name || Course.title || Member.role ) AS X FROM 
    User JOIN Member JOIN Course 
    ON User.id = Member.user_id AND Member.course_id = Course.id
    ORDER BY X''')
print(str(cur.fetchone()[0]))
cur.close()
