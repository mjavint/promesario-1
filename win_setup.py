__author__ = 'Pyboy'
from cx_Freeze import setup, Executable

setup(
 name="Promesario",
 version="1.0",
 description="Un sencillo promesario para usar en familia",
 py_modules=['manager','database gen'],
 executables = [Executable("promesario.py",icon='prom.ico',base='Win32GUI')],
 )
