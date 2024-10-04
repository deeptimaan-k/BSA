from tkinter import *
from tkinter import ttk
import sqlite3
from tkcalendar import DateEntry
from tkinter import StringVar
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
from tkinter import filedialog
root=Tk()
root.geometry("1280x727+-8+0")
root.resizable(0,0)
root.configure(background="#2A579A")
global school_name
school_name="P.S. CHANDPUR JOGITHER \nNawabganj, Bareilly \nUDiseCode : 123455"
s=0
def show_profile():
    global school_name
    school_name="P.S. CHANDPUR JOGITHER \nNawabganj, Bareilly \nUDiseCode : 123455"
    main_frame=Frame(root,bg="green")
    header=Label(main_frame,bg="#86592D",width=1265,height=130)
    header.pack()
    head=Label(header,text=school_name,font=("Algerian",23),bg="#86592D",fg="#fff")
    head.place(x=300,y=13)
    img = PhotoImage(file = r"images/logo.png")
    img_header=Button(header,image=img,bg='#ECD9C6',width=400,height=128,border=0)
    img_header.photo=img
    img_header.place(x=900,y=0)
    main_frame.place(x=0,y=0,height=130)
    info_frame=Frame(root,bg="#DCDCEA")
    imgback = PhotoImage(file = r"images/home/back.png")
    backbtn=Button(info_frame,image=imgback,bg="#DCDCEA",
                   activebackground="#23707B",border=0)
    backbtn.photo=imgback
    backbtn.place(x=20,y=20)
    name1=StringVar()
    phone1=StringVar()
    email1=StringVar()
    pan1=StringVar()
    aadhar1=StringVar()
    RELEAVING1=StringVar()
    dob1=StringVar()
    homedis1=StringVar()
    group1=StringVar()
    gender1=StringVar()
    ehrms1=StringVar()
    cadre1=StringVar()
    levelincadre2=StringVar()
    dateofapp1=StringVar()
    dateofjoin1=StringVar()
    dateofcurrent1=StringVar()
    qualification1=StringVar()
    imgaddtext=StringVar()
    imgaddentry=StringVar()
    imgaddtext=''

    searchby=StringVar()
    searchtext=StringVar()
    admclass=StringVar()
    def chooseimage():
        global imgaddtext
        filename=filedialog.askopenfilename(initialdir="C:/",title="choose file",filetype=(("jpg","*.jpg"),("png","*.png")))
        imgaddtext=filename
        
    def search_teacher():
        
        
        
        conn=sqlite3.connect("School_data.db")
        c=conn.cursor()
        
        if(searchby.get()=='eHRMS CODE'):
            c.execute("SELECT * FROM teacher_profile WHERE eHRMS_CODE ='"+searchtext.get()+"'")
            records=c.fetchall()
            for r1 in records:    
                name1.set(r1[1])
                ehrms1.set(r1[2])
                dob1.set(r1[3])
                cadre1.set(r1[4])
                levelincadre2.set(r1[5])
                gender1.set(r1[6])
                homedis1.set(r1[7])
                group1.set(r1[8])
                qualification1.set(r1[9])
                dateofapp1.set(r1[10])
                dateofjoin1.set(r1[11])
                dateofcurrent1.set(r1[12])
                phone1.set(r1[13])
                email1.set(r1[14])
                pan1.set(r1[15])
                aadhar1.set(r1[16])
                RELEAVING1.set(r1[17])
                imgaddtext=record[18]
                
            
        elif(searchby.get()=='Name'):
            
            c.execute("SELECT * FROM teacher_profile WHERE NAME='"+searchtext.get()+"'")
            records=c.fetchall()
            for r1 in records: 
                name1.set(r1[1])
                ehrms1.set(r1[2])
                dob1.set(r1[3])
                cadre1.set(r1[4])
                levelincadre2.set(r1[5])
                gender1.set(r1[6])
                homedis1.set(r1[7])
                group1.set(r1[8])
                qualification1.set(r1[9])
                dateofapp1.set(r1[10])
                dateofjoin1.set(r1[11])
                dateofcurrent1.set(r1[12])
                phone1.set(r1[13])
                email1.set(r1[14])
                pan1.set(r1[15])
                aadhar1.set(r1[16])
                RELEAVING1.set(r1[17])
                imgaddtext=record[18]
         
        
        
        conn.commit()
        conn.close()
    def insertdata_teacher():
        global s
        f=1
        db=sqlite3.connect('School_data.db')
        cr=db.cursor()
        r=cr.execute("SELECT * FROM teacher_profile WHERE SN=%d" %f)
        for r1 in r:
            name1.set(r1[1])
            ehrms1.set(r1[2])
            dob1.set(r1[3])
            cadre1.set(r1[4])
            levelincadre2.set(r1[5])
            gender1.set(r1[6])
            homedis1.set(r1[7])
            group1.set(r1[8])
            qualification1.set(r1[9])
            dateofapp1.set(r1[10])
            dateofjoin1.set(r1[11])
            dateofcurrent1.set(r1[12])
            phone1.set(r1[13])
            email1.set(r1[14])
            pan1.set(r1[15])
            aadhar1.set(r1[16])
            RELEAVING1.set(r1[17])
            imgaddtext=record[18]
            s=1
            break
    def next_btn():
        global s
        s+=1
        if s==12:
            s=s-1
        db=sqlite3.connect('School_data.db')
        cr=db.cursor()
        r=cr.execute("SELECT * FROM teacher_profile WHERE SN=%d" %s)
        for r1 in r:
            name1.set(r1[1])
            ehrms1.set(r1[2])
            dob1.set(r1[3])
            cadre1.set(r1[4])
            levelincadre2.set(r1[5])
            gender1.set(r1[6])
            homedis1.set(r1[7])
            group1.set(r1[8])
            qualification1.set(r1[9])
            dateofapp1.set(r1[10])
            dateofjoin1.set(r1[11])
            dateofcurrent1.set(r1[12])
            phone1.set(r1[13])
            email1.set(r1[14])
            pan1.set(r1[15])
            aadhar1.set(r1[16])
            RELEAVING1.set(r1[17])
            imgaddtext=record[18]
    def back_btn():
        global s
        s=s-1
        db=sqlite3.connect('School_data.db')
        cr=db.cursor()
        r=cr.execute("SELECT * FROM teacher_profile WHERE SN=%d" %s)
        if s==0:
            s=1
        for r1 in r:
            name1.set(r1[1])
            ehrms1.set(r1[2])
            dob1.set(r1[3])
            cadre1.set(r1[4])
            levelincadre2.set(r1[5])
            gender1.set(r1[6])
            homedis1.set(r1[7])
            group1.set(r1[8])
            qualification1.set(r1[9])
            dateofapp1.set(r1[10])
            dateofjoin1.set(r1[11])
            dateofcurrent1.set(r1[12])
            phone1.set(r1[13])
            email1.set(r1[14])
            pan1.set(r1[15])
            aadhar1.set(r1[16])
            RELEAVING1.set(r1[17])
            imgaddtext=record[18]
    def insertdata_teacher_LAST():
        global s
        s=11
        if s==12:
            s=11
        db=sqlite3.connect('School_data.db')
        cr=db.cursor()
        l=11
        r=cr.execute("SELECT * FROM teacher_profile WHERE SN=%d" %l)
        for r1 in r:
            name1.set(r1[1])
            ehrms1.set(r1[2])
            dob1.set(r1[3])
            cadre1.set(r1[4])
            levelincadre2.set(r1[5])
            gender1.set(r1[6])
            homedis1.set(r1[7])
            group1.set(r1[8])
            qualification1.set(r1[9])
            dateofapp1.set(r1[10])
            dateofjoin1.set(r1[11])
            dateofcurrent1.set(r1[12])
            phone1.set(r1[13])
            email1.set(r1[14])
            pan1.set(r1[15])
            aadhar1.set(r1[16])
            RELEAVING1.set(r1[17])
            imgaddtext=record[18]
    h1=Label(info_frame,text="Personal Information:",font=("times new roman",17,"bold","underline"),bg="#DCDCEA")
    h1.place(x=150,y=30)
    name=Label(info_frame,text="NAME",font=("times new roman",13,"bold"),bg="#DCDCEA")
    name.place(x=50,y=100)
    name_entry=Entry(info_frame,state="readonly",bg="white",font=("times new roman",13,"bold"),bd=3,textvariable=name1)
    name_entry.place(x=260,y=100)
    search_frame=Frame(info_frame,bg="#DCDCEA")  
    droplabel=Label(search_frame,text="Search by:",bg="#DCDCEA",font=("times new roman",13,"bold"))
    droplabel.place(x=0,y=0,height=30)
    search_combo=Combobox(search_frame,width=18,state="readonly",font=("times new roman",13,"bold"),textvariable=searchby)
    search_combo['values']=("Name","eHRMS CODE")
    search_combo.place(x=90,y=0,height=30)
    searche=Entry(search_frame,width=20,font=("times new roman",13,"bold"),textvariable=searchtext)
    searche.place(x=280,y=0,height=30,width=300)
    searchb=Button(search_frame,command=search_teacher,text="Search",font=("times new roman",13,"bold"),fg="white",bg="green")
    searchb.place(x=600,y=0,width=80,height=30)
    search_frame.place(x=450,y=30,width=800,height=30)


    ehrms=Label(info_frame,text="eHRMS CODE",font=("times new roman",13,"bold"),bg="#DCDCEA")
    ehrms.place(x=50,y=150)
    ehrms_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=ehrms1)
    ehrms_entry.place(x=260,y=150)

    cal=Entry(info_frame,bd=3,state="readonly",textvariable=dob1,font=("",13,"bold"))
    cal.place(x=260,y=200,width=190,height=30)
    dob=Label(info_frame,text="DOB",font=("times new roman",13,"bold"),bg="#DCDCEA")
    dob.place(x=50,y=200)

    cadre=Label(info_frame,text="CADRE",font=("times new roman",13,"bold"),bg="#DCDCEA")
    cadre.place(x=50,y=250)
    cadre_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=cadre1)
    cadre_entry.place(x=260,y=250)

    levelincarder=Label(info_frame,text="LEVEL IN CADRE",font=("times new roman",13,"bold"),bg="#DCDCEA")
    levelincarder.place(x=50,y=300)
    levelincarder_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=levelincadre2)
    levelincarder_entry.place(x=260,y=300)

    gender=Label(info_frame,text="GENDER",font=("times new roman",13,"bold"),bg="#DCDCEA")
    gender.place(x=50,y=350)
    gender=Entry(info_frame,bd=3,state="readonly", font=("times new roman",13,"bold"),textvariable=gender1)
    gender.place(x=260,y=350,width=190)


    homedic=Label(info_frame,text="HOME DISTRICT",font=("times new roman",13,"bold"),bg="#DCDCEA")
    homedic.place(x=50,y=400)
    homedic_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=homedis1)
    homedic_entry.place(x=260,y=400)

    group=Label(info_frame,text="GROUP",font=("times new roman",13,"bold"),bg="#DCDCEA")
    group.place(x=50,y=450)
    group_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=group1)
    group_entry.place(x=260,y=450)

    qualification=Label(info_frame,text="QUALIFICATION",font=("times new roman",13,"bold"),bg="#DCDCEA")
    qualification.place(x=50,y=500)
    qualification_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=qualification1)
    qualification_entry.place(x=260,y=500)

    date_appo=Label(info_frame,text="DATE OF APPOINTMENT",font=("times new roman",13,"bold"),bg="#DCDCEA")
    date_appo.place(x=500,y=100)
    date_appo_entry=Entry(info_frame,bd=3,state="readonly",textvariable=dateofapp1,font=("",13,"bold"))
    date_appo_entry.place(x=740,y=100,width=190,height=30)

    date_join=Label(info_frame,text="DATE OF JOINING",font=("times new roman",13,"bold"),bg="#DCDCEA")
    date_join.place(x=500,y=150)
    date_join_entry=Entry(info_frame,state="readonly",bd=3,textvariable=dateofjoin1,font=("",13,"bold"))
    date_join_entry.place(x=740,y=150,width=190,height=30)

    date_current=Label(info_frame,text="DATE OF CURRENT JOINING",font=("times new roman",13,"bold"),bg="#DCDCEA")
    date_current.place(x=500,y=200)
    date_current_entry=Entry(info_frame,state="readonly",bd=3,textvariable=dateofcurrent1,font=("",13,"bold"))
    date_current_entry.place(x=740,y=200,width=190,height=30)



    mobile=Label(info_frame,text="MOBILE NO.",font=("times new roman",13,"bold"),bg="#DCDCEA")
    mobile.place(x=500,y=250)
    mobile_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=phone1)
    mobile_entry.place(x=740,y=250)

    email=Label(info_frame,text="EMAIL",font=("times new roman",13,"bold"),bg="#DCDCEA")
    email.place(x=500,y=300)
    email_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=email1)
    email_entry.place(x=740,y=300)	

    pan=Label(info_frame,text="PAN CARD NO.",font=("times new roman",13,"bold"),bg="#DCDCEA")
    pan.place(x=500,y=350)
    pan_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=pan1)
    pan_entry.place(x=740,y=350)

    aadhar=Label(info_frame,text="AADHAR CARD NO.",font=("times new roman",13,"bold"),bg="#DCDCEA")
    aadhar.place(x=500,y=400)
    aadhar_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=aadhar1)
    aadhar_entry.place(x=740,y=400)
    info_frame.place(x=13,y=140,width=1260,height=575)

    DOR=Label(info_frame,text="DATE OF RELEAVING",font=("times new roman",13,"bold"),bg="#DCDCEA")
    DOR.place(x=500,y=450)
    DOR_entry=Entry(info_frame,state="readonly",font=("times new roman",13,"bold"),bd=3,textvariable=RELEAVING1)
    DOR_entry.place(x=740,y=450)
    info_frame.place(x=13,y=140,width=1260,height=575)
    canvas_for_image = Canvas(info_frame, borderwidth=0, highlightthickness=0)
    canvas_for_image.place(x=1020,y=100,height=150,width=130)
    image = Image.open(r"E:\Camera\IMG20171210125542.jpg")
    canvas_for_image.image = ImageTk.PhotoImage(image.resize((130, 150), Image.ANTIALIAS))
    canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')
    photo_label=Label(info_frame,text="PHOTOGRAPH",font=("times new roman",13,"bold"),bg="#DCDCEA")
    photo_label.place(x=1022,y=260)

    left_end=PhotoImage(file = r"images/teacher profile/left_end.png")
    left_end_btn=Button(info_frame,image=left_end,bg="#DCDCEA",activebackground="#DCDCEA",bd=0,command=insertdata_teacher)
    left_end_btn.photo=left_end
    left_end_label=Label(info_frame,text="First",bg="#DCDCEA",font=("",13,"bold"),fg="#08047C")
    left_end_label.place(x=896,y=540)
    left_end_btn.place(x=900,y=500)

    previous=PhotoImage(file = r"images/teacher profile/previous.png")
    previous_btn=Button(info_frame,image=previous,command=back_btn,bg="#DCDCEA",activebackground="#DCDCEA",bd=0)
    previous_btn.photo=previous
    previous_label=Label(info_frame,text=" Back",bg="#DCDCEA",font=("",13,"bold"),fg="#08047C")
    previous_label.place(x=946,y=540)
    previous_btn.place(x=950,y=500)

    Next=PhotoImage(file = r"images/teacher profile/next.png")
    next_btn=Button(info_frame,image=Next,bg="#DCDCEA",command=next_btn,activebackground="#DCDCEA",bd=0)
    next_btn.photo=Next
    next_label=Label(info_frame,text=" Next",bg="#DCDCEA",font=("",13,"bold"),fg="#08047C")
    next_label.place(x=996,y=540)
    next_btn.place(x=1000,y=500)

    right_end=PhotoImage(file = r"images/teacher profile/right_end.png")
    right_end_btn=Button(info_frame,image=right_end,bg="#DCDCEA",activebackground="#DCDCEA",bd=0,command=insertdata_teacher_LAST)
    right_end_btn.photo=right_end
    right_end_label=Label(info_frame,text=" Last",bg="#DCDCEA",font=("",13,"bold"),fg="#08047C")
    right_end_label.place(x=1050,y=540)
    right_end_btn.place(x=1050,y=500)

