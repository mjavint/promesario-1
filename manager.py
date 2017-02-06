__author__ = 'Pyboy'
# Module for interact with GUI
# This module must be able to interact with the database and retrieve its content to GUI
import sqlite3 as s
import random
from tkinter import messagebox

def rand_number(table):
    """This function is for pick a random number for select a random element in tables"""
    db=s.connect("data.db")
    cur=db.cursor()
    cur.execute("SELECT count(id) FROM promesas")
    rows=cur.fetchone()[0]-1 # This number must be changed to the amount of rows in selected table
    r_numb=random.randint(1,rows)
    return r_numb

def get_element():
    """Function to select an element from a table"""
    index=rand_number("promesas")
    db=s.connect("data.db")
    cur=db.cursor()
    cur.execute("""SELECT texto,cita FROM promesas WHERE id=?""",(index,))
    selection=cur.fetchone()
    db.close()
    return selection

def add_new(text,foot):
    """Function for add new elements to existing tables"""
    db=s.connect("data.db")
    cur=db.cursor()
    if text=="" or foot=="" or text==" " or foot==" ":
        messagebox.showinfo(title="Info",message="No pueden haber campos vacios")
    #Once conected to database,insert new values to tables
    try:
        cur.execute("""INSERT INTO promesas (texto,cita) VALUES (?,?)""",(text,foot))
    except s.IntegrityError:
        messagebox.showinfo(title="Informacion",message="Ya existe ese texto guardado")
    finally:
        db.commit()
        cur.close()
        db.close()




