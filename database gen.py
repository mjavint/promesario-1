__author__ = 'Pyboy'
import sqlite3

# File code
prom=open("promesas.txt","r")
fras=open("frases.txt","r")
prom_cont=prom.readlines()
fras_cont=fras.readlines()

# Database code
# Table for promesas
db=sqlite3.connect("data.db")
cur=db.cursor()
cur.execute("""CREATE TABLE promesas (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
cita TEXT UNIQUE NOT NULL,
texto TEXT UNIQUE NOT NULL,
fav BOOL NOT NULL)""")
# Table for frases
cur.execute("""CREATE TABLE frases (
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
texto TEXT UNIQUE NOT NULL,
autor TEXT NOT NULL)""")
db.commit()
# Data insertion procedure
for line in prom_cont:
    cita=line.split(" ")[0]
    texto=line.split(" ")[1].strip('\n')
    cur.execute("""INSERT INTO promesas
    (cita,texto) VALUES (?,?)""", (cita,texto))
for line in fras_cont:
    texto=line.split(" ")[0]
    autor=line.split(" ")[1].strip("\n")
    cur.execute("""INSERT INTO frases
    (texto,autor) VALUES (?,?)""",(texto,autor))
# Database closing
db.commit()
cur.close()
db.close()

