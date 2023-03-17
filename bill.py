from tkinter import*
from tkinter import font
from PIL  import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class BillClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1500x800+200+150")
        self.root.title("Inventry Management System ")

        #--------------------------------------------------------title----------------------------------------------------------------------

        self.icon_title=PhotoImage(file="images/pantry (1).png")

        title=Label(self.root,text= "Inventry Managment System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c4d",fg="white",anchor="w",padx=30).place(x=0,y=0,relwidth=1,height=100)

        #-------------------------------------------------------Btn_logout-------------------------------------------------------------------

        btn_logout=Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1700,y=25,width=150)   

        #----------------------------------------------------------welcome--------------------------------------------------------------------

        self.lbl_clock=Label(self.root,text= "Welcome, You are in Billing Window ",font=("times new roman",20),bg="black",fg="white")
        self.lbl_clock.place(x=0,y=100,relwidth=1,height=50)
    

        #======Product Frame=======
        self.var_search=StringVar()
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        ProductFrame1.place(x=5,y=150,width=410,height=550)
        
        pTitle=Label(ProductFrame1,text="All Products",font=("Goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)

        ProductFrame2=Frame(ProductFrame1,bd=2,relief=RIDGE,bg="white")
        ProductFrame2.place(x=2,y=42,width=398,height=90)

        lbl_searchText=Label(ProductFrame2,text="Search the name of product",font=("times new roman",13,"bold"),bg="white",fg="green").place(x=2,y=5)

        lbl_nameText=Label(ProductFrame2,text="Product Name",font=("times new roman",12,"bold"),bg="white").place(x=5,y=45)
        text_search=Entry(ProductFrame2,textvariable=self.var_search,font=("times new roman",15),bg="light yellow").place(x=135,y=47,width=150,height=22) 
        btn_search=Button(ProductFrame2,text="Search",font=("Goudy Old Style",12),bg="#2196f3",fg="white",cursor="hand2").place(x=290,y=45,width=80,height=25)
        btn_showAll=Button(ProductFrame2,text="Show All",font=("Goudy Old Style",12),bg="#083531",fg="white",cursor="hand2").place(x=290,y=10,width=80,height=25)

#====================PRODUCT FRAME DETAILS===========================

        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE)
        ProductFrame3.place(x=2,y=140,width=398,height=385)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.ProductTable=ttk.Treeview(ProductFrame3,columns=("PId","Name","Price","Qty","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.ProductTable.xview)
        scrolly.config(command=self.ProductTable.yview)

        self.ProductTable.heading("PId",text="P.ID")
        self.ProductTable.heading("Name",text="NAME")
        self.ProductTable.heading("Price",text="PRICE")
        self.ProductTable.heading("Qty",text="Qty.")
        self.ProductTable.heading("Status",text="STATUS")
        self.ProductTable["show"]="headings"
        self.ProductTable.column("PId",width=90)
        self.ProductTable.column("Name",width=100)
        self.ProductTable.column("Price",width=100)
        self.ProductTable.column("Qty",width=100)
        self.ProductTable.column("Status",width=100)
        self.ProductTable.pack(fill=BOTH,expand=1)

        lbl_Note=Label(ProductFrame1,text="Note: Enter 0 Qty to remove the product from Cart",font=("Goudy Old Style",12),anchor='w',bg="White",fg="Red").pack(side=BOTTOM,fill=X)


        #======CUSTOMER FRAME===============
        self.var_NAME=StringVar()
        self.var_CONTACT=StringVar()
        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="light grey")
        CustomerFrame.place(x=420,y=150,width=630,height=70)

        cTitle=Label(CustomerFrame,text="Customer Details",font=("Goudy old style",20,"bold"),bg="light grey").pack(side=TOP,fill=X)
        lbl_NAME=Label(CustomerFrame,text="Customer Name",font=("times new roman",12),bg="light grey").place(x=5,y=35)
        text_NAME=Entry(CustomerFrame,textvariable=self.var_NAME,font=("times new roman",15),bg="light yellow").place(x=150,y=35,width=170,height=25) 

        lbl_CONTACT=Label(CustomerFrame,text="Contact No.",font=("times new roman",12),bg="light grey").place(x=350,y=35)
        text_CONTACT=Entry(CustomerFrame,textvariable=self.var_CONTACT,font=("times new roman",15),bg="light yellow").place(x=480,y=35,width=130,height=25) 

    #==========CART/CALCULATOR FRAME======
        CalCartFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        CalCartFrame.place(x=420,y=220,width=630,height=460)
    #==========CALCULATOR FRAME===========
        self.var_CalInput=StringVar()
        CalFrame=Frame(CalCartFrame,bd=9,relief=RIDGE,bg="white")
        CalFrame.place(x=5,y=10,width=368,height=360)

        txt_cal_input=Entry(CalFrame,textvariable=self.var_CalInput,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)

        btn7=Button(CalFrame,text='7',font=('Arial',15,'bold'),command=lambda:self.get_Input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn8=Button(CalFrame,text='8',font=('Arial',15,'bold'),command=lambda:self.get_Input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn9=Button(CalFrame,text='9',font=('Arial',15,'bold'),command=lambda:self.get_Input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btnSum=Button(CalFrame,text='+',font=('Arial',15,'bold'),command=lambda:self.get_Input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)

        btn4=Button(CalFrame,text='4',font=('Arial',15,'bold'),command=lambda:self.get_Input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn5=Button(CalFrame,text='5',font=('Arial',15,'bold'),command=lambda:self.get_Input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn6=Button(CalFrame,text='6',font=('Arial',15,'bold'),command=lambda:self.get_Input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btnDiff=Button(CalFrame,text='-',font=('Arial',15,'bold'),command=lambda:self.get_Input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)

        btn1=Button(CalFrame,text='1',font=('Arial',15,'bold'),command=lambda:self.get_Input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn2=Button(CalFrame,text='2',font=('Arial',15,'bold'),command=lambda:self.get_Input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn3=Button(CalFrame,text='3',font=('Arial',15,'bold'),command=lambda:self.get_Input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btnMul=Button(CalFrame,text='*',font=('Arial',15,'bold'),command=lambda:self.get_Input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
        
        btn0=Button(CalFrame,text='0',font=('Arial',15,'bold'),command=lambda:self.get_Input(0),bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=0)
        btnDel=Button(CalFrame,text='Del',font=('Arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=1)
        btnEq=Button(CalFrame,text='=',font=('Arial',15,'bold'),command=self.performCal,bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=2)
        btnDiv=Button(CalFrame,text='/',font=('Arial',15,'bold'),command=lambda:self.get_Input('/'),bd=5,width=4,pady=10,cursor="hand2").grid(row=4,column=3)


    #==========CART FRAME=================

        CartFrame=Frame(CalCartFrame,bd=3,relief=RIDGE)
        CartFrame.place(x=330,y=8,width=290,height=362)
        cartTitle=Label(CartFrame,text="   Cart   Total Products: [0]",font=("Goudy old style",15),bg="light grey").pack(side=TOP,fill=X)

        scrolly=Scrollbar(CartFrame,orient=VERTICAL)
        scrollx=Scrollbar(CartFrame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(CartFrame,columns=("PId","Name","Price","Qty","Status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)

        self.CartTable.heading("PId",text="P.ID")
        self.CartTable.heading("Name",text="NAME")
        self.CartTable.heading("Price",text="PRICE")
        self.CartTable.heading("Qty",text="Qty.")
        self.CartTable.heading("Status",text="STATUS")
        self.CartTable["show"]="headings"
        self.CartTable.column("PId",width=40)
        self.CartTable.column("Name",width=100)
        self.CartTable.column("Price",width=90)
        self.CartTable.column("Qty",width=40)
        self.CartTable.column("Status",width=90)
        self.CartTable.pack(fill=BOTH,expand=1)

#===============ADD CART WIDGETS========
        self.var_PId=StringVar()
        self.var_PName=StringVar()
        self.var_Price=StringVar()
        self.var_Qty=StringVar()
        self.var_stock=StringVar()

        AddCartFrame=Frame(self.root,bd=2,relief=RIDGE,bg="light grey")
        AddCartFrame.place(x=420,y=600,width=630,height=110)

        lbl_P_Name=Label(AddCartFrame,text='Product Name',font=("Times New Roman",15),bg="light grey").place(x=5,y=5)
        txt_P_Name=Entry(AddCartFrame,textvariable=self.var_PName,font=("Times New Roman",15),bg="light yellow",state='readonly').place(x=5,y=35,width=190,height=22)

        lbl_P_Price=Label(AddCartFrame,text='Price per Qty',font=("Times New Roman",15),bg="light grey").place(x=230,y=5)
        txt_P_Price=Entry(AddCartFrame,textvariable=self.var_PName,font=("Times New Roman",15),bg="light yellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_P_Qty=Label(AddCartFrame,text='Quantity',font=("Times New Roman",15),bg="light grey").place(x=390,y=5)
        txt_P_Qty=Entry(AddCartFrame,textvariable=self.var_PName,font=("Times New Roman",15),bg="light yellow").place(x=390,y=35,width=120,height=22)
        
        self.lbl_instock=Label(AddCartFrame,text='In Stock[999]',font=("Times New Roman",15),bg="light grey")
        self.lbl_instock.place(x=5,y=70)

        btn_ClearCart=Button(AddCartFrame,text="Clear",font=("Times New Roman",15,"bold"),bg="Lightgrey",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_AddCart=Button(AddCartFrame,text="Add",font=("Times New Roman",15,"bold"),bg="Orange",cursor="hand2").place(x=340,y=70,width=150,height=30) 
        
#==============BILLING AREA============

        BillFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        BillFrame.place(x=1053,y=150,width=410,height=410)

        bTitle=Label(BillFrame,text="Billing Area",font=("Goudy old style",20,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        scrolly=Scrollbar(BillFrame,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y)

        self.text_Bill_Area=Text(BillFrame,yscrollcommand=scrolly.set)
        self.text_Bill_Area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.text_Bill_Area.yview)

     #======Billing Buttons============
        BillMenuFrame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        BillMenuFrame.place(x=1053,y=520,width=410,height=140)

        self.lbl_Amt=Label(BillMenuFrame,bd=2,relief=RIDGE,text='Bill Amount\n[0]',font=("Goudy Old Style",15,"bold"),bg="#3f51b5",fg="White")
        self.lbl_Amt.place(x=2,y=5,width=120,height=70)

        self.lbl_Dis=Label(BillMenuFrame,bd=2,relief=RIDGE,text='Discount\n[5%]',font=("Goudy Old Style",15,"bold"),bg="#8bc34a",fg="White")
        self.lbl_Dis.place(x=124,y=5,width=120,height=70)

        self.lbl_NetPay=Label(BillMenuFrame,bd=2,relief=RIDGE,text='Net Pay\n[0]',font=("Goudy Old Style",15,"bold"),bg="#607d8b",fg="White")
        self.lbl_NetPay.place(x=248,y=5,width=150,height=70)

        btn_Print=Button(BillMenuFrame,text='Print Bill',pady=10,cursor='hand2',font=("Goudy Old Style",15,"bold"),bg="light green",fg="White")
        btn_Print.place(x=2,y=80,width=120,height=70)

        btn_clear_all=Button(BillMenuFrame,text='Clear All',pady=10,cursor='hand2',font=("Goudy Old Style",15,"bold"),bg="gray",fg="White")
        btn_clear_all.place(x=124,y=80,width=120,height=70)

        btn_Generate=Button(BillMenuFrame,text='Save Bill',pady=10, cursor='hand2',font=("Goudy Old Style",15,"bold"),bg="#009688",fg="White")
        btn_Generate.place(x=248,y=80,width=150,height=70)

#=========================FOOTER=============================
        Footer=Label(self.root,text="IMS-INVENTORY MANAGEMENT SYSTEM | Developed By Harsh & Rajat",font=("Times New Roman",20,"bold"),bg="#4d636d",fg="black",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)



    
#=================FUNCTIONS=====================

    def get_Input(self,num):
        xnum=self.var_CalInput.get()+str(num)
        self.var_CalInput.set(xnum)
    def clear_cal(self):
        self.var_CalInput.set('')
    
    def performCal(self):
        result=self.var_CalInput.get()
        self.var_CalInput.set(eval(result))
        
        
        
if __name__=="__main__":   
    root=Tk()
    obj=BillClass(root)
    root.mainloop()