import sqlite3
def create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTs employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,pass text,utype text)")
    con.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS category(CId INTEGER PRIMARY KEY AUTOINCREMENT,Name text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS bill(PId INTEGER PRIMARY KEY AUTOINCREMENT,Name text,Price text,Qty text, Status text)")
    con.commit()

create_db()