def teacher_profile():
    name1=StringVar()
    phone1=StringVar()
    email1=StringVar()
    pan1=StringVar()
    aadhar1=StringVar()
    RELEAVING1=StringVar()
    dob1=StringVar()
    homedis1=StringVar()
    group1=StringVar()
    gender1=StringVar()
    ehrms1=StringVar()
    cadre1=StringVar()
    levelincadre2=StringVar()
    dateofapp1=StringVar()
    dateofjoin1=StringVar()
    dateofcurrent1=StringVar()
    qualification1=StringVar()
    def insertdata_teacher():
        conn = sqlite3.connect('School_data.db')
        cursor = conn.cursor()
        cursor.execute ("""CREATE TABLE IF NOT EXISTS teacher_profile(
        Sn    INTEGER,
        NAME CHAR(25) NOT NULL,
        eHRMS_CODE INT(6),
        DOB CHAR(10),
        CADRE CHAR(20) ,
        LEVEL_IN_CADRE INT(2),
        GENDER CHAR(6),
        HOME_DISTRICT CHAR(20),
        EMPLOYEE_GROUP CHAR(1),
        QUALIFICATION,
        DATE_OF_APPOINTMENT CHAR(10),
        DATE_OF_JOINING CHAR(10),
        DATE_OF_CURRENT_JOINING CHAR(10),
        MOBILE_NO INT(10),
        EMAIL,
        PAN_CARD_NO,
        AADHAR_CARD_NO INT(12),
        DATE_OF_RELEAVING CHAR(10),
        PHOTOGRAPH BLOB)""")
        if name1.get()=="":
            messagebox.showinfo('Entry Requries',"Name entry is requried")
        elif ehrms1.get()=="":
            messagebox.showinfo('Entry Requries',"eHRMS entry is requried")
        elif group1.get()=="":
            messagebox.showinfo('Entry Requries',"GROUP entry is requried")
        elif cadre1.get()=="":
            messagebox.showinfo('Entry Requries',"CADRE entry is requried")
        elif levelincadre2.get()=="":
            messagebox.showinfo('Entry Requries',"LEVEL IN CADRE entry is requried")
        elif gender1.get()=="":
            messagebox.showinfo('Entry Requries',"GENDER entry is requried")
        elif homedis1.get()=="":
            messagebox.showinfo('Entry Requries',"HOME DISTRICT entry is requried")
        elif dob1.get()=="":
            messagebox.showinfo('Entry Requries',"DOB entry is requried")
        elif dateofapp1.get()=="":
            messagebox.showinfo('Entry Requries',"DATE OF APPOINTMENT entry is requried")
        elif dateofjoin1.get()=="":
            messagebox.showinfo('Entry Requries',"DATE OF JOINING entry is requried")
        elif dateofcurrent1.get()=="":
            messagebox.showinfo('Entry Requries',"DATE OF CURRENT JOINING entry is requried")
        elif qualification1.get()=="":
            messagebox.showinfo('Entry Requries',"QUALIFICATION entry is requried")
        elif phone1.get()=="":
            messagebox.showinfo('Entry Requries',"MOBILE NO. entry is requried")
        elif email1.get()=="":
            messagebox.showinfo('Entry Requries'," EMAIL entry is requried")
        elif pan1.get()=="":
            messagebox.showinfo('Entry Requries',"PAN CARD NO. entry is requried")
        elif aadhar1.get()=="":
            messagebox.showinfo('Entry Requries',"AADHAR CARD NO. entry is requried")    
        else:
            conn.execute("insert into teacher_profile (NAME,eHRMS_CODE,DOB,CADRE,LEVEL_IN_CADRE,GENDER,HOME_DISTRICT,EMPLOYEE_GROUP,QUALIFICATION,DATE_OF_APPOINTMENT,DATE_OF_JOINING,DATE_OF_CURRENT_JOINING,MOBILE_NO,EMAIL,PAN_CARD_NO,AADHAR_CARD_NO,DATE_OF_RELEAVING) values('"+name1.get()+"','"+ehrms1.get()+"','"+dob1.get()+"','"+cadre1.get()+"','"+levelincadre2.get()+"','"+gender1.get()+"','"+homedis1.get()+"','"+group1.get()+"','"+qualification1.get()+"','"+dateofapp1.get()+"','"+dateofjoin1.get()+"','"+dateofcurrent1.get()+"','"+phone1.get()+"','"+email1.get()+"','"+pan1.get()+"','"+aadhar1.get()+"','"+RELEAVING1.get()+"')")
            conn.commit()
            conn.close()
            messagebox.showinfo('Save',"Data Saved")
            name1.set("")
            phone1.set("")
            email1.set("")
            pan1.set("")
            aadhar1.set("")
            RELEAVING1.set("")
            dob1.set("")
            homedis1.set("")
            group1.set("")
            gender1.set("")
            ehrms1.set("")
            cadre1.set("")
            levelincadre2.set("")
            dateofapp1.set("")
            dateofjoin1.set("")
            dateofcurrent1.set("")
            qualification1.set("")
    main_frame=Frame(root,bg="green")
    header=Label(main_frame,bg="#86592D",width=1265,height=130)
    header.pack()
    head=Label(header,text=school_name,font=("Algerian",23),bg="#86592D",fg="#fff")
    head.place(x=300,y=13)
    img = PhotoImage(file = r"images/logo.png")
    img_header=Button(header,image=img,bg='#ECD9C6',width=400,height=128,border=0)
    img_header.photo=img
    img_header.place(x=900,y=0)
    main_frame.place(x=0,y=0,height=130)
    info_frame=Frame(root,bg="#DCDCEA")
    imgback = PhotoImage(file = r"images/home/back.png")
    backbtn=Button(info_frame,image=imgback,bg="#DCDCEA",
                   activebackground="#23707B",border=0)
    backbtn.photo=imgback
    backbtn.place(x=20,y=20)
    h1=Label(info_frame,text="Personal Information:",font=("times new roman",17,"bold","underline"),bg="#DCDCEA")
    h1.place(x=460,y=30)
    name=Label(info_frame,text="NAME",font=("times new roman",13,"bold"),bg="#DCDCEA")
    name.place(x=50,y=100)
    name_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=name1)
    name_entry.place(x=260,y=100)
    
    ehrms=Label(info_frame,text="eHRMS CODE",font=("times new roman",13,"bold"),bg="#DCDCEA")
    ehrms.place(x=50,y=150)
    ehrms_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=ehrms1)
    ehrms_entry.place(x=260,y=150)

    cal=DateEntry(info_frame,textvariable=dob1,font=("",13,"bold"),date_pattern="dd/MM/yyyy",firstweekday="sunday",background="dark blue",showothermonthdays=False,
                   weekendbackground="white",weekendforeground="red")
    cal.place(x=260,y=200,width=190,height=30)
    dob=Label(info_frame,text="DOB",font=("times new roman",13,"bold"),bg="#DCDCEA")
    dob.place(x=50,y=200)

    cadre=Label(info_frame,text="CADRE",font=("times new roman",13,"bold"),bg="#DCDCEA")
    cadre.place(x=50,y=250)
    cadre_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=cadre1)
    cadre_entry.place(x=260,y=250)
    
    levelincarder=Label(info_frame,text="LEVEL IN CADRE",font=("times new roman",13,"bold"),bg="#DCDCEA")
    levelincarder.place(x=50,y=300)
    levelincarder_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=levelincadre2)
    levelincarder_entry.place(x=260,y=300)
    
    gender=Label(info_frame,text="GENDER",font=("times new roman",13,"bold"),bg="#DCDCEA")
    gender.place(x=50,y=350)
    combobox= Combobox(info_frame,state="readonly", font=("times new roman",13,"bold"),textvariable=gender1)
    items=("Male","Female")
    combobox["values"]=items
    combobox.set('-----Select Gender-----')
    combobox.place(x=260,y=350,width=190)


    homedic=Label(info_frame,text="HOME DISTRICT",font=("times new roman",13,"bold"),bg="#DCDCEA")
    homedic.place(x=50,y=400)
    homedic_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=homedis1)
    homedic_entry.place(x=260,y=400)

    group=Label(info_frame,text="GROUP",font=("times new roman",13,"bold"),bg="#DCDCEA")
    group.place(x=50,y=450)
    group_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=group1)
    group_entry.place(x=260,y=450)

    qualification=Label(info_frame,text="QUALIFICATION",font=("times new roman",13,"bold"),bg="#DCDCEA")
    qualification.place(x=50,y=500)
    qualification_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=qualification1)
    qualification_entry.place(x=260,y=500)

    date_appo=Label(info_frame,text="DATE OF APPOINTMENT",font=("times new roman",13,"bold"),bg="#DCDCEA")
    date_appo.place(x=500,y=100)
    date_appo_entry=DateEntry(info_frame,textvariable=dateofapp1,font=("",13,"bold"),date_pattern="dd/MM/yyyy",firstweekday="sunday",background="dark blue",showothermonthdays=False,
                   weekendbackground="white",weekendforeground="red")
    date_appo_entry.place(x=740,y=100,width=190,height=30)

    date_join=Label(info_frame,text="DATE OF JOINING",font=("times new roman",13,"bold"),bg="#DCDCEA")
    date_join.place(x=500,y=150)
    date_join_entry=DateEntry(info_frame,textvariable=dateofjoin1,font=("",13,"bold"),date_pattern="dd/MM/yyyy",firstweekday="sunday",background="dark blue",showothermonthdays=False,
                   weekendbackground="white",weekendforeground="red")
    date_join_entry.place(x=740,y=150,width=190,height=30)

    date_current=Label(info_frame,text="DATE OF CURRENT JOINING",font=("times new roman",13,"bold"),bg="#DCDCEA")
    date_current.place(x=500,y=200)
    date_current_entry=DateEntry(info_frame,textvariable=dateofcurrent1,font=("",13,"bold"),date_pattern="dd/MM/yyyy",firstweekday="sunday",background="dark blue",showothermonthdays=False,
                   weekendbackground="white",weekendforeground="red")
    date_current_entry.place(x=740,y=200,width=190,height=30)



    mobile=Label(info_frame,text="MOBILE NO.",font=("times new roman",13,"bold"),bg="#DCDCEA")
    mobile.place(x=500,y=250)
    mobile_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=phone1)
    mobile_entry.place(x=740,y=250)

    email=Label(info_frame,text="EMAIL",font=("times new roman",13,"bold"),bg="#DCDCEA")
    email.place(x=500,y=300)
    email_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=email1)
    email_entry.place(x=740,y=300)	

    pan=Label(info_frame,text="PAN CARD NO.",font=("times new roman",13,"bold"),bg="#DCDCEA")
    pan.place(x=500,y=350)
    pan_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=pan1)
    pan_entry.place(x=740,y=350)

    aadhar=Label(info_frame,text="AADHAR CARD NO.",font=("times new roman",13,"bold"),bg="#DCDCEA")
    aadhar.place(x=500,y=400)
    aadhar_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=aadhar1)
    aadhar_entry.place(x=740,y=400)
    info_frame.place(x=13,y=140,width=1260,height=575)

    DOR=Label(info_frame,text="DATE OF RELEAVING",font=("times new roman",13,"bold"),bg="#DCDCEA")
    DOR.place(x=500,y=450)
    DOR_entry=Entry(info_frame,font=("times new roman",13,"bold"),bd=3,textvariable=RELEAVING1)
    DOR_entry.place(x=740,y=450)
    info_frame.place(x=13,y=140,width=1260,height=575)

    canvas_for_image = Canvas(info_frame, borderwidth=0, highlightthickness=0)
    canvas_for_image.place(x=1020,y=100,height=150,width=130)
    image = Image.open(r"images/Home.png")
    canvas_for_image.image = ImageTk.PhotoImage(image.resize((130, 150), Image.ANTIALIAS))
    canvas_for_image.create_image(0, 0, image=canvas_for_image.image, anchor='nw')
    photo_label=Label(info_frame,text="PHOTOGRAPH",font=("times new roman",13,"bold"),bg="#DCDCEA")
    photo_label.place(x=1022,y=260)
    photo_button=Button(info_frame,text="Browse",font=("",13,"bold"),bg="#DEB23C")
    photo_button.bind("<Enter>",lambda b:photo_button.configure(background="green"))
    photo_button.bind("<Leave>",lambda b:photo_button.configure(background="#DEB23C"))
    photo_button.place(x=1160,y=220)
    add_button=Button(info_frame,text="Add Profile",bg="#DEB23C",font=("",20),command=insertdata_teacher)
    add_button.place(x=500,y=500,height=40)
    add_button.bind("<Enter>",lambda b:add_button.configure(background="green"))
    add_button.bind("<Leave>",lambda b:add_button.configure(background="#DEB23C"))
    view_button=Button(info_frame,text="Show List",bg="#DEB23C",font=("",20),command=teacher_view_all)
    view_button.place(x=1034,y=500,height=40)
    view_button.bind("<Enter>",lambda b:view_button.configure(background="green"))
    view_button.bind("<Leave>",lambda b:view_button.configure(background="#DEB23C"))
    update_button=Button(info_frame,text="Update profile",bg="#DEB23C",font=("",20))
    update_button.place(x=837,y=500,height=40)
    update_button.bind("<Enter>",lambda b:update_button.configure(background="green"))
    update_button.bind("<Leave>",lambda b:update_button.configure(background="#DEB23C"))
    showindividual_button=Button(info_frame,text="Show profile",bg="#DEB23C",font=("",20),command=show_profile)
    showindividual_button.place(x=660,y=500,height=40)
    showindividual_button.bind("<Enter>",lambda b:showindividual_button.configure(background="green"))
    showindividual_button.bind("<Leave>",lambda b:showindividual_button.configure(background="#DEB23C"))
