__author__ = 'Pyboy'
# Module for interact with GUI
# This module must be able to interact with the database and retrieve its content to GUI
import sqlite3 as s
import random

def rand_number(table):
    # This function is for pick a random number for select a random element in tables
    rows=15 # This number must be changed to the amount of rows in selected table
    r_numb=random.randint(0,rows)
    return r_numb

def get_element(element):
    # This function defines a general form for treat all kinds of text.
    index=rand_number(element)
    db=s.connect("data.db")
    cur=db.cursor()
    if element=="promesas":
        cur.execute("""SELECT cita,texto FROM promesas WHERE id=?""",(index,))
        cita,texto=cur.fetchone()
        return cita,texto
    elif element=="frases":
        cur.execute("""SELECT autor,texto FROM promesas WHERE id=?""",(index,))
        autor,texto=cur.fetchone()
        return autor,texto





