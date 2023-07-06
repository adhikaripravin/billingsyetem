from tkinter import*
from tkinter import messagebox
#from PIL import ImageTk
from tkinter import ttk
import pymysql
import re
class login_sys:
    def __init__(self,root):
        self.root=root
        self.root.resizable(0,0)
        self.root.geometry("500x360+200+200")
        self.root.title("Login Form")
        self.root["bg"]="#7F525D"

         #form variables
        self.email=StringVar()
        self.password=StringVar()

        #form title
        label_title = Label(self.root,text="Login Form",bg="#7F525D",width = 20,font=("Myraid pro",20,"bold"))
        label_title.place(x=90,y=53)

        label_email = Label(self.root,text="Email", width=20,bg="#7F525D",font=("Myraid pro",10,"bold")).place(x=68,y=130)
        entry_email = Entry(self.root,width=20,textvariable=self.email)
        entry_email.place(x=240,y=130)

        label_password = Label(self.root,text="Password", width=20,bg="#7F525D",font=("Myraid pro",10,"bold")).place(x=75,y=190)
        entry_password = Entry(self.root,width=20,show="*",textvariable=self.password)
        entry_password.place(x=240,y=190)

        #login button
        sub_btn=Button(self.root,text="Login",width=10,bg="green",command=self.validation,fg="white").place(x=80,y=250)
        clear_btn=Button(self.root,text="Clear",width=10,command=self.clear,bg="green",fg="white").place(x=200,y=250)
        login_btn=Button(self.root,text="Back To Register",command=self.log,width=15,bg="Blue",fg="white").place(x=320,y=250)
        forp_btn=Button(self.root,text="Forget Password ?",command=self.forgot,width=17,bg="#7F525D",border=0,fg="black").place(x=180,y=300)
        


    def clear(self):
        self.email.set("")
        self.password.set("")

        #form validation
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

    def validation(self):
        if self.email.get()=="":
            messagebox.showerror("Error","Please enter your email",parent=self.root) 
        elif self.password.get()=="":
            messagebox.showerror("Error","Please enter your password")
        else:
            con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
            cur=con.cursor()
            cur.execute("select * from register where email=%s and password=%s",
                       (self.email.get(),self.password.get())
                       ) 
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Alert","Incorrect email or password")   
                return 
            else:
                cur.execute("insert into login(email,password) values(%s,%s)",
                           (self.email.get(),self.password.get())
                           )
                messagebox.showinfo("Success","Login Successfully") 
                con.commit()
                con.close()   
                self.root.destroy()
                import service  
            
    def log(self):
        self.root.destroy()
        import register

    def forgot(self):
        self.root.destroy()
        import forgetpassword


root=Tk()
obj=login_sys(root)
root.mainloop()
