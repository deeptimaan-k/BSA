from tkinter import *
import sqlite3
from tkinter import StringVar
cr = sqlite3.connect('student_managmant.db')
cr = cr.cursor()
cursor.execute("DROP TABLE IF EXISTS teacher_profile")
sql ='''CREATE TABLE teacher_profile('NAME','DOB','HOMEDIS','GROUP','GENDER',
                                                      'eHRMS CODE','CADRE',
                                                      'LEVEL IN CADRE',
                                                      'DATE OF APPOINTMENT','DATE OF JOINING',
                                                      'DATE OF CURRENT SCHOOL JOINING','QUALIFICATION','PHOTO','MOBILE','EMAIL','PANNO','AADHAR NO','DATE OF RELEAVING')'''
cr.execute("select * from login where NAME='"+name.get()+"',DOB='"+dob.get+"',HOMEDIS='"+homedis.get()+"',GROUP='"+group.get()+"',GENDER='"+gender.get()+"',eHRMS CODE='"+ehrms.get()+"',CADRE='"+cadre.get()+"',LEVEL IN CADRE='"+levelincadre.get()+"',DATE OF APPOINTMENT='"+dateofapp.get()+"',DATE OF JOINING='"+dateofjoin.get()+"',DATE OF CURRENT SCHOOL JOINING='"+dateofcurrent.get()+"',QUALIFICATION='"+qualification.get()+"',PANNO='"+pan.get()+"',AADHAR='"+aadhar.get()+"',PHOTO='"+photo.get()+"',EMAIL='"+email.get()+"',DATE OF RELEAVING="+RELEAVING.get()+"',PHONE='"+phone.get()+"' ")
print("Table created successfully........")
cr.commit()
cr.close()
name=StringVar()
phone=StringVar()
email=StringVar()
photo=StringVar()
pan=StringVar()
aadhar=StringVar()
RELEAVING=StringVar()
dob=StringVar()
homedis=StringVar()
group=StringVar()
gender=StringVar()
ehrms=StringVar()
cadre=StringVar()
levelincadre=StringVar()
dateofapp=StringVar()
dateofjoin=StringVar()
dateofcurrent=StringVar()
qualification=StringVar()

