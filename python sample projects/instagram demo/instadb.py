<<<<<<< HEAD
from mysql.connector import *
def open():
    global cursor
    global conn
    conn=connect(host='localhost',db='insta',user='root',password='Mayil@#$1709')
    cursor=conn.cursor()

def login(username,password):
    open()
    query=f"select * from ins where username='{username}' and password='{password}'"
    print(query)
    cursor.execute(query)
    fin=cursor.fetchall()
    if len(fin):
        return True
    else:
        return False

    close()

def close():
    conn.commit()
    conn.close()
    cursor.close()
    
=======
from mysql.connector import *
def open():
    global cursor
    global conn
    conn=connect(host='localhost',db='insta',user='root',password='Mayil@#$1709')
    cursor=conn.cursor()

def login(username,password):
    open()
    query=f"select * from ins where username='{username}' and password='{password}'"
    print(query)
    cursor.execute(query)
    fin=cursor.fetchall()
    if len(fin):
        return True
    else:
        return False

    close()

def close():
    conn.commit()
    conn.close()
    cursor.close()
    
>>>>>>> 4a81e46a277a6aedb437f8b7d27d3c9be43210fa
