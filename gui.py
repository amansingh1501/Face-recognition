from Tkinter import *
from tkMessageBox import *
import ttk
def h():
        
        def face():
        	import Add
        	root.destroy()
	
        def rec():
                root.destroy()
                import Rec
                Rec.h1()
	

        def test():
                root.destroy()
                import test		
	
        def home():
            for widget in root.winfo_children():
                widget.destroy()
            Label(root,text='Facial Recognition System',font='Arial 25 bold',justify='center',bg='light blue').place(relx=0.25,rely=0.0)
            Label(root,image=a).place(relx=0.1,rely=0.07)
            Button(root,text='  Add Faces  ',font='Arial 15 bold',bg='light blue',fg='black',command=face).place(relx=.05,rely=.93)
            Button(root,text='Recognise',font='Arial 15 bold',bg='light blue',fg='black',command=rec).place(relx=.28,rely=.93)
            Button(root,text='  About ',font='Arial 15 bold',command=about,bg='light blue',fg='black').place(relx=.46,rely=.93)
            Button(root,text='  Test Graphs ',font='Arial 15 bold',command=test,bg='light blue',fg='black').place(relx=.40,rely=.84)
            Button(root,text=' Contact ',font='Arial 15 bold',command=contact,bg='light blue',fg='black').place(relx=.63,rely=.93)
            Button(root,text='  Quit   ',font='Arial 15 bold',command=leave,bg='light blue',fg='black').place(relx=.82,rely=.93)
            #Label(root,text='Version 0.1.0 Copyrights(free to copy) 2018',font='Arial 9',padx=90).place(relx=.55,rely=.15)
        def leave():
            if askokcancel('EXIT','Do you want to exit ?'):
                root.destroy()
        def about():
            for widget in root.winfo_children():
                widget.destroy()
            Label(root,text='Facial Recognition System',font='Arial 25 bold',justify='center',bg='light blue').place(relx=0.25,rely=0.0)
            Label(root,text='A facial recognition system is a computer application capable of identifying or ',font='Arial 12 bold',padx=90).place(relx=.01,rely=.08)
            Label(root,text='verifying a person from a digital image or a video frame from a video source. ',font='Arial 12 bold',padx=90).place(relx=.01,rely=.12)
            Label(root,text='One of the ways to do this is by comparing selected facial features from the ',font='Arial 12 bold',padx=90).place(relx=.01,rely=.16)
            Label(root,text='image and a face database. It is typically used in security systems and can be ',font='Arial 12 bold',padx=90).place(relx=.01,rely=.20)
            Label(root,text='compared to other biometrics such as fingerprint or eye iris recognition systems.',font='Arial 12 bold',padx=90).place(relx=.01,rely=.24)
            Label(root,text='Recently, it has also become popular as a commercial identification and marketing tool',font='Arial 12 bold',padx=90).place(relx=.01,rely=.28)
            Label(root,text='Algorithms used in the following Model:',font='Arial 12 bold',padx=90).place(relx=.01,rely=.32)
            Label(root,text='1.Eigen Faces',font='Arial 12 bold',padx=90).place(relx=.01,rely=.36)
            Label(root,text='2.LBPH Faces',font='Arial 12 bold',padx=90).place(relx=.01,rely=.40)
            Label(root,text='3.Fisher Faces(not functional)',font='Arial 12 bold',padx=90).place(relx=.01,rely=.44)
            Button(root,text='  Back ',font='Arial 15 bold',command=home,bg='light blue',fg='black').place(relx=.45,rely=.75)
            Label(root,text='Version 0.1.0 Copyrights(free to copy) 2018',font='Arial 9',padx=90).place(relx=.55,rely=.95)
        
        def contact():
            for widget in root.winfo_children():
                widget.destroy()
            Label(root,text='Facial Recognition System',font='Arial 25 bold',justify='center',bg='light blue').place(relx=0.25,rely=0.0)
            Label(root,text='Facial Recognitin System by:   \n\nAman Kumar Singh 151229\n\n Mob: +919756395388\n\nAnshit Hayaran 151239\n\n Mob: +919454535787    \n\nKartikey Chandola 151305\n\n Mob: +919455060574',font='Arial 14 bold',padx=90).place(relx=.22,rely=.1)
            Button(root,text='  Back ',font='Arial 15 bold',command=home,bg='light blue',fg='black').place(relx=.45,rely=.85)
            Label(root,text='Version 0.1.0 Copyrights(free to copy) 2018',font='Arial 9',padx=90).place(relx=.55,rely=.95)
            
        root=Tk()
        a=PhotoImage(file='face.gif')
        root.geometry('800x600')
        home()
        root.mainloop()
        
h()        