s_name=Label(home_frame1,text="Student's name:",font=("times new roman",12,"bold"),bg="white")
    s_name.grid(row=1,column=0,padx=10,pady=15)
    f_name=Label(home_frame1,text="Father's name:",font=("times new roman",12,"bold"),bg="white")
    f_name.grid(row=2,column=0,padx=10,pady=5)
    f_oc=Label(home_frame1,text="Father's Occupation:",font=("times new roman",12,"bold"),bg="white")
    f_oc.grid(row=2,column=2,padx=10,pady=5)
    m_name=Label(home_frame1,text="Mothers's name:",font=("times new roman",12,"bold"),bg="white")
  
    m_name.grid(row=3,column=0,padx=10,pady=5)
    m_oc=Label(home_frame1,text="Mothers's occupation:",font=("times new roman",12,"bold"),bg="white")
  
    m_oc.grid(row=3,column=2,padx=10,pady=5)
      # imgadd=Entry(home_frame,width=25,font=("times new roman",15,"bold"),borderwidth=5,textvariable=photoo)
    #imgadd.grid(row=12,column=2,pady=5)
    aadhar=Label(home_frame1,text="Aadhar No.",font=("times new roman",12,"bold"),bg="white")
    aadhar.grid(row=7,column=0,padx=10,pady=5)
    phone=Label(home_frame1,text="Mobile no.:",font=("times new roman",12,"bold"),bg="white")
    phone.grid(row=1,column=2,padx=10,pady=5)
    Class=Label(home_frame1,text="Class:",font=("times new roman",12,"bold"),bg="white")
    Class.grid(row=4,column=0,padx=10,pady=5)
    sr_no=Label(home_frame1,text="Serial No:",font=("times new roman",12,"bold"),bg="white")
    sr_no.grid(row=5,column=0,padx=10,pady=5) 
    bg=Label(home_frame1,text="Blood Group:",font=("times new roman",12,"bold"),bg="white")
    bg.grid(row=11,column=0,padx=10,pady=5) 
    
    gender=Label(home_frame1,text="Gender:",font=("times new roman",12,"bold"),bg="white")
    gender.grid(row=8,column=0,padx=10,pady=5) 
    cast=Label(home_frame1,text="Cast:",font=("times new roman",12,"bold"),bg="white")
    cast.grid(row=10,column=0,padx=10,pady=5)
    category=Label(home_frame1,text="Category:",font=("times new roman",12,"bold"),bg="white")
    category.grid(row=9,column=0,padx=10,pady=5) 
    cwsn=Label(home_frame1,text="CWSN:",font=("times new roman",12,"bold"),bg="white")
    cwsn.grid(row=4,column=2,padx=10,pady=5)
    address=Label(home_frame1,text="Address:",font=("times new roman",12,"bold"),bg="white")
    address.grid(row=5,column=2,padx=10,pady=5) 
    doblabel=Label(home_frame1,text="D.O.B:",font=("times new roman",12,"bold"),bg="white")
    doblabel.grid(row=6,column=0,padx=10,pady=5)
    doalabel=Label(home_frame1,text="D.O.A:",font=("times new roman",12,"bold"),bg="white")
    doalabel.grid(row=6,column=2,padx=10,pady=5)
    doelabel=Label(home_frame1,text="D.O.E:",font=("times new roman",12,"bold"),bg="white")
    doelabel.grid(row=7,column=2,padx=10,pady=5)
    
    s_name_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),textvariable=sname,borderwidth=5)
    s_name_entry.grid(row=1,column=1,pady=5)
    
    f_name_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),textvariable=fname,borderwidth=5)
    f_name_entry.grid(row=2,column=1,pady=5)
    
    f_oc_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),textvariable=foc,borderwidth=5)
    f_oc_entry.grid(row=2,column=3,pady=5)
    
    m_name_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=mname)
    m_name_entry.grid(row=3,column=1,pady=5)
    m_oc_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=moc)
    m_oc_entry.grid(row=3,column=3,pady=5)
    
    Class_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=cl)
    Class_entry.grid(row=4,column=1,pady=5)
    
    sr_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=adm)
    sr_entry.grid(row=5,column=1,pady=5)
    
    bg_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=bg)
    bg_entry.grid(row=11,column=1,pady=5)
    
    gender_combo=ttk.Combobox(home_frame1,width=23,font=("times new roman",12,"bold"),textvariable=gend)
    gender_combo['values']=("Male","Female","Other")
    gender_combo.grid(row=8,column=1,pady=5)
    
    cwsn_combo=ttk.Combobox(home_frame1,width=23,font=("times new roman",12,"bold"),textvariable=cwsn)
    cwsn_combo['values']=("PH","VH")
    cwsn_combo.grid(row=4,column=3,pady=5)
    
    category_combo=ttk.Combobox(home_frame1,width=23,font=("times new roman",12,"bold"),textvariable=cat)
    category_combo['values']=("General","OBC","SC","ST","Other")
    category_combo.grid(row=9,column=1,pady=5)
    
    cast_combo=ttk.Combobox(home_frame1,width=23,font=("times new roman",12,"bold"),textvariable=cast)
    cast_combo['values']=("Male","Female","Other")
    cast_combo.grid(row=10,column=1,pady=5)
    
    
    
    aadhar_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=aadhar)
    aadhar_entry.grid(row=7,column=1,pady=5)
    
    mobile_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=mn)
    mobile_entry.grid(row=1,column=3,pady=5)
    
    address_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=addr)
    address_entry.grid(row=5,column=3,pady=5)
    # imgadd=Entry(anf,width=25,font=("times new roman",15,"bold"),borderwidth=5,textvariable=photoo)
    # imgadd.grid(row=12,column=2,pady=5)
    
    dob_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=dob)
    dob_entry.grid(row=6,column=1,pady=5)
    
    # chooselabel=Label(home_frame1,text="Student image:",bg="white",font=("times new roman",12,"bold"))
    # chooselabel.grid(row=12,column=0,pady=5,padx=10)
    # changebtn=Button(home_frame1,text="Change photo",relief=RIDGE,font=("times new roman",12,"bold"),borderwidth=5,bg="green",command=imgchoose)
    # changebtn.grid(row=4,column=8,pady=5)
    
    closebtn=Button(home_frame1,text="Close",bg="green",relief=RIDGE,borderwidth=5,font=("times new roman",12,"bold"))
    closebtn.grid(row=13,column=2,ipadx=50,pady=22)
    
    
    
    doalabel=Label(home_frame1,text="D.O.A:",font=("times new roman",12,"bold"),bg="white")
    doalabel.grid(row=6,column=2,padx=10,pady=5)
    doelabel=Label(home_frame1,text="D.O.E:",font=("times new roman",12,"bold"),bg="white")
    doelabel.grid(row=7,column=2,padx=10,pady=5)
    doa_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=doa)
    doa_entry.grid(row=6,column=3,pady=5)
    doe_entry=Entry(home_frame1,width=25,font=("times new roman",12,"bold"),borderwidth=5,textvariable=doe)
    doe_entry.grid(row=7,column=3,pady=5)
    img_profile = PhotoImage(file = r"images/report_card.png")
    updatebtn=Button(home_frame1,bg="white",border=0,activebackground="green",image=img_profile)
    updatebtn.photo=img_profile
    updatebtn.place(x=870,y=300)
    update=Label(home_frame1,text="Academic Record",bg="white",font=("times new roman",12,"bold"),fg="black").place(x=880,y=430)
        


    
    
    
    
    
    
