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
        self.root.title("Customer Login Form")
        self.root["bg"]="#9DF9EF"

         #form variables
        self.contact=StringVar()
        self.password=StringVar()

        #form title
        label_title = Label(self.root,text="Customer Login Form",bg="#9DF9EF",width = 20,font=("Myraid pro",20,"bold"))
        label_title.place(x=90,y=53)

        label_contact = Label(self.root,text="Contact No", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=77,y=130)
        entry_contact = Entry(self.root,width=20,textvariable=self.contact)
        entry_contact.place(x=240,y=130)
        #Contact Validation
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate="key", validatecommand=(validate_contact,"%P"))

        label_password = Label(self.root,text="Password", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=75,y=190)
        entry_password = Entry(self.root,width=20,show="*",textvariable=self.password)
        entry_password.place(x=240,y=190)

        #login button
        sub_btn=Button(self.root,text="Login",width=10,bg="green",command=self.validation,fg="white").place(x=80,y=250)
        clear_btn=Button(self.root,text="Clear",width=10,command=self.clear,bg="green",fg="white").place(x=200,y=250)
        login_btn=Button(self.root,text="Back To Register",command=self.log,width=15,bg="Blue",fg="white").place(x=320,y=250)
        forp_btn=Button(self.root,text="Forget Password ?",command=self.forgot,width=17,bg="#9DF9EF",border=0,fg="black").place(x=180,y=300)
        


    def clear(self):
        self.email.set("")
        self.password.set("")

        #form validation
    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Contact Number")
            return False

        
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
        if self.contact.get()=="":
            messagebox.showerror("Error","Please enter your Conatct Number",parent=self.root) 
        elif self.password.get()=="":
            messagebox.showerror("Error","Please enter your password")
        else:
            con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
            cur=con.cursor()
            cur.execute("select * from customer_register where contact=%s and password=%s",
                       (self.contact.get(),self.password.get())
                       ) 
            row=cur.fetchone()
            if row==None:
                messagebox.showerror("Alert","Incorrect contact or password")   
                return 
            else:
                cur.execute("insert into customer_login(contact,password) values(%s,%s)",
                           (self.contact.get(),self.password.get())
                           )
                messagebox.showinfo("Success","Login Successfully") 
                con.commit()
                con.close()   
                self.root.destroy()
                import customerbook  
            
    def log(self):
        self.root.destroy()
        import customerregister

    def forgot(self):
        self.root.destroy()
        import customerforgetpassword


root=Tk()
obj=login_sys(root)
root.mainloop()
