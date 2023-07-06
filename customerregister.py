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
        self.root.geometry("500x550+300+300")
        self.root.title("Customer Registration Form")
        self.root["bg"]="#9DF9EF"

        #form variables
        self.fname=StringVar()
        self.lname=StringVar()
        self.password=StringVar()
        self.conpassword=StringVar()
        self.contact=StringVar()
        self.email=StringVar()

        #form title
        label_title = Label(self.root,text="Customer Registration",bg="#9DF9EF",width = 20,font=("Myraid pro",20,"bold"))
        label_title.place(x=90,y=53)

        label_fname = Label(self.root,text="First name", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=64,y=130)
        entry_fname = Entry(self.root,width=20,textvariable=self.fname)
        entry_fname.place(x=240,y=130)
        #fname validation
        validate_fname=self.root.register(self.checkfname)
        entry_fname.config(validate="key", validatecommand=(validate_fname,"%P"))


        label_lname = Label(self.root,text="Last name", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=62,y=190)
        entry_lname = Entry(self.root,width=20,textvariable=self.lname)
        entry_lname.place(x=240,y=190)
        #lname validation
        validate_lname=self.root.register(self.checklname)
        entry_lname.config(validate="key", validatecommand=(validate_lname,"%P"))

        label_contact = Label(self.root,text="Contact", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=57,y=250)
        entry_contact = Entry(self.root,width=20,textvariable=self.contact)
        entry_contact.place(x=240,y=250)
        #Contact Validation
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate="key", validatecommand=(validate_contact,"%P"))

        label_email = Label(self.root,text="Email", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=53,y=310)
        entry_email = Entry(self.root,width=20,textvariable=self.email)
        entry_email.place(x=240,y=310)

        label_password = Label(self.root,text="Password", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=62,y=370)
        entry_password = Entry(self.root,width=20,show="*",textvariable=self.password)
        entry_password.place(x=240,y=370)

        label_conpassword = Label(self.root,text="Confirm Password", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=81,y=430)
        entry_conpassword = Entry(self.root,width=20,show="*",textvariable=self.conpassword)
        entry_conpassword.place(x=240,y=430)

        #for button
        sub_btn=Button(self.root,text="Register",command=self.validation,width=10,bg="green",fg="white").place(x=80,y=485)
        clear_btn=Button(self.root,text="Clear",command=self.clear,width=10,bg="green",fg="white").place(x=200,y=485)
        login_btn=Button(self.root,text="Back To Login",command=self.log,width=10,bg="Blue",fg="white").place(x=320,y=485)
        
        #for clear button

    def clear(self):
        self.fname.set("")
        self.lname.set("")
        self.contact.set("")
        self.email.set("")
        self.password.set("")
        self.conpassword.set("")
    

        #form validation and call back function
    def checkfname(self,fname):
        if fname.isalnum():
            return True
        if fname=="":
            return True
        else:
            messagebox.showwarning("Invalid","Not Allowed"+fname[-1])
            return False
        
    def checklname(self,lname):
        if lname.isalnum():
            return True
        if lname=="":
            return True
        else:
            messagebox.showwarning("Invalid","Not Allowed"+lname[-1])
            return False
        
    
    def checkemail(self,email):
        if len(email)>7:
            if re.match("^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$",email):
                return True
            else:
                messagebox.showwarning("Alert","Invalid email enter valid email")
                return False
        else:
            messagebox.showinfo("Invalid","Email length is too small")

    def checkcontact(self,contact):
        if contact.isdigit():
            return True
        if len(str(contact))==0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Contact Number")
            return False
        
    
    def checkconpassword(self,conpassword):
        if len(conpassword)<10:
            if re.match("^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z](?=.*[^a-bA-B0-9]))",conpassword):
                return True
            else:
                messagebox.showwarning("Invalid","Enter valid password")
                return False
        else:
            messagebox.showwarning("invalid","Length try to exceed")
            
    
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
        if self.fname.get()=="":
            messagebox.showerror("Error","Please enter your first name",parent=self.root)
        elif self.lname.get()=="":
            messagebox.showerror("Error","Please enter your last name",parent=self.root)
        elif self.contact.get()=="" or len(self.contact.get())!=10:
            messagebox.showerror("Error","Please enter your valid contact",parent=self.root)
        elif self.email.get()=="":
            messagebox.showerror("Error","Please enter your email",parent=self.root)
        elif self.password.get()=="":
            messagebox.showerror("Error","Please enter your passwsord",parent=self.root)
        elif self.conpassword.get()=="":
            messagebox.showerror("Error","Please enter your confirm passwsord",parent=self.root)
        elif self.password.get()!= self.conpassword.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        elif self.email.get()!=None and self.password.get()!=None:
            x=self.checkemail(self.email.get())
            y=self.checkpassword(self.password.get())

        if (x == True) and (y == True):
            try:
                   con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
                   cur=con.cursor()
                   cur.execute("select * from customer_register where contact=%s",self.contact.get())
                   row=cur.fetchone()
                   if row!=None:
                       messagebox.showerror("Error","Contact Number Already Exist",parent=self.root)
                   else:
                       cur.execute("insert into customer_register (f_name, l_name, contact, email, password, confirmpassword) values(%s,%s,%s,%s,%s,%s)",
                                  (self.fname.get(),self.lname.get(),self.contact.get(),self.email.get(),self.password.get(),self.conpassword.get())
                                  )                        
                       con.commit()
                       con.close()
                       messagebox.showinfo("Done","SuccessFully Registered")
            except Exception as es:
                    messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                    


    
            
    
    def log(self):
        self.root.destroy()
        import customerlogin

root=Tk()
obj=login_sys(root)
root.mainloop()