def teacher_profile():
    home_frame=Frame(root,bg="white")
    home_frame.place(x=0,y=0,width=1265,height=722)
    home_in_img=PhotoImage(file=r"images/passout/show2.png")
    home_in=Label(image=home_in_img,bg="#86592D",width=130)
    home_in.photo=home_in_img
    home_in.place(x=30,y=15)
    header=Frame(home_frame,bg="#86592D",width=1265,height=130).pack()
    head=Label(header,text='        P.S. CHANDPUR JOGITHER', fg="#fff",bg="#86592D",
               font=("Algerian",35)).place(x=150,y=30)
    img = PhotoImage(file = r"images/logo.png")
    img_header=Button(header,image=img,bg='#ECD9C6',width=400,height=128,border=0)
    img_header.photo=img
    img_header.place(x=900,y=0)
    imgback = PhotoImage(file = r"images/home/back.png")
    backbtn=Button(home_frame,command=passout,image=imgback,bg="white",
                   activebackground="white",border=0)
    backbtn.photo=imgback
    backbtn.place(x=10,y=130)
    home_frame1=Frame(home_frame,bg="white",padx=60,pady=20)
    home_frame1.place(x=60,y=130,width=1200,height=600)
    
    
    
    searchb=Button(home_frame1,text="Show All",font=("times new roman",12,"bold"),borderwidth=5,bg="green")
    searchb.grid(row=0,column=2,ipadx=50,padx=400,pady=10,columnspan=4)
    tableframe5=Frame(home_frame1,bd=4,relief=RIDGE,bg="white")
    tableframe5.place(x=40,y=60,width=970,height=500)
    scroll_x=Scrollbar(tableframe5,orient=HORIZONTAL)
    scroll_y=Scrollbar(tableframe5,orient=VERTICAL)
    student_table=ttk.Treeview(tableframe5,height=25,columns=("SR no.","Name","Father's name","Mother's name","Class","Aadhar no.","D.O.B","D.O.A","D.O.E","Gender","Category","Cast","Father's occupation","Mother's occupation","Mobile no.","CWSN","Blood Group","Address","Academic Record","Image address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
    #student_table=ttk.Treeview(tableframe5,columns=(1,2,3,4,5,6,7,8,9,10,11,12),show ="headings")
    scroll_x.pack(side=BOTTOM,fill="x")
    scroll_y.pack(side=RIGHT,fill="y")
    scroll_x.config(command=student_table.xview)
    scroll_y.config(command=student_table.yview)
    student_table.heading("SR no.",text="Sr No.")
    student_table.heading("Name",text="Name")
    student_table.heading("Father's name",text="Father's name")
    student_table.heading("Mother's name",text="Mother's name")
    student_table.heading("Father's occupation",text="Father's occupation")
    student_table.heading("Mother's occupation",text="Mother's occupation")
    student_table.heading("Class",text="Class")
    student_table.heading("Gender",text="Gender")
    student_table.heading("Cast",text="Cast")
    student_table.heading("Category",text="Category")
    student_table.heading("Aadhar no.",text="Aadhar no.")
    student_table.heading("D.O.B",text="D.O.B")
    student_table.heading("D.O.A",text="D.O.A")
    student_table.heading("D.O.E",text="D.O.E")
    student_table.heading("Mobile no.",text="Mobile no.")
    student_table.heading("Address",text="Address")
    student_table.heading("CWSN",text="CWSN")
    student_table.heading("Blood Group",text="Blood Group")
    student_table.heading("Academic Record",text="Academic Record")
    student_table.heading("Image address",text="Image address")
    student_table.pack(side=TOP)
teacher_profile()

