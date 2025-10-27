#Instagram

from tkinter import *
import instadb as i
a=Tk()
a.title('instagram')
a.geometry('500x700')
a.configure(bg='white')

user=StringVar()
passw=StringVar()

def login():
    username=user.get()
    password=passw.get()
    if i.login(username,password):
        print('login successful')
    else:
        print('login unsuccessful')

def fb():
    mfb=Label(a,text='use username and password to login',fg='red',bg='white',font=('arial',15))
    mfb.grid(row=9,columnspan=2,pady=50)

def sv():
    msv=Label(a,text='saved info',fg='black',bg='white')
    msv.grid(row=6,columnspan=2,ipadx=10)

m=Label(a,text='English(india)',fg='grey',bg='white')
m.grid(row=0,columnspan=4,padx=200,pady=0)
mtit=Label(a,text='𝓘𝓝𝓢𝓣𝓐𝓖𝓡𝓐𝓜',fg='black',bg='white')
mtit.grid(row=1,columnspan=2,padx=200,pady=50)
mface=Button(text='🅵 continue with facebook',bg='blue',fg='white',command=fb)
mface.grid(row=2,columnspan=2,ipadx=150,ipady=10,padx=0,pady=20)

mor=Label(a,text='OR',fg='grey',bg='white')
mor.grid(row=3,columnspan=2,pady=10)
muser=Entry(fg='grey',bg='white',textvariable=user)
muser.grid(row=4,columnspan=2,ipadx=150,ipady=10,pady=10)

mpass=Entry(fg='grey',bg='white',textvariable=passw,show='*')
mpass.grid(row=5,columnspan=2,ipadx=150,ipady=10,pady=10)

msave=Checkbutton(bg='white',command=sv)
msave.grid(row=6,columnspan=1)

msave1=Label(a,text='save login info',bg='white',fg='black')
msave1.grid(row=6,columnspan=2)

mlogin=Button(a,text='Log In',bg='blue',fg='white',command=login)
mlogin.grid(row=7,columnspan=2,ipadx=200,ipady=10,pady=20)

mfor=Label(a,text='Forget Password?',bg='white',fg='blue')
mfor.grid(row=8,columnspan=2)

msign=Label(a,text='''Don't have an account?''',fg='grey',bg='white')
msign.grid(row=10,columnspan=1,padx=10,pady=90)

msign=Label(a,text='Sign Up',fg='black',bg='white')
msign.grid(row=10,columnspan=2,padx=0,pady=90)


a.mainloop()
