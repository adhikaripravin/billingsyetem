from tkinter import*
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql
import re
class home_sys:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.geometry("1350x700+0+0")
        self.root.title("WELCOME TO TWO WHELLER BILLING SYSTEM")
        self.root["bg"]="#7F525D"
        
        #for background image
        self.bg=ImageTk.PhotoImage(file='bg.png')
        #bg_lbl=Label(self.root,image=self.bg,bd=2,relief=RAISED)
        #bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        #bg_lbl.grid(row=0,column=0,padx=40,pady=10)


        #form title
        label_title = Label(self.root,text="Welcome to Two Wheller Billing System",bg="#7F525D",width = 45,font=("Dolphin",40,"bold"))
        label_title.place(x=40,y=53)
        label_text = Label(self.root,text="User Login", width=20,bg="#7F525D",font=("Myraid pro",30,"bold")).place(x=450,y=200)
        #label_text = Label(self.root,text="Customer Login", width=20,bg="#7F525D",font=("Myraid pro",30,"bold")).place(x=800,y=200)
        label_text = Label(self.root,text="Already have an account ?", width=20,bg="#7F525D",font=("Myraid pro",17)).place(x=560,y=280)
        label_text = Label(self.root,text="Don't have an account ?", width=20,bg="#7F525D",font=("Myraid pro",17)).place(x=560,y=410)
        #label_text = Label(self.root,text="Already have an account ?", width=20,bg="#7F525D",font=("Myraid pro",17)).place(x=910,y=280)
        #label_text = Label(self.root,text="Don't have an account ?", width=20,bg="#7F525D",font=("Myraid pro",17)).place(x=910,y=410)
        log_btn=Button(self.root,command=self.ulog,text="Login",bd=0,width=10,bg="#7F525D",font=("Myraid pro",25,"bold")).place(x=580,y=330)
        log_btn=Button(self.root,command=self.ureg,text="Register",bd=0,width=10,bg="#7F525D",font=("Myraid pro",25,"bold")).place(x=580,y=460)
        #log_btn=Button(self.root,command=self.clog,text="Login",bd=0,width=10,bg="#7F525D",font=("Myraid pro",25,"bold")).place(x=920,y=330)
        #register_btn=Button(self.root,command=self.creg,text="Register",bd=0,bg="#7F525D",width=10,font=("Myraid pro",25,"bold")).place(x=920,y=460)

    def ulog(self):
        self.root.destroy()
        import logi

        
    def ureg(self):
        self.root.destroy()
        import register

    #def clog(self):
        #self.root.destroy()
        #import customerlogin

    #def creg(self):
        #self.root.destroy()
        #import customerregister



root=Tk()
obj=home_sys(root)
root.mainloop()