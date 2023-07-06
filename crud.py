from tkinter import*
from tkinter import ttk
import math,random,os
from tkinter import messagebox
import pymysql
import datetime
class Service_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Two Wheeler Billing System")

        title=Label(self.root,text="Managing Customer Data",bd=0,fg="black",font=("myraid pro",18,"bold"),pady=2).pack(fill=X)
        back_btn=Button(self.root,command=self.goback,text="<<",width=5,border=0,fg="black").place(x=10,y=10)
        
        self.cname=StringVar()
        self.cphone=StringVar()
        self.cbikeno=StringVar()
        self.cbillno=StringVar()
        self.id=StringVar()
        #p=random.randint(1000,9999)
        #self.cbillno.set(str(p))
        
        now = datetime.datetime.now()
        self.interior_parts=StringVar()
        self.exterior_parts=StringVar()
        self.regular_parts=StringVar()
        self.grand_total=StringVar()
        
        self.c_id=StringVar()
        self.customer_name=StringVar()
        self.customer_phone=StringVar()
        self.customer_email=StringVar()
        self.customer_bikeno=StringVar()
        self.bsmodel=StringVar()


        Customer_information=Frame(self.root,bd=4,relief=RIDGE,bg="#7F525D")
        Customer_information.place(x=40,y=115,width=400,height=490)

        c_title=Label(Customer_information,text="Customer Detail",bg="#7F525D",fg="black",font=("times new roman",15,"bold"))
        c_title.grid(row=0,columnspan=2,pady=10)

        id=Label(Customer_information,text="Customer ID",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        id.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        id=Entry(Customer_information,textvariable=self.id,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        id.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        name=Label(Customer_information,text="Customer Name",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        name=Entry(Customer_information,textvariable=self.cname,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        phone=Label(Customer_information,text="Customer Phone No",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        phone.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        phone=Entry(Customer_information,textvariable=self.cphone,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        phone.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        bikeno=Label(Customer_information,text="Customer Bike No",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        bikeno.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        bikeno=Entry(Customer_information,textvariable=self.cbikeno,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        bikeno.grid(row=4,column=1,pady=10,padx=20,sticky="w")

        billno=Label(Customer_information,text="Customer Bill no",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        billno.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        billno=Entry(Customer_information,textvariable=self.cbillno,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        billno.grid(row=5,column=1,pady=10,padx=20,sticky="w")

        interior=Label(Customer_information,text="Interior Parts Price",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        interior.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        interior=Entry(Customer_information,textvariable=self.interior_parts,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        interior.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        exterior=Label(Customer_information,text="Exterior Parts Price",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        exterior.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        exterior=Entry(Customer_information,textvariable=self.exterior_parts,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        exterior.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        regular=Label(Customer_information,text="Regular Parts Price",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        regular.grid(row=8,column=0,pady=10,padx=20,sticky="w")

        regular=Entry(Customer_information,textvariable=self.regular_parts,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        regular.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        total=Label(Customer_information,text="Grand Total",bg="#7F525D",fg="black",font=("Myraid pro",10,"bold"))
        total.grid(row=9,column=0,pady=10,padx=20,sticky="w")

        total=Entry(Customer_information,textvariable=self.grand_total,font=("myraid pro",10,"bold"),bd=0,relief=GROOVE)
        total.grid(row=9,column=1,pady=10,padx=20,sticky="w")


        #addbtn=Button(Customer_information,text="ADD",width=8).grid(row=9,column=0,padx=0,pady=0)
        updatebtn=Button(Customer_information,command=self.update,text="UPDATE",width=8,bg="green").grid(row=10,column=0,padx=0,pady=20)
        deletebtn=Button(Customer_information,command=self.delete,text="DELETE",width=8,bg="green").grid(row=10,column=1,padx=0,pady=0)
        #clearbtn=Button(Customer_information,text="CLEAR",width=8).grid(row=9,column=3,padx=10,pady=10)

        # creating reading data of servicecustomer 
        #service_customer=Frame(self.root,bd=4,relief=RIDGE,bg="#7F525D")
        #service_customer.place(x=500,y=495,width=820,height=190)

        #creating table for customer service scroll bar

        #table_f=Frame(service_customer,bd=4,relief=RIDGE,bg="#7F525D")
        #table_f.place(x=10,y=40,width=790,height=130)

        #customer_title=Label(service_customer,text="Customer Bike Service",bg="#7F525D",fg="black",font=("times new roman",15,"bold"))
        #customer_title.grid(row=0,pady=10,padx=10)

        #scroll_x=Scrollbar(table_f,orient=HORIZONTAL)
        #scroll_y=Scrollbar(table_f,orient=VERTICAL)
        #self.customer_book=ttk.Treeview(table_f,columns=("c_id","customer_name","customer_phone","customer_email","customer_bikeno","bsmodel"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        #scroll_x.pack(side=BOTTOM,fill=X)
        #scroll_y.pack(side=RIGHT,fill=Y)
        #scroll_x.config(command=self.customer_book.xview)
        #scroll_y.config(command=self.customer_book.yview)
        #self.customer_book.heading("c_id",text="ID")
        #self.customer_book.heading("customer_name",text="Customer Name")
        #self.customer_book.heading("customer_phone",text="Customer Phone")
        #self.customer_book.heading("customer_email",text="Customer Email")
        #self.customer_book.heading("customer_bikeno",text="Customer Bike No")
        #self.customer_book.heading("bsmodel",text="Customer Vechicle Model")
        #self.customer_book['show']='headings'
       #self.customer_book.pack(fill=BOTH,expand=1)
        #self.customer_book.bind("<ButtonRelease-1>",self.got_cursor)
        #self.customer_book.pack()
        #self.getdata()

    #def got_cursor(self,ev):
        #cursor_row=self.customer_book.focus()
        #contents=self.customer_book.item(cursor_row)
        #row=contents['values']
        #self.c_id.set(row[0])
        #self.customer_name.set(row[1])
        #self.customer_phone.set(row[2])
        #self.customer_email.set(row[3])
        #self.customer_bikeno.set(row[4])
        #self.bsmodel.set(row[5])
        #self.getdata()

    

    #def getdata(self):
        #con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
        #now = datetime.datetime.now()
        #cur=con.cursor()
        #cur.execute("select * from customer_bookform") 
        #rows=cur.fetchall() 
        #if len(rows)!=0:
            #self.customer_book.delete(*self.customer_book.get_children())
            #for row in rows:
                #self.customer_book.insert('',END,values=row)
    

    
        #creating reading data 

        Customer_d=Frame(self.root,bd=4,relief=RIDGE,bg="#7F525D")
        Customer_d.place(x=500,y=50,width=820,height=620)

        showbtn=Button(Customer_d,text="Show All",width=8,pady=5).grid(row=0,column=3,padx=10,pady=10)


        #creating table for scroll bar

        table=Frame(Customer_d,bd=4,relief=RIDGE,bg="crimson")
        table.place(x=10,y=70,width=790,height=530)

        # customer detail of scroll bar

        scroll_x=Scrollbar(table,orient=HORIZONTAL)
        scroll_y=Scrollbar(table,orient=VERTICAL)
        self.customer_info=ttk.Treeview(table,columns=("id","cname","cphone","cbikeno","cbillno","interior_parts","exterior_parts","regular_parts","grand_total","datetime"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.customer_info.xview)
        scroll_y.config(command=self.customer_info.yview)
        self.customer_info.heading("id",text="Customer ID")
        self.customer_info.heading("cname",text="Customer Name")
        self.customer_info.heading("cphone",text="Customer Phone No")
        self.customer_info.heading("cbikeno",text="Customer Bike No")
        self.customer_info.heading("cbillno",text="Customer Bill No")
        self.customer_info.heading("interior_parts",text="Interior Parts Price")
        self.customer_info.heading("exterior_parts",text="Exterior Parts Price")
        self.customer_info.heading("regular_parts",text="Regular Parts Price")
        self.customer_info.heading("grand_total",text="Grand Total")
        self.customer_info.heading("datetime",text="Date and Time")
        self.customer_info['show']='headings'
        self.customer_info.pack(fill=BOTH,expand=1)
        self.customer_info.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetchdata()

        #self.customer_info.pack()

    def get_cursor(self,ev):
        cursor_row=self.customer_info.focus()
        contents=self.customer_info.item(cursor_row)
        row=contents['values']
        self.id.set(row[0])
        self.cname.set(row[1])
        self.cphone.set(row[2])
        self.cbikeno.set(row[3])
        self.cbillno.set(row[4])
        self.interior_parts.set(row[5])
        self.exterior_parts.set(row[6])
        self.regular_parts.set(row[7])
        self.grand_total.set(row[8])

    

    def goback(self):
        self.root.destroy()
        import service

    

    #fetching data in scroll bar from database

    def fetchdata(self):
        con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
        #now = datetime.datetime.now()
        cur=con.cursor()
        now = datetime.datetime.now()
        cur.execute("select * from tservices") 
        rows=cur.fetchall() 
        if len(rows)!=0:
            self.customer_info.delete(*self.customer_info.get_children())
            for row in rows:
                self.customer_info.insert('',END,values=row)

            con.commit()
            con.close()

    def update(self):
        if self.cname.get()=="" or self.cphone.get()=="":
            messagebox.showerror("Error","Field empty")
        else:
            con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
            cur=con.cursor()
            cur.execute("update tservices set c_name=%s,c_phoneno=%s where id=%s",(self.cname.get(),self.cphone.get(),self.id.get()))
            messagebox.showinfo("Sucess","Successfully Updated")
            con.commit()
            self.fetchdata()
            con.close()

    def delete(self):
        if self.cbikeno.get()=="":
            messagebox.showerror("Error","Empty Field")
        else:
            con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
            cur=con.cursor()
            cur.execute("delete from tservices where id=%s",self.id.get())
            messagebox.showinfo("Sucess","Customer Info Deleted Successfully ")
            con.commit()
            self.fetchdata()
            con.close()
        







        




root=Tk()
obj=Service_App(root)
root.mainloop()
