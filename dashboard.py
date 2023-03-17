import os
from tkinter import*
from typing import Sized
from PIL import Image,ImageTk
from employee import emoloyeeClass
from category import CategoryClass
from bill import BillClass
import sqlite3
from tkinter import messagebox
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1900x980+0+0")
        self.root.title("Inventry Management System ")
        self.root.config(bg="#ffe4c4")

        #--------------------------------------------------------title----------------------------------------------------------------------

        self.icon_title=PhotoImage(file="images/logo1.png")

        title=Label(self.root,text= "Inventry Managment System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c4d",fg="white",anchor="w",padx=30).place(x=0,y=0,relwidth=1,height=100)

        #-------------------------------------------------------Btn_logout-------------------------------------------------------------------

        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1700,y=25,width=150)   

        #----------------------------------------------------------welcome--------------------------------------------------------------------

        self.lbl_clock=Label(self.root,text= "Welcome, You are logged in as Admin ",font=("times new roman",20),bg="black",fg="white")
        self.lbl_clock.place(x=0,y=100,relwidth=1,height=50)

        #-------------------------------------------------------left menu-----------------------------------------------------------------
        self.MenuLogo=Image.open("images/pantry.png")
        self.MenuLogo=self.MenuLogo.resize((250,250),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        LeftMenu=Frame(self.root,bd=1,relief=RIDGE,bg="white")
        LeftMenu.place(x=0,y=150,width=250,height=750)

        lbl_menuLogo=Label(LeftMenu,bg="#c0c0c0" ,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)
        self.icon_menu=PhotoImage(file="images/menu (1).png")
        btn_menu1=Button(LeftMenu,text="Menu",padx=25 ,font=("times new roman",25),bd=2,bg="#808080",image=self.icon_menu,compound=LEFT,anchor="w")
        btn_menu1.pack(side=TOP,fill=X)
        self.icon_send=PhotoImage(file="images/send-button (1).png")
        btn_menu=Button(LeftMenu,text="Users",padx=12,font=("times new roman",25),bd=3,bg="#fffff0",cursor="hand2",command=self.employee,image=self.icon_send,compound=LEFT,anchor="w")
        btn_menu.pack(side=TOP,fill=X)
        btn_menu=Button(LeftMenu,text="Billing",padx=12,font=("times new roman",25),bd=3,bg="#fffff0",cursor="hand2",command=self.bill,image=self.icon_send,compound=LEFT,anchor="w")
        btn_menu.pack(side=TOP,fill=X)
        btn_menu=Button(LeftMenu,text="Category",padx=12,font=("times new roman",25),bd=3,bg="#fffff0",cursor="hand2",command=self.category,image=self.icon_send,compound=LEFT,anchor="w")
        btn_menu.pack(side=TOP,fill=X)
        btn_menu=Button(LeftMenu,text="Products",padx=12,font=("times new roman",25),bd=3,bg="#fffff0",cursor="hand2",image=self.icon_send,compound=LEFT,anchor="w")
        btn_menu.pack(side=TOP,fill=X)
        btn_menu=Button(LeftMenu,text="Forget",padx=12,font=("times new roman",25),bd=3,bg="#fffff0",cursor="hand2",image=self.icon_send,compound=LEFT,anchor="w")
        btn_menu.pack(side=TOP,fill=X)

        #----------------------------------------------------------content-------------------------------------------------------------------

        self.bg_image=ImageTk.PhotoImage(file="images/menu_im.png")
        self.lbl_bg_image=Label(self.root,image=self.bg_image,bg="#ffe4c4",bd=0).place(x=1100,y=200)


        self.lbl_employee=Label(self.root,text="Users\n[0]",bd=5,relief=RIDGE ,bg="#008080",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=300,height=150,width=350)

        self.lbl_category=Label(self.root,text="Category\n[0]",bd=5,relief=RIDGE ,bg="#008080",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=700,y=300,height=150,width=350)

        self.lbl_product=Label(self.root,text="Product\n[0]",bd=5,relief=RIDGE ,bg="#008080",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=600,height=150,width=350)

        self.lbl_bill=Label(self.root,text="bills\n[0]",bd=5,relief=RIDGE ,bg="#008080",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_bill.place(x=700,y=600,height=150,width=350)



         #----------------------------------------------------------footer--------------------------------------------------------------------

        lbl_footer=Label(self.root,text= "Designed by Harsh Aryan and Rajat Kumar",font=("times new roman",20),bg="#220c1d",fg="white")
        lbl_footer.pack(side=BOTTOM,fill=X)

        self.update_content()
#--------------------------------------------------------------------------------------------------------------------------------------------
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=emoloyeeClass(self.new_win)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CategoryClass(self.new_win)

    def bill(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=BillClass(self.new_win)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")


    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            # cur.execute("select * from product")
            # procuct=cur.fetchall()
            # self.lbl_product.config(text=f'Total product\n[{str(len(product))} ]')

            # cur.execute("select * from supplier")
            # bill=cur.fetchall()
            # self.lbl_bill.config(text=f'Total Bills\n[{str(len(bill))} ]')

            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Category\n[{str(len(category))} ]')
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Users\n[{str(len(employee))} ]')

            

        except Exception as ex:
            print("")
            messagebox.showerror("Error",f"Error due to  : {str(ex)}",parent=self.root)




if __name__=="__main__":   
    root=Tk()
    obj=IMS(root)
    root.mainloop()
