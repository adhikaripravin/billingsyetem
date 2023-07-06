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
        
        
        self.cbikeno=StringVar()
        self.gtotal=StringVar()
        self.id=StringVar()
        #self.tdiscount=StringVar()
        #self.gprice=StringVar()

        
        title=Label(self.root,text="Two Wheeler Billing System",bd=12,bg="#FF6A6A",fg="black",font=("dolphin",30,"bold"),pady=2).pack(fill=X)
        
        #bikeno_label=Label(self.root,text="Bike No",bg="#FF6A6A", fg="black", font=("Myraid pro",12,"bold")).place(x=1060,y=12,height=30,width=150)
        #bikeno_txt=Entry(self.root,width=12,textvariable=self.cbikeno,bd=0,font=("times new roman",15)).place(x=1185,y=12,height=30,width=150)
        #gtotal_label=Label(self.root,text="Grand Total",bg="#FF6A6A", fg="black", font=("Myraid pro",12,"bold")).place(x=1060,y=45,height=30,width=150)
        #gtotal_txt=Entry(self.root,width=12,textvariable=self.gtotal,bd=0,font=("times new roman",15)).place(x=1185,y=45,height=30,width=150)
        

        #this is variables
        #variables of customer information
        self.cname=StringVar()
        self.cphone=StringVar()
        self.cbillno=StringVar()
        p=random.randint(1000,9999)
        self.cbillno.set(str(p))

        #for interior parts variables
        self.air_filter=IntVar()
        self.led_light=IntVar()
        self.spark_plug=IntVar()
        self.chain_spocket=IntVar()
        self.cone_bearing=IntVar()
        self.brake_cable=IntVar()
        self.battery=IntVar()
        self.throttle_wire=IntVar()
        self.circuit=IntVar()
        self.lub_filter=IntVar()
        self.disk_pad=IntVar()
        self.starter_switch=IntVar()
        self.choke=IntVar()
        self.tachometer=IntVar()
        self.transmission=IntVar()
        self.piston=IntVar()

        #for exterior part variables
        self.clutch_lever=IntVar()
        self.gear_shifter=IntVar()
        self.horn=IntVar()
        self.pegs=IntVar()
        self.engine_guard=IntVar()
        self.signal_light=IntVar()
        self.headlight=IntVar()
        self.mirror=IntVar()
        self.fuel_tank=IntVar()
        self.tire=IntVar()
        self.rear_suspension=IntVar()
        self.exhaust_pipe=IntVar()
        self.seat=IntVar()
        self.dashboard=IntVar()
        self.kickstand=IntVar()
        self.rims=IntVar()

        #for regular servicing parts variables
        self.servicing=IntVar()
        self.lub=IntVar()

        

        #for grand total variables
        self.interior_parts=StringVar()
        self.exterior_parts=StringVar()
        self.regular_parts=StringVar()
        self.grand_total=StringVar()
        self.discount=StringVar()
        self.final_total=StringVar()
        self.tdiscount=StringVar()
        self.gprice=StringVar()

        self.dis=StringVar()

        self.idis=StringVar()
        self.edis=StringVar()
        self.rdis=StringVar()

        self.idi=StringVar()
        self.edi=StringVar()
        self.rdi=StringVar()

        #for customer info
        F1=LabelFrame(self.root,text="CUSTOMER INFORMATION",bg="#8DB6CD",fg="black",font=("Myraid pro",15,"bold"))
        F1.place(x=0,y=85,relwidth=1)

        label_cname=Label(F1,text="Customer Name",bg="#8DB6CD",fg="black",font=("Myraid pro",15,"bold")).grid(row=0,column=0,padx=50,pady=10)
        entry_cname=Entry(F1,width=13,bd=0,textvariable=self.cname,font=("Myraid pro",15)).grid(row=0,column=1,padx=10,pady=10)
        
        cphone_label=Label(F1,text="Customer Phone No",bg="#8DB6CD",fg="black",font=("Myraid pro",15,"bold")).grid(row=0,column=2,padx=10,pady=10)
        cphoneno_txt=Entry(F1,width=13,bd=0,textvariable=self.cphone,font=("Myraid pro",15)).grid(row=0,column=3,padx=15,pady=10)

        #cservicebillno_label=Label(F1,text="Customer Service Bill No",bg="#8DB6CD",fg="black",font=("Myraid pro",15,"bold")).grid(row=0,column=4,padx=10,pady=10)
        #cservicebillno_txt=Entry(F1,width=13,bd=0,textvariable=self.cbillno,font=("Myraid pro",15)).grid(row=0,column=5,padx=15,pady=10)
        
        bikeno_label=Label(F1,text="Bike No",bg="#8DB6CD", fg="black", font=("Myraid pro",15,"bold")).grid(row=0,column=4,padx=10,pady=10)
        bikeno_txt=Entry(F1,width=13,textvariable=self.cbikeno,bd=0,font=("Myraid pro",15)).grid(row=0,column=5,padx=15,pady=10)
        

        bill_btn=Button(F1,text="Search",width=8,border=0,command=self.find_bill,font=("Myraid pro",10,"bold")).grid(row=0,column=6)
        #F2=Frame(self.root,bd=10,bg="light green")
        #F2.place(x=1071,y=172,height=200)

        #title=Label(F2,text="Regular Servicing Parts",bd=8,bg="light green",fg="black",font=("Myraid pro",15,"bold")).grid(row=0,columnspan=2,padx=0,pady=2)

        #lubtype_label=Label(F2,text="Lubricant Type",bg="light green",fg="black",font=("Myraid pro",10,"bold")).grid(row=1,column=0,padx=0,pady=20,sticky="w")
        #lubtype_txt=Entry(F2,width=15,bd=5,font=("Myraid pro",15,"bold")).grid(row=1,column=1,padx=0,pady=10)
        
        #lubfilter_label=Label(F2,text="Lubricant Filter",bg="light green",fg="black",font=("Myraid pro",10,"bold")).grid(row=2,column=0,padx=0,pady=20)
        #lubfilter_txt=Entry(F2,width=15,bd=5,font=("Myraid pro",15,"bold")).grid(row=2,column=1,padx=0,pady=10)
        
        F8=Frame(self.root,bd=10,relief=GROOVE)
        F8.place(x=1,y=175,width=380,height=410)
        bill_title=Label(F8,text="Payment Section",font="arial 15 bold",bd=7).pack(fill=X)
        scrol_y=Scrollbar(F8,orient=VERTICAL)
        self.txtarea=Text(F8,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #frame and label of interior parts
        F3=Frame(self.root,bd=10,bg="#FFD39B")
        F3.place(x=380,y=172,width=480,height=410)

        title=Label(F3,text="Interior Parts",bd=8,bg="#FFD39B",fg="black",font=("Myraid pro",15,"bold")).grid(row=0,columnspan=2,padx=50,pady=2)

        F3_label=Label(F3,text="Air Filter",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=1,column=0,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.air_filter,font=("times new roman",15)).grid(row=1,column=1,padx=0,pady=10, sticky="w")
        
        F3_label=Label(F3,text="Led Headlight",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=2,column=0,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.led_light,font=("times new roman",15)).grid(row=2,column=1,padx=0,pady=10, sticky="w")

        F3_label=Label(F3,text="Spark Plug",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=3,column=0,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.spark_plug,font=("times new roman",15)).grid(row=3,column=1,padx=0,pady=10, sticky="w" )
        
        F3_label=Label(F3,text="Chain Spocket",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=4,column=0,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.chain_spocket,font=("times new roman",15)).grid(row=4,column=1,padx=0,pady=10, sticky="w")

        F3_label=Label(F3,text="Cone Bearing",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=5,column=0,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.cone_bearing,font=("times new roman",15)).grid(row=5,column=1,padx=0,pady=10, sticky="w")
        
        F3_label=Label(F3,text="Brake Cable",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=6,column=0,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.brake_cable,font=("times new roman",15)).grid(row=6,column=1,padx=0,pady=10, sticky="w")

        F3_label=Label(F3,text="Battery",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=7,column=0,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.battery,font=("times new roman",15)).grid(row=7,column=1,padx=0,pady=10, sticky="w")
        
        F3_label=Label(F3,text="Throttle Wire",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=8,column=0,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.throttle_wire,font=("times new roman",15)).grid(row=8,column=1,padx=0,pady=10, sticky="w")

        #label of interior part2

        F3_label=Label(F3,text="Circuit",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=1,column=5,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.circuit,font=("times new roman",15)).grid(row=1,column=6,padx=60,pady=10, sticky="w")
        
        F3_label=Label(F3,text="Lubricant Filter",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=2,column=5,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.lub_filter,font=("times new roman",15)).grid(row=2,column=6,padx=60,pady=10, sticky="w")

        F3_label=Label(F3,text="Disk Pad",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=3,column=5,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.disk_pad,font=("times new roman",15)).grid(row=3,column=6,padx=60,pady=10, sticky="w")
        
        F3_label=Label(F3,text="Starter Switch",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=4,column=5,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.starter_switch,font=("times new roman",15)).grid(row=4,column=6,padx=60,pady=10, sticky="w")

        F3_label=Label(F3,text="Choke",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=5,column=5,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.choke,font=("times new roman",15)).grid(row=5,column=6,padx=60,pady=10, sticky="w")
        
        F3_label=Label(F3,text="Tachometer",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=6,column=5,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.tachometer,font=("times new roman",15)).grid(row=6,column=6,padx=60,pady=10, sticky="w")

        F3_label=Label(F3,text="Transmission",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=7,column=5,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.transmission,font=("times new roman",15)).grid(row=7,column=6,padx=60,pady=10, sticky="w")
        
        F3_label=Label(F3,text="Piston",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=8,column=5,padx=0,pady=3, sticky="w")
        F3_txt=Entry(F3,width=5,bd=0,textvariable=self.piston,font=("times new roman",15)).grid(row=8,column=6,padx=60,pady=10, sticky="w")

        #frame and label of exterior parts

        F6=Frame(self.root,bd=10,bg="#FFD39B")
        F6.place(x=865,y=172,width=480,height=410)

        title=Label(F6,text="Exterior Parts",bd=8,bg="#FFD39B",fg="black",font=("Myraid pro",15,"bold")).grid(row=0,columnspan=2,padx=50,pady=2)

        F6_label=Label(F6,text="Clutch Lever",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=1,column=0,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.clutch_lever,font=("times new roman",15)).grid(row=1,column=1,padx=0,pady=10, sticky="w")
        
        F6_label=Label(F6,text="Gear Shifter",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=2,column=0,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.gear_shifter,font=("times new roman",15)).grid(row=2,column=1,padx=0,pady=10, sticky="w")

        F6_label=Label(F6,text="Horn",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=3,column=0,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.horn,font=("times new roman",15)).grid(row=3,column=1,padx=0,pady=10, sticky="w" )
        
        F6_label=Label(F6,text="Pegs",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=4,column=0,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.pegs,font=("times new roman",15)).grid(row=4,column=1,padx=0,pady=10, sticky="w")

        F6_label=Label(F6,text="Engine Guard",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=5,column=0,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.engine_guard,font=("times new roman",15)).grid(row=5,column=1,padx=0,pady=10, sticky="w")
        
        F6_label=Label(F6,text="Signal Lights",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=6,column=0,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.signal_light,font=("times new roman",15)).grid(row=6,column=1,padx=0,pady=10, sticky="w")

        F6_label=Label(F6,text="HeadLights",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=7,column=0,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.headlight,font=("times new roman",15)).grid(row=7,column=1,padx=0,pady=10, sticky="w")
        
        F6_label=Label(F6,text="Mirror",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=8,column=0,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.mirror,font=("times new roman",15)).grid(row=8,column=1,padx=0,pady=10, sticky="w")

        #label of exterior part2

        F6_label=Label(F6,text="Fuel Tank",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=1,column=5,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.fuel_tank,font=("times new roman",15)).grid(row=1,column=6,padx=40,pady=10, sticky="w")
        
        F6_label=Label(F6,text="Tires",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=2,column=5,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.tire,font=("times new roman",15)).grid(row=2,column=6,padx=40,pady=10, sticky="w")

        F6_label=Label(F6,text="Rear Suspension",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=3,column=5,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.rear_suspension,font=("times new roman",15)).grid(row=3,column=6,padx=40,pady=10, sticky="w")
        
        F6_label=Label(F6,text="Exhaust Pipe",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=4,column=5,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.exhaust_pipe,font=("times new roman",15)).grid(row=4,column=6,padx=40,pady=10, sticky="w")

        F6_label=Label(F6,text="Seat",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=5,column=5,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.seat,font=("times new roman",15)).grid(row=5,column=6,padx=40,pady=10, sticky="w")
        
        F6_label=Label(F6,text="DashBoard",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=6,column=5,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.dashboard,font=("times new roman",15)).grid(row=6,column=6,padx=40,pady=10, sticky="w")

        F6_label=Label(F6,text="Kickstand",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=7,column=5,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.kickstand,font=("times new roman",15)).grid(row=7,column=6,padx=40,pady=10, sticky="w")
        
        F6_label=Label(F6,text="Rims",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=8,column=5,padx=0,pady=3, sticky="w")
        F6_txt=Entry(F6,width=5,bd=0,textvariable=self.rims,font=("times new roman",15)).grid(row=8,column=6,padx=40,pady=10, sticky="w")

        #for regular parts

        F4=Frame(self.root,bd=10,bg="#FFD39B")
        F4.place(x=865,y=590,width=480,height=100)

        title=Label(F4,text="Regular Parts",bd=8,bg="#FFD39B",fg="black",font=("Myraid pro",12,"bold")).grid(row=0,columnspan=2,padx=0,pady=2)

        lubtype_label=Label(F4,text="Lubricant",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=1,column=0,padx=0,pady=20, sticky="w")
        lubtype_txt=Entry(F4,width=8,bd=0,textvariable=self.lub,font=("times new roman",15)).grid(row=1,column=1,padx=40,pady=10, sticky="w")
        
        servicing_label=Label(F4,text="Servicing Charge",bg="#FFD39B",fg="black",font=("Myraid pro",10,"bold")).grid(row=1,column=5,padx=0,pady=20, sticky="w")
        servicing_txt=Entry(F4,width=7,bd=0,textvariable=self.servicing,font=("times new roman",15)).grid(row=1,column=6,padx=40,pady=10, sticky="w")
        
        #for total bill frame

        F5=Frame(self.root,bd=10,bg="#40D0E0")
        F5.place(x=4,y=590,width=372,height=100)

        totalip_label=Label(F5,text="Total Interior Parts",bg="#40D0E0",fg="black",font=("Myraid pro",12,"bold")).grid(row=1,column=0,padx=20,pady=1, sticky="w")
        totalip_txt=Entry(F5,width=12,bd=0,textvariable=self.interior_parts,font=("times new roman",15)).grid(row=1,column=1,padx=10,pady=1)
        
        totalep_label=Label(F5,text="Total Exterior Parts",bg="#40D0E0",fg="black",font=("Myraid pro",12,"bold")).grid(row=2,column=0,padx=20,pady=1, sticky="w")
        totalep_txt=Entry(F5,width=12,bd=0,textvariable=self.exterior_parts,font=("times new roman",15)).grid(row=2,column=1,padx=10,pady=1)

        totalrp_label=Label(F5,text="Total Regular Parts",bg="#40D0E0",fg="black",font=("Myraid pro",12,"bold")).grid(row=3,column=0,padx=20,pady=1, sticky="w")
        totalrp_txt=Entry(F5,width=12,bd=0,textvariable=self.regular_parts,font=("times new roman",15)).grid(row=3,column=1,padx=10,pady=1)

        # for button
        F7=Frame(self.root,bd=10,bg="#66CDAA")
        F7.place(x=380,y=590,width=480,height=100)

        #gtotal_label=Label(F7,text="Grand Total",bg="#66CDAA", fg="black", font=("Myraid pro",12,"bold")).grid(row=0,column=2,padx=3,pady=3)
        #gtotal_txt=Entry(F7,width=12,bd=0,textvariable=self.gtotal,font=("times new roman",15)).grid(row=0,column=3,padx=3,pady=3)

        total_bill=Button(F7,command=self.total,text="Grand Total",cursor="hand2",bd=5,bg="#FFD700",width=11,font=("arial 10 bold")).grid(row=0,column=1,padx=3,pady=3)
        cal_bill=Button(F7,command=self.payment_section,text="Show Receipt",cursor="hand2",bg="#FFD700",bd=5,width=11,font=("Myraid",10,"bold")).grid(row=0,column=2,padx=3,pady=3)
        clear_bill=Button(F7,command=self.clear,text="Clear",cursor="hand2",bg="#FFD700",bd=5,width=11,font=("Myraid",10,"bold")).grid(row=0,column=3,padx=3,pady=3)
        #del_bill=Button(F7,command=self.dele,text="Delete Data",cursor="hand2",bg="light blue",bd=5,width=11,font=("Myraid",10,"bold")).grid(row=2,column=1,padx=3,pady=3)
        save_data=Button(F7,command=self.save_data,text="Create Data",cursor="hand2",bg="light blue",bd=5,width=11,font=("Myraid",10,"bold")).grid(row=2,column=2,padx=3,pady=3)
        exit_bill=Button(F7,command=self.log,text="logout",cursor="hand2",bg="#FFD700",bd=5,width=11,font=("Myraid",10,"bold")).grid(row=0,column=4,padx=3,pady=3)
        #update_data=Button(F7,command=self.update,text="Update Data",cursor="hand2",bg="light blue",bd=5,width=11,font=("Myraid",10,"bold")).grid(row=2,column=4,padx=3,pady=3)
        cdata_bill=Button(F7,text="Customer Data",cursor="hand2",bg="light blue",command=self.read,bd=5,width=11,font=("Myraid",10,"bold")).grid(row=2,column=3,padx=3,pady=3)
        self.welcome_payment()
        

    def total(self):
        
        self.i_af=self.air_filter.get()*750
        self.i_ll=self.led_light.get()*250
        self.i_sp=self.spark_plug.get()*590
        self.i_cs=self.chain_spocket.get()*1590
        self.i_cb=self.cone_bearing.get()*4000
        self.i_bc=self.brake_cable.get()*500
        self.i_b=self.battery.get()*3500
        self.i_tw=self.throttle_wire.get()*200
        self.i_c=self.circuit.get()*600
        self.i_lf=self.lub_filter.get()*230
        self.i_dp=self.disk_pad.get()*550
        self.i_ss=self.starter_switch.get()*890
        self.i_tm=self.tachometer.get()*1860
        self.i_t=self.transmission.get()*2500
        self.i_s=self.piston.get()*12570
        self.i_ch=self.choke.get()*200
    
        self.total_interior_parts=float(
             self.i_af+
             self.i_ll+
             self.i_sp+
             self.i_cs+
             self.i_cb+
             self.i_bc+
             self.i_b+
             self.i_tw+
             self.i_c+
             self.i_lf+
             self.i_dp+
             self.i_ss+
             self.i_tm+
             self.i_t+
             self.i_s+
             self.i_ch
             )
        self.interior_parts.set("Rs. "+str(self.total_interior_parts))
        #self.idi=round((self.total_interior_parts*0.4),2)
        #self.idis.set(""+str(self.idi))

        
        self.e_cl=self.clutch_lever.get()*490
        self.e_gs=self.gear_shifter.get()*1320
        self.e_hg=self.horn.get()*700
        self.e_p=self.pegs.get()*300
        self.e_sl=self.signal_light.get()*2100
        self.e_hl=self.headlight.get()*7000
        self.e_m=self.mirror.get()*200
        self.e_ft=self.fuel_tank.get()*4500
        self.e_t=self.tire.get()*6100
        self.e_rs=self.rear_suspension.get()*3000
        self.e_ep=self.exhaust_pipe.get()*5800
        self.e_st=self.seat.get()*2300
        self.e_db=self.dashboard.get()*2500
        self.e_ks=self.kickstand.get()*370
        self.e_rm=self.rims.get()*3500
        self.e_eg=self.engine_guard.get()*2200

        self.total_exterior_parts=float(
             self.e_cl+
             self.e_gs+
             self.e_hg+
             self.e_p+
             self.e_sl+
             self.e_hl+
             self.e_m+
             self.e_ft+
             self.e_t+
             self.e_rs+
             self.e_ep+
             self.e_st+
             self.e_db+
             self.e_ks+
             self.e_rm+
             self.e_eg
             )
            
        self.exterior_parts.set("Rs. "+str(self.total_exterior_parts))
        #self.edi.round((self.total_exterior_parts*0.4),2)
        #self.edis.set(""+str(self.edi))

        
        self.r_l=self.lub.get()*1280
        self.r_s=self.servicing.get()*1
        
        self.total_regular_parts=float(
             self.r_l+
             self.r_s
        )

        self.regular_parts.set("Rs. "+str(self.total_regular_parts))
       # self.rdi=round((self.total_regular_parts*0.4),2)
        #self.rdis.set(""+str(self.rdi))

        #this is to show grand total in F7 frame in button section

        #to show total price,discount,grand total in database

        self.gtotal.set("Rs. "+str(self.total_interior_parts+self.total_exterior_parts+self.total_regular_parts))
        #self.tdiscount=float(self.rdi+self.idi+self.edi)
       #self.tdiscount=round((self.total_interior_parts+self.total_exterior_parts+self.total_regular_parts*0.12),2)
        #self.tdiscount.set("Rs. "+str(self.total_interior_parts+self.total_exterior_parts+self.total_regular_parts*0.12))
        #self.final_total.set("Rs. "+str(self.grand_total-self.discount))

        #===========================================================================

        #variable for grand total to show in the payment section

        self.grand_total=float(self.total_interior_parts+self.total_exterior_parts+self.total_regular_parts)
        
        #self.discount=round((self.grand_total*0.12),2)
        
        #self.final_total=float(self.grand_total-self.discount)

        #==========================================#
    

    def welcome_payment(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t  TWO WHEELER BILLING SYSTEM")
        self.txtarea.insert(END,f"\n ----------------------------------------")
        #for date and time
        now = datetime.datetime.now()
        timeStr = now.strftime("%H:%M:%S")
        dateStr = now.strftime("%Y-%m-%d")
        #===========================================#
        self.txtarea.insert(END,f"\n Time: {timeStr}")
        self.txtarea.insert(END,f"\n Date: {dateStr}")
        self.txtarea.insert(END,f"\n CUSTOMER NAME: {self.cname.get()}")
        self.txtarea.insert(END,f"\n CUSTOMER PHONE NO: {self.cphone.get()}")
        self.txtarea.insert(END,f"\n CUSTOMER Bike NO: {self.cbikeno.get()}")
        self.txtarea.insert(END,f"\n CUSTOMER SERVICE BILL NO: {self.cbillno.get()}")
        self.txtarea.insert(END,f"\n ----------------------------------------")
        self.txtarea.insert(END,f"\n Parts\t\t Quantity\t\t Price")
        self.txtarea.insert(END,f"\n ----------------------------------------")

    def payment_section(self):
        if self.cname.get()=="" or self.cphone.get()=="" or self.cbikeno.get()=="":
            messagebox.showerror("Error","Customer Information are empty")
        elif self.interior_parts.get()=="Rs. 0.0" and self.exterior_parts.get()=="Rs. 0.0" and self.regular_parts.get()=="Rs. 0.0":
            messagebox.showerror("Error","All Parts are Empty")
        else:
            self.welcome_payment()
        
        #for interior parts payment section

        if self.air_filter.get()!=0:
            #messagebox.showerror("Error","Air filter Not Available")
            self.txtarea.insert(END,f"\n Air Filter\t\t {self.air_filter.get()}\t\t{self.i_af}")
        if self.led_light.get()!=0:
            self.txtarea.insert(END,f"\n Led Headlight\t\t {self.led_light.get()}\t\t{self.i_ll}")
        if self.spark_plug.get()!=0:
            self.txtarea.insert(END,f"\n Spark Plug\t\t {self.spark_plug.get()}\t\t{self.i_sp}")
        if self.chain_spocket.get()!=0:
            self.txtarea.insert(END,f"\n Chain Spocket\t\t {self.chain_spocket.get()}\t\t{self.i_cs}")
        if self.cone_bearing.get()!=0:
            self.txtarea.insert(END,f"\n Cone Bearing\t\t {self.cone_bearing.get()}\t\t{self.i_cb}")
        if self.brake_cable.get()!=0:
            self.txtarea.insert(END,f"\n Brake Cable\t\t {self.brake_cable.get()}\t\t{self.i_bc}")
        if self.battery.get()!=0:
            self.txtarea.insert(END,f"\n Battery\t\t {self.battery.get()}\t\t{self.i_b}")
        if self.throttle_wire.get()!=0:
            self.txtarea.insert(END,f"\n Throttle Wire\t\t {self.throttle_wire.get()}\t\t{self.i_tw}")
        if self.circuit.get()!=0:
            self.txtarea.insert(END,f"\n Circuit\t\t {self.circuit.get()}\t\t{self.i_c}")
        if self.lub_filter.get()!=0:
            self.txtarea.insert(END,f"\n Lubricant Filter\t\t {self.lub_filter.get()}\t\t{self.i_lf}")
        if self.disk_pad.get()!=0:
            self.txtarea.insert(END,f"\n Disk Pad\t\t {self.disk_pad.get()}\t\t{self.i_dp}")
        if self.starter_switch.get()!=0:
            self.txtarea.insert(END,f"\n Starter Switch\t\t {self.starter_switch.get()}\t\t{self.i_ss}")
        if self.choke.get()!=0:
            self.txtarea.insert(END,f"\n Choke\t\t {self.choke.get()}\t\t{self.i_ch}")
        if self.tachometer.get()!=0:
            self.txtarea.insert(END,f"\n Tachometer\t\t {self.tachometer.get()}\t\t{self.i_tm}")
        if self.transmission.get()!=0:
            self.txtarea.insert(END,f"\n Transmission\t\t {self.transmission.get()}\t\t{self.i_t}")
        if self.piston.get()!=0:
            self.txtarea.insert(END,f"\n Piston\t\t {self.piston.get()}\t\t{self.i_s}")
        
        #for exterior part payment section

        if self.clutch_lever.get()!=0:
            self.txtarea.insert(END,f"\n Clutch Lever\t\t {self.clutch_lever.get()}\t\t{self.e_cl}")
        if self.gear_shifter.get()!=0:
            self.txtarea.insert(END,f"\n Gear Shifter\t\t {self.gear_shifter.get()}\t\t{self.e_gs}")
        if self.horn.get()!=0:
            self.txtarea.insert(END,f"\n Horn\t\t {self.horn.get()}\t\t{self.e_hg}")
        if self.pegs.get()!=0:
            self.txtarea.insert(END,f"\n Pegs\t\t {self.pegs.get()}\t\t{self.e_p}")
        if self.engine_guard.get()!=0:
            self.txtarea.insert(END,f"\n Engine Guard\t\t {self.engine_guard.get()}\t\t{self.e_eg}")
        if self.signal_light.get()!=0:
            self.txtarea.insert(END,f"\n Signal Lights\t\t {self.signal_light.get()}\t\t{self.e_sl}")
        if self.headlight.get()!=0:
            self.txtarea.insert(END,f"\n Headlights\t\t {self.headlight.get()}\t\t{self.e_hl}")
        if self.mirror.get()!=0:
            self.txtarea.insert(END,f"\n Mirror\t\t {self.mirror.get()}\t\t{self.e_m}")
        if self.fuel_tank.get()!=0:
            self.txtarea.insert(END,f"\n Fuel Tank\t\t {self.fuel_tank.get()}\t\t{self.e_ft}")
        if self.tire.get()!=0:
            self.txtarea.insert(END,f"\n Tires\t\t {self.tire.get()}\t\t{self.e_t}")
        if self.rear_suspension.get()!=0:
            self.txtarea.insert(END,f"\n Rear Suspension\t\t {self.rear_suspension.get()}\t\t{self.e_rs}")
        if self.exhaust_pipe.get()!=0:
            self.txtarea.insert(END,f"\n Exhaust\t\t {self.exhaust_pipe.get()}\t\t{self.e_ep}")
        if self.seat.get()!=0:
            self.txtarea.insert(END,f"\n Seat\t\t {self.seat.get()}\t\t{self.e_st}")
        if self.dashboard.get()!=0:
            self.txtarea.insert(END,f"\n Dashboard\t\t {self.dashboard.get()}\t\t{self.e_db}")
        if self.kickstand.get()!=0:
            self.txtarea.insert(END,f"\n Kickstand\t\t {self.kickstand.get()}\t\t{self.e_ks}")
        if self.rims.get()!=0:
            self.txtarea.insert(END,f"\n Rims\t\t {self.rims.get()}\t\t{self.e_rm}")

        #for regular parts payment section

        if self.lub.get()!=0:
            self.txtarea.insert(END,f"\n Lubricant\t\t {self.lub.get()}\t\t{self.r_l}")
        if self.servicing.get()!=0:
            self.txtarea.insert(END,f"\n Service Charge\t\t {self.servicing.get()}\t\t{self.r_s}")
        
        #for total price to show in the payment section
        self.txtarea.insert(END,f"\n-----------------------------------------")
        self.txtarea.insert(END,f"\n Total Price: \t\t\t\t{self.grand_total}")
        #self.txtarea.insert(END,f"\n 12% Discount: \t\t\t\t{self.discount}")
        self.txtarea.insert(END,f"\n-----------------------------------------")
        #self.txtarea.insert(END,f"\n Grand Total: \t\t\t\t{self.final_total}")
        #self.txtarea.insert(END,f"\n-----------------------------------------")
        self.save_receipt()


    def clear(self):
        self.cname.set("")
        self.cphone.set("")
        self.cbillno.set("")
        self.cbikeno.set("")
        p=random.randint(1000,9999)
        self.cbillno.set(str(p))

        self.air_filter.set(0)
        self.led_light.set(0)
        self.spark_plug.set(0)
        self.chain_spocket.set(0)
        self.cone_bearing.set(0)
        self.brake_cable.set(0)
        self.battery.set(0)
        self.throttle_wire.set(0)
        self.circuit.set(0)
        self.lub_filter.set(0)
        self.disk_pad.set(0)
        self.starter_switch.set(0)
        self.choke.set(0)
        self.tachometer.set(0)
        self.transmission.set(0)
        self.piston.set(0)

        self.clutch_lever.set(0)
        self.gear_shifter.set(0)
        self.horn.set(0)
        self.pegs.set(0)
        self.engine_guard.set(0)
        self.signal_light.set(0)
        self.headlight.set(0)
        self.mirror.set(0)
        self.fuel_tank.set(0)
        self.tire.set(0)
        self.rear_suspension.set(0)
        self.exhaust_pipe.set(0)
        self.seat.set(0)
        self.dashboard.set(0)
        self.kickstand.set(0)
        self.rims.set(0)

        self.servicing.set(0)
        self.lub.set(0)

        self.interior_parts.set("")
        self.exterior_parts.set("")
        self.regular_parts.set("")
        self.gtotal.set("")
    
        
    def read(self):
        self.root.destroy()
        import crud
        
    #customer info validation and save data
    def save_receipt(self):
        ap=messagebox.askyesno("Save Receipt", "Do you want to save the receipt ?")
        if ap>0:
            self.payment_section=self.txtarea.get('1.0', END)
            f1=open("receipt/"+str(self.cbikeno.get())+".txt","w")
            f1.write(self.payment_section)
            f1.close()
            messagebox.showinfo("Payment Receipt Saved",f"Customer bike No: {self.cbikeno.get()} has been Saved...")
        #elif self.cphone.get()=="" or len(self.contact.get())!=10:
            #messagebox.showerror("Error","Please enter your phone no")
        else:
            return
        
    #for search button   
    def find_bill(self):
        present="no"
        for i in os.listdir("receipt/"):
            if i.split('.')[0]==self.cbikeno.get():
                f1=open(f"receipt/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present="yes"
        if present == "no":
            messagebox.showerror("Error","Invalid Customer Bike No")
        
    def log(self):
        rm=messagebox.askyesno("Logout","Do you want to logout?")
        if rm>0:
            self.root.destroy()
            import logi
        else:
            return
        
        
    #def update(self):
        #pr=messagebox.showinfo("UPDATE INFO","Update Customer Information")
        #self.root.destroy()
        #import update

    
    
    def save_data(self):
        #print(self.cname.get(), self.cphone.get(), self.cbillno.get(), self.interior_parts.get(), self.exterior_parts.get(), self.regular_parts.get(), self.grand_total.get())
        #try:
        if self.cname.get()=="" or self.cphone.get()=="" or self.cbikeno.get()=="":
            messagebox.showerror("Customer INFO Empty","Customer Detail are Mandatory")
        #elif self.cphone.get()=="" or len(self.contact.get())!=10:
            #messagebox.showerror("Error","Please enter your phone no")
        elif self.interior_parts.get()=="" or self.exterior_parts.get()=="" or self.regular_parts.get()=="":
            messagebox.showerror("ERROR","Servicing Parts Not Selected")
        else:
            con=pymysql.connect(host="localhost", user="root", password="", database="cservices")
            now = datetime.datetime.now()
            cur=con.cursor()
            ##more to see==========================================================================================
            cur.execute("insert into service (interior_price,exterior_price) values(%s,%s)",(self.interior_parts.get(),self.exterior_parts.get()))
            ##========================================#
            cur.execute("insert into tservices (c_name, c_phoneno, bike_no, bill_no, interior_price, exterior_price, regular_price, grand_total, datetime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                       (self.cname.get(),self.cphone.get(),self.cbikeno.get(),self.cbillno.get(),self.interior_parts.get(),self.exterior_parts.get(),self.regular_parts.get(),self.gtotal.get(),now)
                       )     
            con.commit()
            con.close()
            messagebox.showinfo("DONE", "Data has been Saved in Database")
            #except Exception as es:
            #messagebox.showerror("Error", f"Error due to: {str(es)}",parent=self.root)

    

       
        
root=Tk()
obj = Service_App(root)
root.mainloop()