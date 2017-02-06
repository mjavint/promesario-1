__author__ = 'Pyboy'
import sqlite3

# File code
prom=open("promesas.txt","r")
prom_cont=prom.readlines()
# Database code
# Table for promesas
db=sqlite3.connect("data.db")
cur=db.cursor()
cur.execute("""CREATE TABLE promesas (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
texto TEXT UNIQUE NOT NULL,
cita TEXT UNIQUE NOT NULL)""")
db.commit()
# Data insertion procedure
for line in prom_cont:
    cita=line.split(" ")[0]
    texto=line.split(" ")[1].strip('\n')
    cur.execute("""INSERT INTO promesas
    (texto,cita) VALUES (?,?)""", (texto,cita))
# Database closing
db.commit()
cur.close()
db.close()

