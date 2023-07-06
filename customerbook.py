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
        self.root.title("Customer Booking Form")
        self.root["bg"]="#9DF9EF"

        #form variables
        self.customer_name=StringVar()
        self.customer_phone=StringVar()
        self.customer_email=StringVar()
        self.customer_bikeno=StringVar()
        self.bsmodel=StringVar()

        #form title
        label_title = Label(self.root,text="Service Your Vechicle ?",bg="#9DF9EF",width = 20,font=("Myraid pro",20,"bold"))
        label_title.place(x=90,y=53)

        label_name = Label(self.root,text="Full name", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=64,y=130)
        entry_name = Entry(self.root,width=20,textvariable=self.customer_name)
        entry_name.place(x=240,y=130)
        #fname validation
        validate_name=self.root.register(self.checkname)
        entry_name.config(validate="key", validatecommand=(validate_name,"%P"))

        label_contact = Label(self.root,text="Phone No", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=62,y=190)
        entry_contact = Entry(self.root,width=20,textvariable=self.customer_phone)
        entry_contact.place(x=240,y=190)
        #Contact Validation
        validate_contact=self.root.register(self.checkcontact)
        entry_contact.config(validate="key", validatecommand=(validate_contact,"%P"))

        label_email = Label(self.root,text="Email", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=52,y=250)
        entry_email = Entry(self.root,width=20,textvariable=self.customer_email)
        entry_email.place(x=240,y=250)
        

        label_bikeno = Label(self.root,text="Bike No", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=53,y=310)
        entry_bikeno = Entry(self.root,width=20,textvariable=self.customer_bikeno)
        entry_bikeno.place(x=240,y=310)
        #bikeno Validation
        validate_bikeno=self.root.register(self.checkbikeno)
        entry_bikeno.config(validate="key", validatecommand=(validate_bikeno,"%P"))

        label_model = Label(self.root,text="Bike Model", width=20,bg="#9DF9EF",font=("Myraid pro",10,"bold")).place(x=62,y=370)
        entry_model = Entry(self.root,width=20,textvariable=self.bsmodel)
        entry_model.place(x=240,y=370)
        #model Validation
        validate_model=self.root.register(self.checkmodel)
        entry_model.config(validate="key", validatecommand=(validate_model,"%P"))


        #for button
        sub_btn=Button(self.root,text="Submit for Vechicle Servicing",command=self.validation,width=22,bg="green",fg="white").place(x=81,y=430)
        clear_btn=Button(self.root,text="Clear",width=10,bg="blue",fg="white").place(x=330,y=430)
        #login_btn=Button(self.root,text="Back To Login",width=10,bg="Blue",fg="white").place(x=320,y=485)
        
        #for clear button

    
    

        #form validation and call back function
    def checkname(self,name):
        if name.isalnum():
            return True
        if name=="":
            return True
        else:
            messagebox.showwarning("Invalid","Not Allowed"+name[-1])
            return False
        
    def checkbikeno(self,bikeno):
        if bikeno.isdigit():
            return True
        if len(str(bikeno))==0:
            return True
        else:
            messagebox.showwarning("Invalid","Invalid Bike no Number")
            return False
        
    def checkmodel(self,model):
        if model.isalnum():
            return True
        if model=="":
            return True
        else:
            messagebox.showwarning("Invalid","Not Allowed")
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
        
    
    def validation(self):
        if self.customer_name.get()=="":
            messagebox.showerror("Error","Please enter your first name",parent=self.root)
        elif self.customer_phone.get()=="":
            messagebox.showerror("Error","Please enter your password",parent=self.root)
        elif self.customer_phone.get()=="" or len(self.customer_phone.get())!=10:
            messagebox.showerror("Error","Please enter your valid contact",parent=self.root)
        elif self.customer_bikeno.get()=="" or len(self.customer_bikeno.get())!=4:
            messagebox.showerror("Error","Please enter your Bike No",parent=self.root)
        elif self.customer_email.get()=="":
            messagebox.showerror("Error","Please enter your email",parent=self.root)
        elif self.bsmodel.get()=="":
            messagebox.showerror("Error","Please enter your Bike model",parent=self.root)
        elif self.customer_email.get()!=None:
            x=self.checkemail(self.customer_email.get())

        if (x == True):
            try:
                   con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
                   cur=con.cursor()
                   cur.execute("insert into customer_bookform (name, phone, email, bikeno, model) values(%s,%s,%s,%s,%s)",
                              (self.customer_name.get(),self.customer_phone.get(),self.customer_email.get(),self.customer_bikeno.get(),self.bsmodel.get())
                              )                        
                   con.commit()
                   con.close()
                   messagebox.showinfo("Successfully Submitted","Service Provider will contact you on register phone number")
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
                    

root=Tk()
obj=login_sys(root)
root.mainloop()


