from tkinter import *
from tkinter import messagebox as tkMessageBox
from tkinter.font import Font
from PIL import Image,ImageTk
import sqlite3


Afnan = Tk()
Afnan.title("Welcome to Movies")
Afnan.geometry('1000x800')
Afnan.configure(background='black')
fo = Font(family="Georgia",size=42,weight="bold",slant="roman",underline=0,overstrike=0)
f = Font(family="Georgia",size=20,weight="bold",slant="roman",underline=0,overstrike=0)
a = Label(Afnan, text="Welcome to Movies ",background = "black", fg='white', font=fo)
a.place(x=250,y=20)  # place
b = Label(Afnan, text="what movie you want to sign for? ",background = "black", fg='white', font=f)
b.place(x=300,y=120)  # place

#SQL

conn = sqlite3.connect('customer.db')
cursorObj = conn.cursor()

def sql_table():
    cursorObj.execute("CREATE TABLE customer(name text , email text)")





def re1():
    Sara = Tk()
    Sara.title("Registration form")
    Sara.geometry('500x500')
    Sara.configure(background='black')
    s = Font(family="Cambria", size=10, weight="bold", slant="roman", underline=2, overstrike=0)
    label_0 = Label(Sara, text="HOTEL TRANSYLVANIA", width=20, background = "black", fg='white',font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(Sara, text="FullName",background = "black", fg='white', width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(Sara)
    entry_1.place(x=240, y=130)
    label_2 = Label(Sara, text="Email",background = "black", fg='white', width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_2 = Entry(Sara )
    entry_2.place(x=240, y=180)
    label_3 = Label(Sara, text="Seat",background = "black", fg='white',width=20, font=("bold", 10))
    label_3.place(x=10, y=230)
    var = IntVar()
    Radiobutton(Sara, text="S1", padx=5, variable=var, value=1).place(x=250, y=230)
    Radiobutton(Sara, text="A1", padx=20, variable=var, value=2).place(x=290, y=230)
    Radiobutton(Sara, text="C1", padx=5, variable=var, value=3).place(x=130, y=230)
    Radiobutton(Sara, text="D3", padx=20, variable=var, value=4).place(x=180, y=230)
    label_4 = Label(Sara, text="*Note : This is just a Pre-booking seats!", background = "black",font= s ,fg = 'red')
    label_4.place(x=30, y=300)
    label_5 = Label(Sara, text="Payment will be at the movie place.",background = "black", font= s ,fg = 'red')
    label_5.place(x=30, y=330)
    Button(Sara, text='save data', width=20, bg='brown', fg='white',command =cursorObj.execute("INSERT INTO customer (name, email) values (?,?) ", (str(entry_1),str(entry_2)))).place(x=180, y=380)
    Button(Sara, text='submit', width=20, bg='brown', fg='white',command =m).place(x=180, y=420)



def re2():
    Ghadeer = Tk()
    Ghadeer.title("Registration form")
    Ghadeer.geometry('500x500')
    Ghadeer.configure(background='black')
    s = Font(family="Cambria", size=10, weight="bold", slant="roman", underline=2, overstrike=0)
    label_0 = Label(Ghadeer, text="BLOOD STEEL", width=20, background = "black", fg='white',font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(Ghadeer, text="FullName",background = "black", fg='white', width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(Ghadeer)
    entry_1.place(x=240, y=130)
    label_2 = Label(Ghadeer, text="Email",background = "black", fg='white', width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_2 = Entry(Ghadeer)
    entry_2.place(x=240, y=180)
    label_3 = Label(Ghadeer, text="Seat",background = "black", fg='white',width=20, font=("bold", 10))
    label_3.place(x=10, y=230)
    var = IntVar()
    Radiobutton(Ghadeer, text="S1", padx=5, variable=var, value=1).place(x=250, y=230)
    Radiobutton(Ghadeer, text="A1", padx=20, variable=var, value=2).place(x=290, y=230)
    Radiobutton(Ghadeer, text="C1", padx=5, variable=var, value=3).place(x=130, y=230)
    Radiobutton(Ghadeer, text="D3", padx=20, variable=var, value=4).place(x=180, y=230)
    label_4 = Label(Ghadeer, text="*Note : This is just a Pre-booking seats!", background = "black",font= s ,fg = 'red')
    label_4.place(x=30, y=300)
    label_5 = Label(Ghadeer, text="Payment will be at the movie place.",background = "black", font= s ,fg = 'red')
    label_5.place(x=30, y=330)
    Button(Ghadeer, text='save data', width=20, bg='brown', fg='white',command =cursorObj.execute("INSERT INTO customer (name, email) values (?,?) ", (str(entry_1),str(entry_2)))).place(x=180, y=380)
    Button(Ghadeer, text='submit', width=20, bg='brown', fg='white',command =m).place(x=180, y=420)

def re3():
    Afaf = Tk()
    Afaf.title("Registration form")
    Afaf.geometry('500x500')
    Afaf.configure(background='black')
    s = Font(family="Cambria", size=10, weight="bold", slant="roman", underline=2, overstrike=0)
    label_0 = Label(Afaf, text="X", width=20, background = "black", fg='white',font=("bold", 20))
    label_0.place(x=90, y=53)
    label_1 = Label(Afaf, text="FullName",background = "black", fg='white', width=20, font=("bold", 10))
    label_1.place(x=80, y=130)
    entry_1 = Entry(Afaf)
    entry_1.place(x=240, y=130)
    label_2 = Label(Afaf, text="Email",background = "black", fg='white', width=20, font=("bold", 10))
    label_2.place(x=68, y=180)
    entry_2 = Entry(Afaf)
    entry_2.place(x=240, y=180)
    label_3 = Label(Afaf, text="Seat",background = "black", fg='white',width=20, font=("bold", 10))
    label_3.place(x=10, y=230)
    var = IntVar()
    Radiobutton(Afaf, text="S1", padx=5, variable=var, value=1).place(x=250, y=230)
    Radiobutton(Afaf, text="A1", padx=20, variable=var, value=2).place(x=290, y=230)
    Radiobutton(Afaf, text="C1", padx=5, variable=var, value=3).place(x=130, y=230)
    Radiobutton(Afaf, text="D3", padx=20, variable=var, value=4).place(x=180, y=230)
    label_4 = Label(Afaf, text="*Note : This is just a Pre-booking seats!", background = "black",font= s ,fg = 'red')
    label_4.place(x=30, y=300)
    label_5 = Label(Afaf, text="Payment will be at the movie place.",background = "black", font= s ,fg = 'red')
    label_5.place(x=30, y=330)
    Button(Afaf, text='save data', width=20, bg='brown', fg='white',command =cursorObj.execute("INSERT INTO customer (name, email) values (?,?) ", (str(entry_1),str(entry_2)))).place(x=180, y=380)
    Button(Afaf, text='submit', width=20, bg='brown', fg='white',command =m).place(x=180, y=420)

def m():
   tkMessageBox.showinfo( "complete", "Done!")






mov1 = ImageTk.PhotoImage(Image.open('M1.jpg'))
c = Button(image=mov1 , width=250,height=380 , background='black',command = re1)
c.place(x=20,y=250)
mov2 = ImageTk.PhotoImage(Image.open('M6.jpg'))
d = Button(image=mov2, width=250,height=380 , background='black',command = re2)
d.place(x=350,y=250)
mov3 = ImageTk.PhotoImage(Image.open('M3.jpeg'))
d = Button(image=mov3, width=250,height=380 , background='black',command = re3)
d.place(x=700,y=250)


#SQL
conn.commit()



Afnan.mainloop()
sql_table()
