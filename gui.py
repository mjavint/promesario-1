__author__ = 'Pyboy'
import tkinter as t
import sys

# Definitions of classes
class App:
    def __init__(self,master):
        frame=t.Frame(master)
        frame.pack(side=t.RIGHT)
        # Adding a menu here
        menu=t.Menu(frame)
        menu.pack()
        # Button
        select=t.Button(master,text="Select",command=sys.exit)
        select.pack()
        # Label to show text
        texto=t.Label(master,bg="#BLACK",text="something here")
        texto.pack()


