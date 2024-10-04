from tkinter import *
from tkinter import messagebox
from tkinter import StringVar
import sqlite3
import os
from PIL import ImageTk, Image
root=Tk()
root.title("Maan School Administration")
root.geometry("1280x727+-8+0")
root.resizable(0,0)
root.configure(background="#001E56")
##home page
def homepage():
    home_frame=Frame(root,bg="#23707B")
    home=Label(text="Home",bg="#86592D",fg="#fff",font=("",17))
    home.place(x=19,y=95)
    home_in_img=PhotoImage(file=r"images/home/home.png")
    home_in=Label(image=home_in_img,bg="#86592D")
    home_in.photo=home_in_img
    home_in.place(x=0,y=0)
    header=Frame(home_frame,bg="#86592D",width=1265,height=130).place(x=0)
    head=Label(header,text='        P.S. CHANDPUR JOGITHER', fg="#fff",bg="#86592D",
               font=("Algerian",35)).place(x=150,y=30)
    img = PhotoImage(file = r"images/logo.png")
    img_header=Button(header,image=img,bg='#ECD9C6',width=400,height=128,border=0)
    img_header.photo=img
    img_header.place(x=900,y=0)
    home_frame.place(x=0,y=0,width=1280,height=727)
#back Button
    imgback = PhotoImage(file = r"images/home/back.png")
    backbtn=Button(home_frame,image=imgback,bg="#23707B",
                   activebackground="#23707B",border=0)
    backbtn.photo=imgback
    backbtn.place(x=20,y=150)
    f_icon=Frame(home_frame,bg="#1B424E")
# teacher button
    def ht():
        os.startfile(r"phy 3 ans.pdf")
    def Show(event):
        choose_teacher.place(x =10, y = 370)
    def Hide(event):
        choose_teacher.place_forget()
    td=Label(f_icon,text="Teacher's Details ",bg="#1B424E",fg="white",font=("",15))
    td.place(x=10,y=200)
    img_teacher = PhotoImage(file = r"images/home/teacher.png")
    btn_teacher=Button(f_icon,image=img_teacher,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_teacher.photo=img_teacher
    btn_teacher.place(x=20,y=70)
    btn_teacher.bind("<Enter>", Show)
    choose_teacher=Frame(root,bg="#B5B078",border=5)
    selectteacher=Label(choose_teacher,text="Select Designation",bg="#B5B078",font=("",12),fg="#000")
    selectteacher.grid(column=0,row=0,padx=15)
    b_teacher=Button(choose_teacher,text="H.T.",font=("",15),command=ht,width=8,bg="#E7C386")
    b_teacher.bind("<Enter>",lambda e:b_teacher.configure(background="#CEB779"))
    b_teacher.bind("<Leave>",lambda e:b_teacher.configure(background="#E7C386"))
    b_teacher.grid(column=0,row=2,padx=1)
    b_teacher2=Button(choose_teacher,text="A.T.",font=("",15),width=8,bg="#E7C386")
    b_teacher2.bind("<Enter>",lambda e:b_teacher2.configure(background="#CEB779"))
    b_teacher2.bind("<Leave>",lambda e:b_teacher2.configure(background="#E7C386"))
    b_teacher2.grid(column=0,row=3,padx=1)
    b_teacher3=Button(choose_teacher,text="S.M.",font=("",15),width=8,bg="#E7C386")
    b_teacher3.bind("<Enter>",lambda e:b_teacher3.configure(background="#CEB779"))
    b_teacher3.bind("<Leave>",lambda e:b_teacher3.configure(background="#E7C386"))
    b_teacher3.grid(column=0,row=4,padx=1)
    choose_teacher.bind("<Leave>", Hide)
    
# SMC button
    img_smc = PhotoImage(file = r"images/home/smc.png")
    btn_smc=Button(f_icon,image=img_smc,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_smc.photo=img_smc
    btn_smc.place(x=180,y=70)
    smc=Label(f_icon,text=" SMC Details",bg="#1B424E",fg="white",font=("",15))
    smc.place(x=180,y=200)
# Time tablw button
    img_time = PhotoImage(file = r"images/home/time.png")
    btn_time=Button(f_icon,image=img_time,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_time.photo=img_time
    btn_time.place(x=340,y=90)
    time=Label(f_icon,text="Time Table",bg="#1B424E",fg="white",font=("",15))
    time.place(x=340,y=200)
# profile button
    img_show = PhotoImage(file = r"images/home/show.png")
    btn_show=Button(f_icon,image=img_show,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_show.photo=img_show
    btn_show.place(x=474,y=70)
    show=Label(f_icon,text="  All Student",bg="#1B424E",fg="white",font=("",15))
    show.place(x=480,y=200)
#soprt button
    img_player = PhotoImage(file = r"images/home/sport.png")
    btn_player=Button(f_icon,image=img_player,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_player.photo=img_player
    btn_player.place(x=630,y=80)
    player=Label(f_icon,text="  Sports",bg="#1B424E",fg="white",font=("",15))
    player.place(x=650,y=200)
#cwsn icon
    img_cwsn = PhotoImage(file = r"images/home/cwsn.png")
    btn_cwsn=Button(f_icon,image=img_cwsn,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_cwsn.photo=img_cwsn
    btn_cwsn.place(x=760,y=70)
    player=Label(f_icon,text="      CWSN",bg="#1B424E",fg="white",font=("",15))
    player.place(x=760,y=202)
#contact icon
    contact = PhotoImage(file = r"images/home/phone.png")
    btn_cont=Button(f_icon,image=contact,bg="#1B424E",activebackground="#1B424E",border=0)
    btn_cont.photo=contact
    btn_cont.place(x=900,y=70)
    cont=Label(f_icon,text="Contact \nInfo",bg="#1B424E",fg="white",font=("",15))
    cont.place(x=930,y=200)
# quit button
    img_quit = PhotoImage(file = r"images/exit.png")
    quitbtn=Button(f_icon,bg="#1B424E",border=0,
                   activebackground="#1B424E",image=img_quit)
    quitbtn.photo=img_quit
    quitbtn.place(x=1200,y=240)
    
    f_icon.place(x=0,y=300,width=1280,height=300)
homepage()
