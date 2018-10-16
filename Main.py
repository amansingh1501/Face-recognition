from Tkinter import *
from tkMessageBox import *
import ttk


def start():
	root6.destroy()
	import gui

def home5():
    Label(root6,text='Version: 0.1.0',font='Arial 9',padx=90).place(relx=.75,rely=.95)
    Label(root6,text=' Welcome to Facial Recognition System',font='Arial 25 bold',justify='center',bg='light blue').place(relx=0.11,rely=0.0)
    Label(root6,image=a).place(relx=0.1,rely=0.07)
    Button(root6,text=' Start   ',font='Arial 15 bold',command=start,bg='light blue',fg='black').place(relx=.45,rely=.93)   



root6=Tk()
a=PhotoImage(file='face.gif')
root6.geometry('800x600')
home5()
root6.mainloop()


