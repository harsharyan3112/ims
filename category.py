from tkinter import *
from tkinter import font
from PIL  import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class CategoryClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x900+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()
        #=====VARIABLES=====
        self.var_CatID=StringVar()
        self.var_Name=StringVar()
        self.var_Search=StringVar()
    #==================TITLE=============
        lbl_title=Label(self.root,text="Manage Product Category",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=2)

        lbl_title=Label(self.root,text="Search Category Name",font=("goudy old style",30),bg="white").place(x=50,y=100)
        txt_search=Entry(self.root,textvariable=self.var_Search,font=("goudy old style",18),bg="light yellow").place(x=50,y=170,width=300)
        btn_search=Button(self.root,text="SEARCH",font=("goudy old style",15),bg="Blue",fg="white",cursor="hand2").place(x=360,y=170,width=150,height=30)
  
        lbl_title=Label(self.root,text="Enter Category Name",font=("goudy old style",30),bg="white").place(x=850,y=100)
        txt_name=Entry(self.root,textvariable=self.var_Name,font=("goudy old style",18),bg="light yellow").place(x=850,y=170,width=300)
        btn_add=Button(self.root,text="ADD",command=self.add,font=("goudy old style",15),bg="Green",fg="white",cursor="hand2").place(x=1160,y=170,width=150,height=30)
        btn_delete=Button(self.root,text="DELETE",command=self.delete, font=("goudy old style",15),bg="Red",fg="white",cursor="hand2").place(x=1320,y=170,width=150,height=30)
    
    #====================CATEGORY DETAILS===========================

        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=505,y=320,width=580,height=350)

        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)

        self.CategoryTable=ttk.Treeview(cat_frame,columns=("CId","Name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CategoryTable.xview)
        scrolly.config(command=self.CategoryTable.yview)

        self.CategoryTable.heading("CId",text="C.ID")
        self.CategoryTable.heading("Name",text="NAME")
        self.CategoryTable["show"]="headings"
        self.CategoryTable.column("CId",width=25)
        self.CategoryTable.column("Name",width=200)
        self.CategoryTable.pack(fill=BOTH,expand=1)
        self.CategoryTable.bind("<ButtonRelease-1>",self.getData)
        
        self.show()

#==========FUNCTIONS=============

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor() 
        try:
            if self.var_Name.get()=="":
                messagebox.showerror("Error","Category Name is required",parent=self.root)
            else:
                cur.execute("Select * from Category where Name=?",(self.var_Name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already present,try different name",parent=self.root)
                else:
                    cur.execute("Insert into Category (Name) values(?)",(self.var_Name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category added successfully!",parent=self.root)
        except Exception  as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
        self.show()

    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from Category")
            rows=cur.fetchall()
            self.CategoryTable.delete(*self.CategoryTable.get_children())
            for row in rows:
                self.CategoryTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Errot due to : {str(ex)}",parent=self.root)

    def getData(self,ev):
        f=self.CategoryTable.focus() 
        content=(self.CategoryTable.item(f))
        row=content['Values']
        self.var_CatID.set(row[0])
        self.var_Name.set(row[1])
    
    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_CatID.get()=="":
                messagebox.showerror("Error","Please select category from the list",parent=self.root)
            else:
                cur.execute("Select * from Category where Cid=?",(self.var_CatID.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Please try again",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from Category where CId=?",(self.var_CatID.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Category Deleted Successfully",parent=self.root)
                        self.show()
                        self.var_CatID.set("")
                        self.var_Name.set("")
        except Exception as ex:
           messagebox.showerror("Error",f"Error due to  : {str(ex)}",parent=self.root)


         



if __name__=="__main__":
    root=Tk()
    obj=CategoryClass(root)
    root.mainloop()