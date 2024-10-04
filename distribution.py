from tkinter import *
from tkinter import messagebox
from tkinter import StringVar
import sqlite3
from PIL import ImageTk, Image
root=Tk()
root.title("Maan School Administration")
root.geometry("1280x727+-8+0")
root.resizable(0,0)
root.configure(background="#001E56")
## ------------------------------------------------distribution page---------------------------------------------------------------
global school_name
school_name="P.S. CHANDPUR JOGITHER \nNawabganj, Bareilly \nUDiseCode : 123455"

def distribution():
    def Show(event):
        choose_class.place(x = 25, y = 330)
    def Hide(event):
        choose_class.place_forget()
    distribution_frame=Frame(root,bg="#23707B")
    distribution=Label(text="Distribution",bg="#86592D",fg="#fff",font=("",17))
    distribution.place(x=19,y=92)
    distribution_in_img=PhotoImage(file=r"images/distribution/distribution.png")
    distribution_in=Label(image=distribution_in_img,bg="#86592D")
    distribution_in.photo=distribution_in_img
    distribution_in.place(x=30,y=7)
    header=Frame(distribution_frame,bg="#86592D",width=1265,height=130).place(x=0)
    head=Label(header,text=        school_name, fg="#fff",bg="#86592D",
               font=("Algerian",23)).place(x=300,y=10)
    img = PhotoImage(file = r"images/logo.png")
    img_header=Button(header,image=img,bg='#ECD9C6',width=400,height=128,border=0)
    img_header.photo=img
    img_header.place(x=900,y=0)
    distribution_frame.place(x=0,y=0,width=1280,height=727)
#back button
    imgback = PhotoImage(file = r"images/home/back.png")
    backbtn=Button(distribution_frame,image=imgback,bg="#23707B",
                   activebackground="#23707B",border=0)
    backbtn.photo=imgback
    backbtn.place(x=20,y=150)
    f_icon=Frame(distribution_frame,bg="#1B424E")
