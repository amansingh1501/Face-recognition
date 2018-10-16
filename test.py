from Tkinter import *
from tkMessageBox import *
import ttk
import os

def teste():
	import teste

def testL():
	import testl

def home():
	root2.destroy
	import gui

def leave():
    if askokcancel('EXIT','Do you want to exit ?'):
        root2.destroy()
def home3():

    Label(root2,text='Facial Recognition System',font='Arial 25 bold',justify='center',bg='light blue').place(relx=0.25,rely=0.0)
    Label(root2,image=a).place(relx=0.1,rely=0.07)
    Button(root2,text='  Eigen Test  ',font='Arial 15 bold',bg='light blue',fg='black',command=teste).place(relx=.25,rely=.83)
    Button(root2,text='LBPH Test',font='Arial 15 bold',bg='light blue',fg='black',command=testL).place(relx=.45,rely=.86)
    Button(root2,text='  Home ',font='Arial 15 bold',command=home,bg='light blue',fg='black').place(relx=.62,rely=.89)
    Button(root2,text='  Quit ',font='Arial 15 bold',command=leave,bg='light blue',fg='black').place(relx=.76,rely=.92)

    
root2=Tk()
a=PhotoImage(file='face.gif')
root2.geometry('800x600')
home3()
root2.mainloop()

