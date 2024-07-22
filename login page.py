from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from tkinter import messagebox
r = Tk()
r.geometry("500x600")
r.maxsize(500,700)
r.minsize(500,700)

'''conn = sqlite3.connect('form.db')
c = conn.cursor()
c.execute("CREATE TABLE f1(name text ,age int, gender text, room text, course text)")

conn.commit()
conn.close()''' 


def search():
    root = Toplevel(r)
    root.maxsize(350, 300)
    root.minsize(350, 300)
    Label(root, text="Search Data by Name",bg="green", fg="white", font="time 10 bold", padx=130, pady=20).grid(row=0,column=0, columnspan=10)
    e3 = Entry(root, width=30)
    e3.grid(row=1,column=0, columnspan=5, padx=10, pady=10)

    entry_button = Button(root, text="Search", bg="green", fg="white", font="time 10 bold", command=lambda :name(e3))
    entry_button.grid(row=1, column=5)
    def name(e3):
        conn = sqlite3.connect('form.db')
        c = conn.cursor()
        search_name = e3.get()
        c.execute("SELECT *,OID from f1 WHERE name=?", [search_name])
        records = c.fetchall()
        print(records)
        num = 2
        for i in records:
            name = Label(root, text=i[0], font="time 12 bold", fg="blue")
            name.grid(row=num, column=0, padx=20, pady=10)
            age = Label(root, text=i[1], font="time 12 bold", fg="blue")
            age.grid(row=num, column=1, padx=20, pady=10)
            gender = Label(root, text=i[2], font="time 12 bold", fg="blue")
            gender.grid(row=num, column=2, padx=20, pady=10)
            room = Label(root, text=i[3], font="time 12 bold", fg="blue")
            room.grid(row=num, column=3, padx=20, pady=10)
            course = Label(root, text=i[4], font="time 12 bold", fg="blue")
            course.grid(row=num, column=4, padx=20, pady=10)
            num = num + 1




        conn.commit()
        conn.close()




def next():
    #r1 = Toplevel(r)
    r1 = Tk()
    r1.geometry("600x600")
    r1.maxsize(550, 500)
    r1.minsize(550, 500)
    r1.title("Student Registration Records")
    conn = sqlite3.connect('form.db')
    c = conn.cursor()
    c.execute("SELECT *,OID from f1")
    Label(r1,text="Student Registration Records", font="time 25 bold", bg="blue", fg="white", padx=50, pady=10).grid(row=0,column=0,columnspan=20)
    Label(r1,text="Name", font="time 15 bold").grid(row=1,column=0,padx=20, pady=10)
    Label(r1, text="Age", font="time 15 bold").grid(row=1, column=1, padx=20, pady=10)
    Label(r1, text="Gender", font="time 15 bold").grid(row=1, column=2, padx=20, pady=10)
    Label(r1,text="Room", font="time 15 bold").grid(row=1,column=3,padx=20, pady=10)
    Label(r1, text="Course", font="time 15 bold").grid(row=1, column=4, padx=20, pady=10)

    num = 2
    records = c.fetchall()

    for i in records:
        name = Label(r1, text=i[0],font="time 12 bold", fg="blue")
        name.grid(row=num, column=0, padx=20, pady=10)
        age = Label(r1, text=i[1], font="time 12 bold", fg="blue")
        age.grid(row=num, column=1, padx=20, pady=10)
        gender = Label(r1, text=i[2], font="time 12 bold", fg="blue")
        gender.grid(row=num, column=2, padx=20, pady=10)
        room = Label(r1, text=i[3], font="time 12 bold", fg="blue")
        room.grid(row=num, column=3, padx=20, pady=10)
        course = Label(r1, text=i[4], font="time 12 bold", fg="blue")
        course.grid(row=num, column=4, padx=20, pady=10)

        num= num+1
    conn.commit()
    conn.close()

def action():
    name = e1.get()
    age = e2.get()
    gen =  gender.get()
    room = listroom.get()
    course1=""
    course2=""
    if var1.get()=="1":
        course1="Java"
    if var2.get()=="1":
        course2="Python"
    course= course1+" "+course2

    conn = sqlite3.connect('form.db')
    c = conn.cursor()

    if name=="" or age=="" or gen=="" or room=="":
        messagebox.showerror("Please fill the information","Information Reqiured")
    else:
        c.execute("INSERT INTO f1 VALUES(:name, :age, :gen, :room, :course)",
                  {
                      'name': name,
                      'age': int(age),
                      'gen': gen,
                      'room': room,
                      'course': course

                  })

        messagebox.showinfo("infomation", "Your record is Submitted")


    conn.commit()
    conn.close()
    e1.delete(0,END)
    e2.delete(0,END)






img = Image.open("im.png")
img = img.resize((100,100))

i1 = ImageTk.PhotoImage(img)
label = Label(r, image=i1)
label.place(x=200,y=10)

l1 = Label(r,text="Student Registration Panel", font="time 20 bold")
l1.place(x=75,y=120)

Label(r,text="Enter Name", font="time 10 bold").place(x=30,y=200)
e1 = Entry(r, width=30, bd=3)
e1.place(x=200,y=200)

Label(r,text="Enter age", font="time 10 bold").place(x=30,y=260)
e2 = Entry(r, width=30, bd=3)
e2.place(x=200,y=260)

Label(r,text="Select your Gender", font="time 10 bold").place(x=30,y=320)

gender = StringVar()
g1 = Radiobutton(r, text="Male", variable= gender, value="Male", font="time 10")
g1.select()
g1.place(x=200,y=320)
g2 = Radiobutton(r, text="Female", variable= gender, value="Female", font="time 10")
g2.deselect()
g2.place(x=300,y=320)

Label(r,text="Select Room", font="time 10 bold").place(x=30,y=380)
list = ["Ac Room", "Non Ac Room"]
listroom = StringVar()
listroom.set("Select your Room Type")
menu = OptionMenu(r, listroom, *list)
menu.place(x=200,y=380, width=190)

Label(r,text="Select Course", font="time 10 bold").place(x=30,y=440)
var1 = StringVar()
var2 = StringVar()
c1 = Checkbutton(r,text="Java", variable=var1, onvalue=1, offvalue=0, font= "time 10")
c1.deselect()
c1.place(x=200,y=440)
c2 = Checkbutton(r,text="Python", variable=var2, onvalue=1, offvalue=0, font= "time 10")
c2.select()
c2.place(x=300,y=440)

b1 = Button(r,text="Submit",fg="white", bg="blue", font="time 10 bold", width=44, command=action)
b1.place(x=32,y=500)
b2 = Button(r,text="Show",fg="white", bg="red", font="time 10 bold", width=20, command=next)
b2.place(x=32,y=550)

b3 = Button(r,text="Exit",fg="white", bg="blue", font="time 10 bold", width=20, command=r.destroy)
b3.place(x=225,y=550)

s1 = Button(r,text="Search", bg="green", fg="white", font="time 10 bold",width=10, command=search)
s1.place(x=180,y=600)

r.mainloop()