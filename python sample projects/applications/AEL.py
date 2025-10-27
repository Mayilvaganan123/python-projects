<<<<<<< HEAD
#app
from tkinter import *
a=Tk()
a.geometry('800x800')
a.title('AEL app')
a.configure(bg='#5a639c')
value1=IntVar()

def arm():
    v1=value1.get()
    temp=v1
    sum=0
    while temp>0:
        n=temp%10
        sum=sum+n**3
        temp=temp//10
    if (v1==sum):
        marm2=Label(a,text='                                                                            ',bg='#5a639c',font=('Futura',30))
        marm2.place(x=250,y=575)
        marm1=Label(a,text='It is Armstrong Number',fg='#77e4c8',bg='#5a639c',font=('Futura',30))
        marm1.place(x=180,y=575)
    else:
        marm4=Label(a,text='                                                                            ',bg='#5a639c',font=('Futura',30))
        marm4.place(x=250,y=575)
        marm3=Label(a,text='It is Non Armstrong Number',fg='#77e4c8',bg='#5a639c',font=('Futura',30))
        marm3.place(x=180,y=575)

def EO():
    v2=value1.get()
    if(v2%2==0):
        meo3=Label(a,text='                                                                              ',bg='#5a639c',font=('Futura',30))
        meo3.place(x=250,y=575)
        meo1=Label(a,text='It is Even Number',fg='cyan',bg='#5a639c',font=('Futura',30))
        meo1.place(x=180,y=575)
    else:
        meo4=Label(a,text='                                                                               ',bg='#5a639c',font=('Futura',30))
        meo4.place(x=250,y=575)
        meo2=Label(a,text='It is Odd Number',fg='cyan',bg='#5a639c',font=('Futura',30))
        meo2.place(x=180,y=575)

def LY():
    v3=value1.get()
    if(v3%4==0):
        myl3=Label(a,text='                                                                                ',bg='#5a639c',font=('Futura',30))
        myl3.place(x=250,y=575)
        mly1=Label(a,text='It is Leap year',fg='white',bg='#5a639c',font=('Futura',30))
        mly1.place(x=180,y=575)
    else:
        myl4=Label(a,text='                                                                                ',bg='#5a639c',font=('Futura',30))
        myl4.place(x=250,y=575)
        mly2=Label(a,text='It is Non Leap year',fg='white',bg='#5a639c',font=('Futura',30))
        mly2.place(x=180,y=575)

m1=Label(a,text='Welcome to AEL',fg='red',bg='black')
m1.configure(font=('Myriad Pro',25))
m1.place(x=250,y=0)

mdes=Label(a,text='THIS APP IS USED TO CHECK THE NUMBER ',fg='white',bg='#180161',font=('arial',25))
mdes.place(x=35,y=70)
mdes2=Label(a,text='IS ARMSTRONG,EVEN OR ODD,LEAP YEAR ',fg='white',bg='#180161',font=('arial',25))
mdes2.place(x=35,y=110)
m2=Label(a,text='Enter the value',fg='white',bg='lime',font=('Myriad Pro',20))
m2.place(x=150,y=200)

m3=Entry(a,fg='lime',bg='white',font=('times new roman',20),textvariable=value1)
m3.place(x=350,y=200)

m4=Button(a,text='Armstrong',fg='#77e4c8',bg='#070f2b',font=('Futura',20),command=arm)
m4.place(x=300,y=300)

m5=Button(a,text='Even or Odd',fg='cyan',bg='#070f2b',font=('Futura',20),command=EO)
m5.place(x=300,y=400)

m6=Button(a,text='Leap year',fg='white',bg='#070f2b',font=('Futura',20),command=LY)
m6.place(x=300,y=500)

m7=Label(a,text='THANKS FOR USING ME :)',fg='white',bg='#5a639c',font=('Myriad Pro',30))
m7.place(x=150,y=650)

a.mainloop()
=======
#app
from tkinter import *
a=Tk()
a.geometry('800x800')
a.title('AEL app')
a.configure(bg='#5a639c')
value1=IntVar()

def arm():
    v1=value1.get()
    temp=v1
    sum=0
    while temp>0:
        n=temp%10
        sum=sum+n**3
        temp=temp//10
    if (v1==sum):
        marm2=Label(a,text='                                                                            ',bg='#5a639c',font=('Futura',30))
        marm2.place(x=250,y=575)
        marm1=Label(a,text='It is Armstrong Number',fg='#77e4c8',bg='#5a639c',font=('Futura',30))
        marm1.place(x=180,y=575)
    else:
        marm4=Label(a,text='                                                                            ',bg='#5a639c',font=('Futura',30))
        marm4.place(x=250,y=575)
        marm3=Label(a,text='It is Non Armstrong Number',fg='#77e4c8',bg='#5a639c',font=('Futura',30))
        marm3.place(x=180,y=575)

def EO():
    v2=value1.get()
    if(v2%2==0):
        meo3=Label(a,text='                                                                              ',bg='#5a639c',font=('Futura',30))
        meo3.place(x=250,y=575)
        meo1=Label(a,text='It is Even Number',fg='cyan',bg='#5a639c',font=('Futura',30))
        meo1.place(x=180,y=575)
    else:
        meo4=Label(a,text='                                                                               ',bg='#5a639c',font=('Futura',30))
        meo4.place(x=250,y=575)
        meo2=Label(a,text='It is Odd Number',fg='cyan',bg='#5a639c',font=('Futura',30))
        meo2.place(x=180,y=575)

def LY():
    v3=value1.get()
    if(v3%4==0):
        myl3=Label(a,text='                                                                                ',bg='#5a639c',font=('Futura',30))
        myl3.place(x=250,y=575)
        mly1=Label(a,text='It is Leap year',fg='white',bg='#5a639c',font=('Futura',30))
        mly1.place(x=180,y=575)
    else:
        myl4=Label(a,text='                                                                                ',bg='#5a639c',font=('Futura',30))
        myl4.place(x=250,y=575)
        mly2=Label(a,text='It is Non Leap year',fg='white',bg='#5a639c',font=('Futura',30))
        mly2.place(x=180,y=575)

m1=Label(a,text='Welcome to AEL',fg='red',bg='black')
m1.configure(font=('Myriad Pro',25))
m1.place(x=250,y=0)

mdes=Label(a,text='THIS APP IS USED TO CHECK THE NUMBER ',fg='white',bg='#180161',font=('arial',25))
mdes.place(x=35,y=70)
mdes2=Label(a,text='IS ARMSTRONG,EVEN OR ODD,LEAP YEAR ',fg='white',bg='#180161',font=('arial',25))
mdes2.place(x=35,y=110)
m2=Label(a,text='Enter the value',fg='white',bg='lime',font=('Myriad Pro',20))
m2.place(x=150,y=200)

m3=Entry(a,fg='lime',bg='white',font=('times new roman',20),textvariable=value1)
m3.place(x=350,y=200)

m4=Button(a,text='Armstrong',fg='#77e4c8',bg='#070f2b',font=('Futura',20),command=arm)
m4.place(x=300,y=300)

m5=Button(a,text='Even or Odd',fg='cyan',bg='#070f2b',font=('Futura',20),command=EO)
m5.place(x=300,y=400)

m6=Button(a,text='Leap year',fg='white',bg='#070f2b',font=('Futura',20),command=LY)
m6.place(x=300,y=500)

m7=Label(a,text='THANKS FOR USING ME :)',fg='white',bg='#5a639c',font=('Myriad Pro',30))
m7.place(x=150,y=650)

a.mainloop()
>>>>>>> 4a81e46a277a6aedb437f8b7d27d3c9be43210fa
