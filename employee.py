from tkinter import*
from tkinter import font
from typing import Sized
from PIL import Image,ImageTk
from tkinter import ttk
import sqlite3
from tkinter import ttk,messagebox
class emoloyeeClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("900x550+500+230")
        self.root.title("Inventry Management System ")
        self.root.focus_force()
        self.root.config(bg="#b0c4de")
        #----------------------------------------------

        # Variables

        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
        self.var_emp_id=StringVar()
        self.var_name=StringVar()
        self.var_email=StringVar()
        self.var_contact=StringVar()
        self.var_gender=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()

        #--------------------------------searcframe----------------------------------------

        searchFrame=LabelFrame(self.root,text="search user",font=("gowdy old style",12,"bold"),bd=5,relief=RIDGE,bg="white")
        searchFrame.place(x=150,y=20,width=600,height=70)

        #------------------------------options--------------------------------------------------

        cmb_search=ttk.Combobox(searchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=10,y=2,width=140)
        cmb_search.current(0)

        txt_search=Entry(searchFrame,textvariable=self.var_searchtxt, font=("goudy old style",15),bg="lightyellow")
        txt_search.place(x=160,y=2 )
        btn_search=Button(searchFrame,text="Search",command=self.search,font=("goudy old style",15),bg="#008000",fg="white",cursor="hand2")
        btn_search.place(x=430,y=2,width=150,height=30)

        #----------------------------------title------------------------------------------------
        title=Label(self.root,text="User Details",font=("goudy old style",15),bg="#000080",fg="white")
        title.place(x=50,y=100,width=800)

        #---------------------------------content-----------------------------------------------

        #---------------------------r1--------------------------------
        lbl_empid=Label(self.root,text="User Id",font=("goudy old style",15),bg="#b0c4de")
        lbl_empid.place(x=50,y=150)
        lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="#b0c4de")
        lbl_gender.place(x=450,y=150)

        txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="lightyellow")
        txt_empid.place(x=150,y=150,width=280)
        txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white")
        txt_gender.place(x=600,y=150,width=245)
        cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Other"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_gender.place(x=550,y=150,width=295)
        cmb_gender.current(0)
       
        #------------------------------r2--------------------------------------
        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="#b0c4de")
        lbl_name.place(x=50,y=200)
        lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="#b0c4de")
        lbl_contact.place(x=450,y=200)
        

        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow")
        txt_name.place(x=150,y=200,width=280)
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow")
        txt_contact.place(x=550,y=200,width=295)
        #--------------------------------r3------------------------------------------
        lbl_email=Label(self.root,text="Email",font=("goudy old style",15),bg="#b0c4de")
        lbl_email.place(x=50,y=250)
        lbl_pass=Label(self.root,text="Password",font=("goudy old style",15),bg="#b0c4de")
        lbl_pass.place(x=450,y=250)
        

        txt_email=Entry(self.root,textvariable=self.var_email,font=("goudy old style",15),bg="lightyellow")
        txt_email.place(x=150,y=250,width=280)
        txt_pass=Entry(self.root,textvariable=self.var_pass,font=("goudy old style",15),bg="lightyellow")
        txt_pass.place(x=550,y=250,width=295)
        #-------------------------------r4-------------------------------------------
        lbl_utype=Label(self.root,text="User Type",font=("goudy old style",15),bg="#b0c4de")
        lbl_utype.place(x=50,y=300)

        txt_utype=Entry(self.root,textvariable=self.var_utype,font=("goudy old style",15),bg="lightyellow")
        txt_utype.place(x=170,y=300,width=150)
        cmb_utype=ttk.Combobox(self.root,textvariable=self.var_utype,values=("Admin","User"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_utype.place(x=170,y=300,width=150)
        cmb_utype.current(0)

        #-----------------------------------btn--------------------------------
        btn_add=Button(self.root,text="Save",command=self.add,font=("goudy old style",15),bg="#0000ff",fg="white",cursor="hand2")
        btn_add.place(x=350,y=300,width=120,height=30)
        btn_update=Button(self.root,text="Update",command=self.update,font=("goudy old style",15),bg="#228b22",fg="white",cursor="hand2")
        btn_update.place(x=480,y=300,width=120,height=30)
        btn_delete=Button(self.root,text="Delete",command=self.delete,font=("goudy old style",15),bg="#b22222",fg="white",cursor="hand2")
        btn_delete.place(x=610,y=300,width=120,height=30)
        btn_clear=Button(self.root,text="clear",command=self.clear,font=("goudy old style",15),bg="#696969",fg="white",cursor="hand2")
        btn_clear.place(x=740,y=300,width=120,height=30)


        #---------------------------details--------------------------------------------

        emp_frame=Frame(self.root,bd=2,relief=RIDGE)
        emp_frame.place(x=0,y=350,relwidth=1,height=195)
        
        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.EmplyeeTable=ttk.Treeview(emp_frame,columns=("eid","name","email","gender","contact","pass","utype"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.EmplyeeTable.xview)
        scrolly.config(command=self.EmplyeeTable.yview)
        self.EmplyeeTable.heading("eid",text="User ID")
        self.EmplyeeTable.heading("name",text="Name")
        self.EmplyeeTable.heading("email",text="Email")
        self.EmplyeeTable.heading("gender",text="Gender")
        self.EmplyeeTable.heading("contact",text="Contact")
        self.EmplyeeTable.heading("pass",text="Password")
        self.EmplyeeTable.heading("utype",text="User Type")

        self.EmplyeeTable["show"]="headings"

        self.EmplyeeTable.column("eid",width=100)
        self.EmplyeeTable.column("name",width=100)
        self.EmplyeeTable.column("email",width=200)
        self.EmplyeeTable.column("gender",width=100)
        self.EmplyeeTable.column("contact",width=120)
        self.EmplyeeTable.column("pass",width=120)
        self.EmplyeeTable.column("utype",width=180)
        
        
        
        self.EmplyeeTable.pack(fill=BOTH,expand=1)
        self.EmplyeeTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#-----------------------------------------------------------------

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","User Id must be registered",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This User ID is alredy assigned, try different",parent=self.root)
                else:
                    cur.execute("Insert into employee (eid,name,email,gender,contact,pass,utype) values(?,?,?,?,?,?,?)",(
                                        self.var_emp_id.get(),
                                        self.var_name.get(),  
                                        self.var_email.get(),  
                                        self.var_gender.get(),  
                                        self.var_contact.get(),  
                                        self.var_pass.get(),  
                                        self.var_utype.get()      
                    ))
                    con.commit()
                    messagebox.showinfo("Success","User Added Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to  : {str(ex)}",parent=self.root)


    def show(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from employee")
            rows=cur.fetchall()
            self.EmplyeeTable.delete(*self.EmplyeeTable.get_children())
            for row in rows:
                self.EmplyeeTable.insert('',END,values=row)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to  : {str(ex)}",parent=self.root)

    def get_data(self,ev):
        f=self.EmplyeeTable.focus()
        content=(self.EmplyeeTable.item(f))
        row=content['values']
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])  
        self.var_email.set(row[2])  
        self.var_gender.set(row[3])  
        self.var_contact.set(row[4])  
        self.var_pass.set(row[5])  
        self.var_utype.set(row[6])

    def update(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","User Id must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid User ID",parent=self.root)
                else:
                    cur.execute("Update employee set name=?,email=?,gender=?,contact=?,pass=?,utype=? where eid=?",(
                                        self.var_name.get(),  
                                        self.var_email.get(),  
                                        self.var_gender.get(),  
                                        self.var_contact.get(),  
                                        self.var_pass.get(),  
                                        self.var_utype.get(),
                                        self.var_emp_id.get()     
                    ))
                    con.commit()
                    messagebox.showinfo("Success","User Updated Successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to  : {str(ex)}",parent=self.root)

    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_emp_id.get()=="":
                messagebox.showerror("Error","User Id must be required",parent=self.root)
            else:
                cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid User ID",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:

                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","User Deleted Successfully")
                        self.clear()


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to  : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_emp_id.set("")
        self.var_name.set("")  
        self.var_email.set("") 
        self.var_gender.set("Select")  
        self.var_contact.set("")  
        self.var_pass.set("")  
        self.var_utype.set("Admin")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()


    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By Option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should be required",parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:   
                    self.EmplyeeTable.delete(*self.EmplyeeTable.get_children())
                    for row in rows:
                        self.EmplyeeTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!!",parent=self.root)


        except Exception as ex:
            messagebox.showerror("Error",f"Error due to  : {str(ex)}",parent=self.root)





if __name__=="__main__":   
    root=Tk()
    obj=emoloyeeClass(root)
    root.mainloop()
