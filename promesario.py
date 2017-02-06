__author__ = 'Pyboy'
import tkinter as t
import webbrowser
import manager

# Definitions of classes
class App:
    def __init__(self,master):
        # Adding menu bar here
        menu=t.Menu(master)
        actions_menu=t.Menu(menu,tearoff=0)
        actions_menu.add_command(label="Agregar promesa nueva",command=self.add_element)
        menu.add_cascade(label="Acciones",menu=actions_menu)
        about_menu=t.Menu(menu,tearoff=0)
        about_menu.add_command(label="Acerca de Promesario",command=self.about)
        about_menu.add_command(label="Visitar sitio",command=self.visit_site)
        menu.add_cascade(label="Acerca",menu=about_menu)
        master.configure(menu=menu)
        # Label to show text
        self.texto=t.Label(master,bg="#ffffff",bd=3,relief=t.SUNKEN,height=10,width=38)
        self.texto.pack(padx=5,pady=5)
        # Button
        select_but=t.Button(master,text="Seleccionar",command=self.select_element,height=1,width=8)
        select_but.pack(side=t.BOTTOM,padx=5,pady=5)


        #Commands
    def add_element(self):
        """Defines the add element action"""
        add_win=t.Toplevel()
        top_label=t.Label(add_win,text="Texto")
        top_label.pack()
        text_entry=t.Entry(add_win)
        text_entry.pack(padx=5,pady=5)
        bot_label=t.Label(add_win)
        bot_label.configure(text="Cita")
        bot_label.pack()    
        foot_entry=t.Entry(add_win)
        foot_entry.pack(padx=5,pady=5)
        def add():
            text=text_entry.get()
            foot=foot_entry.get()
            manager.add_new(text,foot)
            text_entry.delete(0,len(text)+1)
            foot_entry.delete(0,len(foot)+1)
        add_button=t.Button(add_win,text="Agregar",command=add)
        add_button.pack(side=t.BOTTOM,padx=5,pady=5)

        
    def about(self):
        t.messagebox.showinfo(title="Acerca",message="Sencillo promesario para usar en familia")
        
    def visit_site(self):
        webbrowser.open("https://github.com/pywill/promesario")
        
    def select_element(self):
        selection=manager.get_element()
        print(selection)
        self.texto.configure(text=selection[0]+'\n'+selection[1])


root=t.Tk()
root.title(string="Promesario")
app=App(root)
root.mainloop()