# books button
    td=Label(f_icon,text="Books ",bg="#1B424E",fg="white",font=("",15))
    td.place(x=55,y=200)
    img_books = PhotoImage(file = r"images/distribution/books.png")
    btn_books=Button(f_icon,image=img_books,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_books.photo=img_books
    btn_books.place(x=20,y=70)
    btn_books.bind("<Enter>", Show)
    choose_class=Frame(root,bg="#B5B078",border=5)
    selectclass=Label(choose_class,text="Select Class",bg="#B5B078",font=("",15),fg="#000")
    selectclass.grid(column=0,row=0,padx=15)
    b1=Button(choose_class,text="Class-I",font=("",15),width=10,bg="#E7C386")
    b1.bind("<Enter>",lambda e:b1.configure(background="#CEB779"))
    b1.bind("<Leave>",lambda e:b1.configure(background="#E7C386"))
    b1.grid(column=0,row=2,padx=1)
    def classII():
        classII_frame=Frame(root)
        distribution_frame=Frame(root,bg="#23707B")
        distribution=Label(text="Distribution",bg="#86592D",fg="#fff",font=("",17))
        distribution.place(x=19,y=92)
        distribution_in_img=PhotoImage(file=r"images/distribution/distribution.png")
        distribution_in=Label(image=distribution_in_img,bg="#86592D")
        distribution_in.photo=distribution_in_img
        distribution_in.place(x=30,y=7)
        header=Frame(distribution_frame,bg="#86592D",width=1265,height=130).place(x=0)
        head=Label(header,text=        school_name, fg="#fff",bg="#86592D",
                   font=("Algerian",23)).place(x=300,y=10)
        img = PhotoImage(file = r"images/logo.png")
        img_header=Button(header,image=img,bg='#ECD9C6',width=400,height=128,border=0)
        img_header.photo=img
        img_header.place(x=900,y=0)
        distribution_frame.place(x=0,y=0,width=1280,height=727)
        classII_frame.place(x=0,y=0,width=1280,height=727)
        classII_left_frame=Frame(root,bg="#D5D5D5")
        classII_left_frame.place(x=10,y=140,width=500,height=580)
        classII_right_frame=Frame(root,bg="#D5D5D5")
        classII_right_frame.place(x=520,y=140,width=750,height=580)
    b2=Button(choose_class,text="Class-II",command=classII,font=("",15),width=10,bg="#E7C386")
    b2.bind("<Enter>",lambda e:b2.configure(background="#CEB779"))
    b2.bind("<Leave>",lambda e:b2.configure(background="#E7C386"))
    b2.grid(column=0,row=3,padx=1)
    b3=Button(choose_class,text="Class-III",font=("",15),width=10,bg="#E7C386")
    b3.bind("<Enter>",lambda e:b3.configure(background="#CEB779"))
    b3.bind("<Leave>",lambda e:b3.configure(background="#E7C386"))
    b3.grid(column=0,row=4,padx=1)
    b4=Button(choose_class,text="Class-IV",font=("",15),width=10,bg="#E7C386")
    b4.bind("<Enter>",lambda e:b4.configure(background="#CEB779"))
    b4.bind("<Leave>",lambda e:b4.configure(background="#E7C386"))
    b4.grid(column=0,row=5,padx=1)
    b5=Button(choose_class,text="Class-V",font=("",15),width=10,bg="#E7C386")
    b5.bind("<Enter>",lambda e:b5.configure(background="#CEB779"))
    b5.bind("<Leave>",lambda e:b5.configure(background="#E7C386"))
    b5.grid(column=0,row=6,padx=1)
    choose_class.bind("<Leave>", Hide)


    
# bags button
    def Show(event):
        choose_bag.place(x = 170, y = 330)
    def Hide(event):
        choose_bag.place_forget()
    img_bags = PhotoImage(file = r"images/distribution/bags.png")
    btn_bags=Button(f_icon,image=img_bags,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_bags.photo=img_bags
    btn_bags.place(x=190,y=70)
    bags=Label(f_icon,text=" Bags",bg="#1B424E",fg="white",font=("",15))
    bags.place(x=225,y=200)
    btn_bags.bind("<Enter>", Show)
    choose_bag=Frame(root,bg="#B5B078",border=5)
    selectbag=Label(choose_bag,text="Select Class",bg="#B5B078",font=("",15),fg="#000")
    selectbag.grid(column=0,row=0,padx=15)
    b_bags=Button(choose_bag,text="Class-I",font=("",15),width=10,bg="#E7C386")
    b_bags.bind("<Enter>",lambda e:b_bags.configure(background="#CEB779"))
    b_bags.bind("<Leave>",lambda e:b_bags.configure(background="#E7C386"))
    b_bags.grid(column=0,row=2,padx=1)
    b_bags2=Button(choose_bag,text="Class-II",font=("",15),width=10,bg="#E7C386")
    b_bags2.bind("<Enter>",lambda e:b_bags2.configure(background="#CEB779"))
    b_bags2.bind("<Leave>",lambda e:b_bags2.configure(background="#E7C386"))
    b_bags2.grid(column=0,row=3,padx=1)
    b_bags3=Button(choose_bag,text="Class-III",font=("",15),width=10,bg="#E7C386")
    b_bags3.bind("<Enter>",lambda e:b_bags3.configure(background="#CEB779"))
    b_bags3.bind("<Leave>",lambda e:b_bags3.configure(background="#E7C386"))
    b_bags3.grid(column=0,row=4,padx=1)
    b_bags4=Button(choose_bag,text="Class-IV",font=("",15),width=10,bg="#E7C386")
    b_bags4.bind("<Enter>",lambda e:b_bags4.configure(background="#CEB779"))
    b_bags4.bind("<Leave>",lambda e:b_bags4.configure(background="#E7C386"))
    b_bags4.grid(column=0,row=5,padx=1)
    b_bags5=Button(choose_bag,text="Class-V",font=("",15),width=10,bg="#E7C386")
    b_bags5.bind("<Enter>",lambda e:b_bags5.configure(background="#CEB779"))
    b_bags5.bind("<Leave>",lambda e:b_bags5.configure(background="#E7C386"))
    b_bags5.grid(column=0,row=6,padx=1)
    choose_bag.bind("<Leave>", Hide)

# shoes button
    def Show(event):
        choose_shoes.place(x = 355, y = 330)
    def Hide(event):
        choose_shoes.place_forget()
    img_shoes= PhotoImage(file = r"images/distribution/shoes.png")
    btn_shoes=Button(f_icon,image=img_shoes,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_shoes.photo=img_shoes
    btn_shoes.place(x=360,y=50)
    shoes=Label(f_icon,text="Shoes\nand\nsocks",bg="#1B424E",fg="white",font=("",15))
    shoes.place(x=400,y=200)
    btn_shoes.bind("<Enter>", Show)
    choose_shoes=Frame(root,bg="#B5B078",border=5)
    selectshoes=Label(choose_shoes,text="Select Class",bg="#B5B078",font=("",15),fg="#000")
    selectshoes.grid(column=0,row=0,padx=15)
    b_shoes=Button(choose_shoes,text="Class-I",font=("",15),width=10,bg="#E7C386")
    b_shoes.bind("<Enter>",lambda e:b_shoes.configure(background="#CEB779"))
    b_shoes.bind("<Leave>",lambda e:b_shoes.configure(background="#E7C386"))
    b_shoes.grid(column=0,row=2,padx=1)
    b_shoes2=Button(choose_shoes,text="Class-II",font=("",15),width=10,bg="#E7C386")
    b_shoes2.bind("<Enter>",lambda e:b_shoes2.configure(background="#CEB779"))
    b_shoes2.bind("<Leave>",lambda e:b_shoes2.configure(background="#E7C386"))
    b_shoes2.grid(column=0,row=3,padx=1)
    b_shoes3=Button(choose_shoes,text="Class-III",font=("",15),width=10,bg="#E7C386")
    b_shoes3.bind("<Enter>",lambda e:b_shoes3.configure(background="#CEB779"))
    b_shoes3.bind("<Leave>",lambda e:b_shoes3.configure(background="#E7C386"))
    b_shoes3.grid(column=0,row=4,padx=1)
    b_shoes4=Button(choose_shoes,text="Class-IV",font=("",15),width=10,bg="#E7C386")
    b_shoes4.bind("<Enter>",lambda e:b_shoes4.configure(background="#CEB779"))
    b_shoes4.bind("<Leave>",lambda e:b_shoes4.configure(background="#E7C386"))
    b_shoes4.grid(column=0,row=5,padx=1)
    b_shoes5=Button(choose_shoes,text="Class-V",font=("",15),width=10,bg="#E7C386")
    b_shoes5.bind("<Enter>",lambda e:b_shoes5.configure(background="#CEB779"))
    b_shoes5.bind("<Leave>",lambda e:b_shoes5.configure(background="#E7C386"))
    b_shoes5.grid(column=0,row=6,padx=1)
    choose_shoes.bind("<Leave>", Hide)    
# dress button
    def Show(event):
        choose_dress.place(x = 520, y = 330)
    def Hide(event):
        choose_dress.place_forget()
    img_dress= PhotoImage(file = r"images/distribution/dress.png")
    btn_dress=Button(f_icon,image=img_dress,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_dress.photo=img_dress
    btn_dress.place(x=534,y=70)
    dress=Label(f_icon,text="Uniform",bg="#1B424E",fg="white",font=("",15))
    dress.place(x=560,y=200)
    btn_dress.bind("<Enter>", Show)
    choose_dress=Frame(root,bg="#B5B078",border=5)
    selectdress=Label(choose_dress,text="Select Class",bg="#B5B078",font=("",15),fg="#000")
    selectdress.grid(column=0,row=0,padx=15)
    b_dress=Button(choose_dress,text="Class-I",font=("",15),width=10,bg="#E7C386")
    b_dress.bind("<Enter>",lambda e:b_dress.configure(background="#CEB779"))
    b_dress.bind("<Leave>",lambda e:b_dress.configure(background="#E7C386"))
    b_dress.grid(column=0,row=2,padx=1)
    b_dress2=Button(choose_dress,text="Class-II",font=("",15),width=10,bg="#E7C386")
    b_dress2.bind("<Enter>",lambda e:b_dress2.configure(background="#CEB779"))
    b_dress2.bind("<Leave>",lambda e:b_dress2.configure(background="#E7C386"))
    b_dress2.grid(column=0,row=3,padx=1)
    b_dress3=Button(choose_dress,text="Class-III",font=("",15),width=10,bg="#E7C386")
    b_dress3.bind("<Enter>",lambda e:b_dress3.configure(background="#CEB779"))
    b_dress3.bind("<Leave>",lambda e:b_dress3.configure(background="#E7C386"))
    b_dress3.grid(column=0,row=4,padx=1)
    b_dress4=Button(choose_dress,text="Class-IV",font=("",15),width=10,bg="#E7C386")
    b_dress4.bind("<Enter>",lambda e:b_dress4.configure(background="#CEB779"))
    b_dress4.bind("<Leave>",lambda e:b_dress4.configure(background="#E7C386"))
    b_dress4.grid(column=0,row=5,padx=1)
    b_dress5=Button(choose_dress,text="Class-V",font=("",15),width=10,bg="#E7C386")
    b_dress5.bind("<Enter>",lambda e:b_dress5.configure(background="#CEB779"))
    b_dress5.bind("<Leave>",lambda e:b_dress5.configure(background="#E7C386"))
    b_dress5.grid(column=0,row=6,padx=1)
    choose_dress.bind("<Leave>", Hide)    

# quit button
    img_quit = PhotoImage(file = r"images/exit.png")
    quitbtn=Button(f_icon,bg="#1B424E",border=0,
                   activebackground="#1B424E",image=img_quit)
    quitbtn.photo=img_quit
    quitbtn.place(x=1200,y=240)
    
    f_icon.place(x=0,y=300,width=1280,height=300)
distribution()
