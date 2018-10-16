from Tkinter import *
from tkMessageBox import *
import ttk
import os
def h1():
        def home2():
                root1.destroy()
                import gui
                gui.h()

        def Eigen():
                import eigen
        
        def LBPH():
        	import LBPH
        
        
        def leave():
                if askokcancel('EXIT','Do you want to exit ?'):
        		root1.destroy()

        def home1():
            Label(root1,text='Version 0.1.0 Copyrights(free to copy) 2018',font='Arial 9',padx=90).place(relx=.55,rely=.95)
            Label(root1,text='Facial Recognition System',font='Arial 25 bold',justify='center',bg='light blue').place(relx=0.25,rely=0.0)
            Label(root1,image=b).place(relx=0.1,rely=0.07)
            Button(root1,text='  Eigen Face  ',font='Arial 15 bold',bg='light blue',fg='black',command= Eigen ).place(relx=.15,rely=.93)
            Button(root1,text='LBPH Face',font='Arial 15 bold',bg='light blue',fg='black',command= LBPH ).place(relx=.38,rely=.93)
            Button(root1,text='  Home ',font='Arial 15 bold',bg='light blue',fg='black',command= home2 ).place(relx=.58,rely=.93)

            Button(root1,text='  Quit   ',font='Arial 15 bold',bg='light blue',fg='black',command= leave ).place(relx=.74,rely=.93)

        root1=Tk()
        b=PhotoImage(file='face.gif')
        root1.geometry('800x600')
        home1()
        root1.mainloop()
h1()
