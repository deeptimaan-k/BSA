import sqlite3
import sqlite3
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("My Books")
def view():
    db=sqlite3.connect('School_data.db')
    cr=db.cursor()
    cr.execute("SELECT * FROM teacher_profile")
    rows=cr.fetchall()
    return rows

def get_selected_row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    e1.delete(0, END)
    e1.insert(END, selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END, selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END, selected_tuple[3])
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="ISBN")
l3.grid(row=1, column=0)

title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

isbn_text = StringVar()
e3 = Entry(window, textvariable=isbn_text)
e3.grid(row=1, column=1)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)
