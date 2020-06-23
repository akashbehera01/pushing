Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tkinter import *
from tkinter import messagebox
import sqlite3
# global variable
z = 0
box = Tk()
def add_data():
    f = Tk()
    lab1 = Label(f, text='Name :').place(x=150,y=150)
    ent1 = Entry(f, width=58, )
    ent1.place(x=300,y=150)

    lab2 = Label(f, text='Email :').place(x=150,y=200)
    ent2 = Entry(f, width=58)
    ent2.place(x=300,y=200)

    lab3 = Label(f, text='DOB(dd/mm/yyyy) :').place(x=150,y=250)
    ent3 = Entry(f, width=58)
    ent3.place(x=300,y=250)


    lab4 = Label(f, text='phone No :').place(x=150,y=300)
    ent4 = Entry(f, width=58)
    ent4.place(x=300,y=300)


    def ButC():
        var1 = StringVar()
        global z
        a = ent1.get()  # name
        b = ent2.get()  # email
        c = ent3.get()  # dob
        d = ent4.get()  # phone no

        if (len(a) > 0):
            if (b.find('@') != -1 and b.find('.') != -1 and (
                    (b.index('.') == len(b) - 3 - 1) or (b.index('.') == len(b) - 2 - 1))):
                l = c.split('/')
                if (1 <= int(l[0]) < 31 and 1 <= int(l[1]) <= 12 and 1000<= int(l[2]) < 2020):
                    if (len(d) == 10):
                        z= z+1
                        add_datab()
                    else:
                        var1 = messagebox.askretrycancel("enter valid phno")
                else:
                    var1 = messagebox.askretrycancel("enter valid date of birth")

            else:
                var1 = messagebox.askretrycancel("enter valid email address")
        else:
            var1 = messagebox.askretrycancel("enter name")

    def add_datab():
        global z
        a = ent1.get()  # name
        b = ent2.get()  # email
        c = ent3.get()  # dob
        d = ent4.get()  # phone no

        con = sqlite3.connect('python.db')

        cur = con.cursor()
        if z == 1:
            cur.execute("""CREATE TABLE Detail_1 ( name ,email ,dob ,phone integer)""")
            cur.execute("INSERT INTO Detail_1 (name,email,dob,phone) Values(?,?,?,?)",[a,b,c,d])
        else:
            cur.execute("INSERT INTO Detail_1 (name,email,dob,phone) Values(?,?,?,?)", [a, b, c, d])
        ent1.delete(0, END)
        ent2.delete(0, END)
        ent3.delete(0, END)
        ent4.delete(0, END)


        con.commit()

    but1 = Button(f, text='submit', command=ButC, bg='red').place(x=200,y=400)
    but2 = Button(f, text='clear' , command=ButC, bg='green').place(x=400,y=400)
    but3 = Button(f, text='cancel', command=ButC, bg='yellow').place(x=600,y=400)
    f.geometry("1000x1000")
    f.mainloop()
def show_data():
    f= Tk()
    lab1= Label(f,text="NAME").place(x=150,y=150)
    lab2 = Label(f, text="EMAIL").place(x=250, y=150)
    lab3= Label(f,text="DOB").place(x=350,y=150)
    lab4 = Label(f, text="PHONE NO").place(x=450, y=150)

    con = sqlite3.connect('python.db')
    cur = con.cursor()
    cur.execute("SELECT * from Detail_1")
    l = list(cur.fetchall())
    y1=200
    for i in l:
        x1 = 150
        d = list(i)
        for j in d:
            lab5 = Label(f,text=str(j)).place(x=x1,y=y1)
            x1 = x1+ 100
        y1 = y1 + 100


    con.commit()
    f.geometry("1000x1000")
    f.mainloop()


b1 = Button(box,text = "ADD",command = add_data).place(x=200,y=300)
b2 = Button(box,text = "CHECK",command = show_data).place(x=400,y=300)
box.geometry("500x500")
box.mainloop()
