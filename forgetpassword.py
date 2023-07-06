from tkinter import*
from tkinter import messagebox
#from PIL import ImageTk
from tkinter import ttk
import pymysql
import re
class forgetpassword_sys:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.geometry("500x380+200+200")
        self.root.title("Forget Password")
        self.root["bg"]="#7F525D"

        #form variables
        self.email=StringVar()
        self.password=StringVar()
        self.conpassword=StringVar()

        #form title
        label_title = Label(self.root,text="Forget Password ?",bg="#7F525D",width = 20,font=("Myraid pro",20,"bold"))
        label_title.place(x=90,y=53)

        label_email = Label(self.root,text="Email", width=20,bg="#7F525D",font=("Myraid pro",10,"bold")).place(x=68,y=130)
        entry_email = Entry(self.root,width=20,textvariable=self.email)
        entry_email.place(x=240,y=130)

        label_password = Label(self.root,text="New Password", width=20,bg="#7F525D",font=("Myraid pro",10,"bold")).place(x=65,y=190)
        entry_password = Entry(self.root,width=20,show="*",textvariable=self.password)
        entry_password.place(x=240,y=190)

        label_conpassord = Label(self.root,text="Confirm New Password", width=20,bg="#7F525D",font=("Myraid pro",10,"bold")).place(x=57,y=250)
        entry_conpassword = Entry(self.root,width=20,show="*",textvariable=self.conpassword)
        entry_conpassword.place(x=240,y=250)

        #for button
        sub_btn=Button(self.root,text="Submit",width=10,bg="green",command=self.submit,fg="white").place(x=200,y=310)
        back_btn=Button(self.root,command=self.goback,text="<<",width=5,border=0,bg="#7F525D",fg="white").place(x=10,y=10)

    def goback(self):
        self.root.destroy()
        import logi
    


    def checkemail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                messagebox.showwarning("Alert","Invalid email enter valid email")
                return False
        else:
            messagebox.showinfo("Invalid","Email length is too small")

    def checkpassword(self,password):
        if len(password)<10:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",password):
                return True
            else:
                messagebox.showwarning("Invalid","Enter valid password")
                return False
        else:
            messagebox.showwarning("invalid","Length try to exceed")

    def checkconpassword(self,conpassword):
        if len(conpassword)<10:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",conpassword):
                return True
            else:
                messagebox.showwarning("Invalid","Enter valid password")
                return False
        else:
            messagebox.showwarning("invalid","Length try to exceed")

    
    def submit(self):
        if self.email.get()=="" or self.password.get()=="" or self.conpassword.get()=="":
            messagebox.showerror("Error","All Field should be Entered")
        elif self.password.get()!=self.conpassword.get():
            messagebox.showerror("Error","Password Does not Match")
        elif self.email.get()!=None and self.password.get()!=None:
             x=self.checkemail(self.email.get())
             y=self.checkpassword(self.password.get())
        if (x == True) and (y == True):
            try:
               con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
               cur=con.cursor()
               cur.execute("select * from register where email=%s",self.email.get())
               row=cur.fetchone()
               if row==None:
                   messagebox.showerror("Alert","This email address does not exit.please enter valid email address")   
               else:
                   cur.execute("update register set password=%s, confirm_password=%s where email=%s",
                              (self.password.get(),self.conpassword.get(),self.email.get())
                              )
                   con.commit()
                   con.close() 
                   messagebox.showinfo("Success","Your Password has been Changed Successfully") 

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                self.root.destroy()
                import logi
                
    

root=Tk()
obj=forgetpassword_sys(root)
root.mainloop()
