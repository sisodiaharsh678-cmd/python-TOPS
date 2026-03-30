from tkinter import *

root = Tk()
root.geometry("500x500")
root.title("My Tkinter example")

l_id = Label(root, text="ID", font=("Arial", 10))
l_id.place(x=50, y=50)

l_fname = Label(root, text="FIRST NAME", font=("Arial", 10))
l_id.place(x=50, y=100)

l_lname = Label(root, text="LAST NAME", font=("Arial", 10))
l_id.place(x=50, y=150)

l_email = Label(root, text="EMAIL", font=("Arial", 10))
l_id.place(x=50, y=200)

l_mobile = Label(root, text="MOBILE", font=("Arial", 10))
l_id.place(x=50, y=250)

e_id=Entry(root)
e_id.place(x=200,y=50)

e_fname=Entry(root)
e_id.place(x=200,y=100)

e_lname=Entry(root)
e_id.place(x=200,y=150)

e_email=Entry(root)
e_id.place(x=200,y=200)

e_mobile=Entry(root)
e_id.place(x=200,y=250)

insert = Button(root , text="INSERT" , bg="black" , fg="white" , font=("Arial" , 12))
insert.place(x=50 , y=300)

insert = Button(root , text="SEARCH" , bg="black" , fg="white" , font=("Arial" , 12))
insert.place(x=120 , y=300)

insert = Button(root , text="UPDATE" , bg="black" , fg="white" , font=("Arial" , 12))
insert.place(x=201 , y=300)

insert = Button(root , text="DELETE" , bg="black" , fg="white" , font=("Arial" , 12))
insert.place(x=280 , y=300)



root.mainloop()  