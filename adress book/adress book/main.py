from tkinter import *
from tkinter.filedialog import *


window = Tk()
window.geometry("500x500")
window.configure(bg = "light green")

myAddressBook = {}

def clear_all():
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    entry4.delete(0,END)
    entry5.delete(0,END)

def add ():
    key = entry1.get()
    if key not in myAddressBook.keys():
        list1.insert(END,key)
    myAddressBook[key]= (entry2.get(),entry3.get(),entry4.get(),entry5.get())
    clear_all()

def edit ():
    global myAddresBook
    clear_all()
    index = list1.curselection()
    detals = myAddressBook[list1.get(index)]
    entry1.insert(0,list1.get(index))
    entry2.insert(0,detals[0])
    entry3.insert(0,detals[1])
    entry4.insert(0,detals[2])
    entry5.insert(0,detals[3])

def save ():
    f = asksaveasfile(defaultextension = ".txt")
    print(myAddressBook,file =f)

def delete():
    d = list1.curselection()
    list1.delete(d)

def open ():
    global myAddressBook
    o = askopenfile(title = "OPEN FILE!!!!!!;")
    myAddressBook = eval(o.read())
    for key in myAddressBook.keys():
        list1.insert(END,key)


lable1 = Label(window,text= "my adress book",bg = "light green")
lable1.pack(side = TOP)

button1 = Button(window,text= "open",command = open)
button1.pack(side = TOP)

Frame1 = Frame(window,bg= "blue")
Frame1.pack(side  = RIGHT,fill = BOTH)

lable2 = Label(window,text= "name",bg = "light green")
lable2.place(x=0,y=100)

lable3 = Label(window,text= " adress",bg = "light green")
lable3.place(x=0,y=150)

lable4 = Label(window,text= "mobile",bg = "light green")
lable4.place(x=0,y=200)

lable5 = Label(window,text= "email",bg = "light green")
lable5.place(x=0,y=250)

lable6 = Label(window,text= "birthday",bg = "light green")
lable6.place(x=0,y=300)

entry1=Entry(window,font = ("Arial"),fg = "black",bg="violet")
entry1.place(x = 100,y=100)

entry2=Entry(window,font = ("Arial"),fg = "black",bg="violet")
entry2.place(x = 100,y=150)

entry3=Entry(window,font = ("Arial"),fg = "black",bg="violet")
entry3.place(x = 100,y=200)

entry4=Entry(window,font = ("Arial"),fg = "black",bg="violet")
entry4.place(x = 100,y=250)

entry5=Entry(window,font = ("Arial"),fg = "black",bg="violet")
entry5.place(x = 100,y=300)

list1 = Listbox(window,width = 17,height = 14,bg = "violet")
list1.place(x = 300,y = 100)

button2 = Button(window,text= "edit",command = edit)
button2.place(x = 400,y = 350)

button3 = Button(window,text= "delete",command = delete)
button3.place(x = 325,y = 350)

button4 = Button(window,text= "update/add",command = add)
button4.place(x =100,y = 350)

button5 = Button(window,text= "save",width = 45,command = save)
button5.place(x = 50,y = 400)






window.mainloop()