def back_button():
     teacher_profile()


def teacher_view_all():
    def View():
        conn = sqlite3.connect("School_data.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM teacher_profile")
        rows = cur.fetchall()
        for row in rows:
            teacher_profile.insert("",END, values=row)
            conn.close()
        b2.destroy()
        b3 = Button(text="Back",command=back_button)
        b3.place(x=1160,y=210,width=90,height=40)


    teacher_view_all=Frame(root)
    main_frame=Frame(root,bg="green")
    header=Label(main_frame,bg="#86592D",width=1265,height=130)
    header.pack()
    head=Label(header,text=school_name,font=("Algerian",23),bg="#86592D",fg="#fff")
    head.place(x=300,y=13)
    img = PhotoImage(file = r"images/logo.png")
    img_header=Button(header,image=img,bg='#ECD9C6',width=400,height=128,border=0)
    img_header.photo=img
    img_header.place(x=900,y=0)
    main_frame.place(x=0,y=0,height=130)
    tableframe5=Frame(root,bd=4,relief=RIDGE,bg="#DCDCEA")
    scroll_x=Scrollbar(tableframe5,orient=HORIZONTAL)
    scroll_y=Scrollbar(tableframe5,orient=VERTICAL)
    teacher_profile= ttk.Treeview(tableframe5,height=500, column=("column", "colunn1","colunn2", "colunn3", "colunn4", "colunn5", "colunn6", "colunn7", "colunn8", "colunn9", "colunn10", "colunn11", "colunn12", "colunn13", "colunn14", "colunn15", "colunn16", "colunn17","colunn18",),yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
    scroll_x.config(command=teacher_profile.xview)
    scroll_y.config(command=teacher_profile.yview)
    teacher_profile.column("#0",anchor="n")
    teacher_profile.column("#1",anchor="n")
    teacher_profile.column("#2",anchor="n")
    teacher_profile.column("#3",anchor="n")
    teacher_profile.column("#4",anchor="n")
    teacher_profile.column("#5",anchor="n")
    teacher_profile.column("#6",anchor="n")
    teacher_profile.column("#7",anchor="n")
    teacher_profile.column("#8",anchor="n")
    teacher_profile.column("#9",anchor="n")
    teacher_profile.column("#10",anchor="n")
    teacher_profile.column("#11",anchor="n")
    teacher_profile.column("#12",anchor="n")
    teacher_profile.column("#13",anchor="n")
    teacher_profile.column("#14",anchor="n")
    teacher_profile.column("#15",anchor="n")
    teacher_profile.column("#16",anchor="n")
    teacher_profile.column("#17",anchor="n")
    teacher_profile.column("#18",anchor="n")
    scroll_x.pack(side=BOTTOM,fill="x")
    scroll_y.pack(side=RIGHT,fill="y")
    teacher_profile.heading("#0",text="")
    teacher_profile.heading("#1",text="S no.")
    teacher_profile.heading("#2", text="NAME")
    teacher_profile.heading("#3", text="eHRMS CODE")
    teacher_profile.heading("#4", text="DOB")
    teacher_profile.heading("#5", text="CADRE")
    teacher_profile.heading("#6", text="LEVEL IN CADRE")
    teacher_profile.heading("#7", text="GENDER")
    teacher_profile.heading("#8", text="HOME DISTRICT")
    teacher_profile.heading("#9", text="GROUP")
    teacher_profile.heading("#10", text="QUALIFICATION")
    teacher_profile.heading("#11", text="DATE OF APPOINTMENT")
    teacher_profile.heading("#12", text="DATE OF JOINING")
    teacher_profile.heading("#13", text="DATE OF CURRENT JOINING")
    teacher_profile.heading("#14", text="MOBILE NO")
    teacher_profile.heading("#15", text="EMAIL")
    teacher_profile.heading("#16", text="PAN CARD NO")
    teacher_profile.heading("#17", text="AADHAR CARD NO")
    teacher_profile.heading("#18", text="'DATE OF RALEVING")
    teacher_profile.pack()
    teacher_profile.pack(side=TOP)
    tableframe5.place(x=30,y=200,width=1100,height=500)
    b2 = Button(text="view data", command=View)
    b2.place(x=1160,y=210,width=90,height=40)
##    back_btn = Button(text="Back", command=teacher_profile)
##    back_btn.place(x=1160,y=190,width=90,height=40)
    teacher_view_all.place(x=0,y=0,width=1280,height=727)
teacher_profile()
root.mainloop()
