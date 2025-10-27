<<<<<<< HEAD
#calculator:

from tkinter import *
r=Tk()
r.geometry('600x400')

value1=IntVar()
value2=IntVar()

def addition():
    v1=value1.get()
    v2=value2.get()
    res=v1+v2
    print(res)

def subtraction():
    v1=value1.get()
    v2=value2.get()
    res=v1-v2
    print(res)

def multi():
    v1=value1.get()
    v2=value2.get()
    res=v1*v2
    print(res)

def div():
    v1=value1.get()
    v2=value2.get()
    res=v1/v2
    print(res)


r.title('mycalci')
lab=Label(r,text='my calculator',fg='black',bg='red',font=('impact',30))
lab.place(x=200,y=10)

num1=Label(r,text='number 1',bg='white',fg='black')
num1.place(x=100,y=100)

n1=Entry(r,textvariable=value1)
n1.place(x=200,y=100)

num2=Label(r,text='number 2',bg='white',fg='black')
num2.place(x=100,y=150)

n2=Entry(r,textvariable=value2)
n2.place(x=200,y=150)

add=Button(r,text='ADD',bg='blue',fg='white',font=('arial',20),command=addition)
add.place(x=100,y=200)

sub=Button(r,text='SUB',fg='white',bg='blue',font=('arial',20),command=subtraction)
sub.place(x=190,y=200)

mul=Button(r,text='MUL',fg='white',bg='blue',font=('arial',20),command=multi)
mul.place(x=290,y=200)

mul=Button(r,text='DIV',fg='white',bg='blue',font=('arial',20),command=div)
mul.place(x=390,y=200)

r.mainloop()
=======
#calculator:

from tkinter import *
r=Tk()
r.geometry('600x400')

value1=IntVar()
value2=IntVar()

def addition():
    v1=value1.get()
    v2=value2.get()
    res=v1+v2
    print(res)

def subtraction():
    v1=value1.get()
    v2=value2.get()
    res=v1-v2
    print(res)

def multi():
    v1=value1.get()
    v2=value2.get()
    res=v1*v2
    print(res)

def div():
    v1=value1.get()
    v2=value2.get()
    res=v1/v2
    print(res)


r.title('mycalci')
lab=Label(r,text='my calculator',fg='black',bg='red',font=('impact',30))
lab.place(x=200,y=10)

num1=Label(r,text='number 1',bg='white',fg='black')
num1.place(x=100,y=100)

n1=Entry(r,textvariable=value1)
n1.place(x=200,y=100)

num2=Label(r,text='number 2',bg='white',fg='black')
num2.place(x=100,y=150)

n2=Entry(r,textvariable=value2)
n2.place(x=200,y=150)

add=Button(r,text='ADD',bg='blue',fg='white',font=('arial',20),command=addition)
add.place(x=100,y=200)

sub=Button(r,text='SUB',fg='white',bg='blue',font=('arial',20),command=subtraction)
sub.place(x=190,y=200)

mul=Button(r,text='MUL',fg='white',bg='blue',font=('arial',20),command=multi)
mul.place(x=290,y=200)

mul=Button(r,text='DIV',fg='white',bg='blue',font=('arial',20),command=div)
mul.place(x=390,y=200)

r.mainloop()
>>>>>>> 4a81e46a277a6aedb437f8b7d27d3c9be43210fa
