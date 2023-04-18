
def addstudent():

    def submitadd():
        id=idval.get()
        name=nameval.get()
        mobile=mobileval.get()
        email=emailval.get()
        address=genderval.get()
        gender=addessval.get()
        dob=dobval.get()
        addtime=time.strftime("%H:%M:%S")
        adddate=time.strftime("%d/%m/%Y")
        try:
            query = 'insert into studentdata values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(query,(id,name,mobile,email,address,gender,dob,adddate,addtime))
            con.commit()
            res=messagebox.askyesnocancel('Notification','Id {} Name {} Added sucessfully.. and want to clean the from'.format(id,name),parent=addroot)
            if(res==True):
                    idval.set('')
                    nameval.set('')
                    mobileval.set('')
                    emailval.set('')
                    genderval.set('')
                    addessval.set('')
                    dobval.set('')
        except:
            messagebox.showerror('Notification','Id Already Exits try another id ...',parent=addroot)
        query='select * from studentdata'
        cur.execute(query)
        datas=cur.fetchall()
        # previous data hide ,current data show
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            list=[i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8]]
            # data insert start to end 
            studenttable.insert('',END,values=list)
        

    addroot=Toplevel(master=DataEntryFrame)
    # for attention current window (   addroot.grab_set() )
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('student management system')
    addroot.config(bg='blue')
    addroot.resizable(False,False)

    #----------------------- add student label-----------

    idlabel=Label(addroot,text='Enter ID',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(addroot,text='Enter NAME',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(addroot,text='Enter MOBILE',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(addroot,text='Enter EMAIL',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(addroot,text='Enter ADDREES',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(addroot,text='Enter GENDER',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)


    doblabel=Label(addroot,text='Enter D.O.B',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)
# --------------------------------- ADD student entry---------------

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    genderval=StringVar()
    addessval=StringVar()
    dobval=StringVar()

    identry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addessentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    addessentry.place(x=250,y=250)

    gederentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addessval)
    gederentry.place(x=250,y=310)

    dobentry=Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    # -------------------- add Button ----------

    submitbtn=Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',command=submitadd)
    submitbtn.place(x=150,y=420)


    addroot.mainloop()

def searchstudent():
   
    def search():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addessval.get()
        gender = genderval.get()
        dob = dobval.get()
        addeddate = time.strftime("%d/%m/%Y")
        if(id != ''):
            query = 'select *from studentdata where id=%s'
            cur.execute(query,(id))
            datas = cur.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=list)
        elif(name != ''):
            query = 'select *from studentdata where name=%s'
            cur.execute(query,(name))
            datas = cur.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=list)
        elif(mobile != ''):
            query = 'select *from studentdata where mobile=%s'
            cur.execute(query,(mobile))
            datas = cur.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=list)
        elif(email != ''):
            query = 'select *from studentdata where email=%s'
            cur.execute(query,(email))
            datas = studenttable.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=list)
        elif(address != ''):
            query = 'select *from studentdata where address=%s'
            cur.execute(query,(address))
            datas = cur.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=list)
        elif(gender != ''):
            query = 'select *from studentdata where gender=%s'
            cur.execute(query,(gender))
            datas = cur.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=list)
        elif(dob != ''):
            query = 'select *from studentdata where dob=%s'
            cur.execute(query,(dob))
            datas = cur.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=list)

        elif(addeddate != ''):
            query = 'select *from studentdata where addeddate=%s'
            cur.execute(query,(addeddate))
            datas = cur.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                studenttable.insert('', END, values=list)


    searchroot=Toplevel(master=DataEntryFrame,)
    searchroot.grab_set()
    searchroot.geometry('470x540+220+200')
    searchroot.title('student management system')
    searchroot.config(bg='firebrick1')
    searchroot.resizable(False,False)

    #----------------------- add student label-----------
    idlabel=Label(searchroot,text='Enter ID',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(searchroot,text='Enter NAME',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(searchroot,text='Enter MOBILE',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(searchroot,text='Enter EMAIL',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(searchroot,text='Enter ADREES',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(searchroot,text='Enter GENDER',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)


    doblabel=Label(searchroot,text='Enter D.O.B',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(searchroot,text='Enter date',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)
# --------------------------------- ADD student entry---------------

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    genderval=StringVar()
    addessval=StringVar()
    dobval=StringVar()
    dateval=StringVar()

    identry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addessentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    addessentry.place(x=250,y=250)

    gederentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=addessval)
    gederentry.place(x=250,y=310)

    dobentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry=Entry(searchroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    # -------------------- add Button -----

    submitbtn=Button(searchroot,text='Search',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',command=search)
    submitbtn.place(x=150,y=480)


    searchroot.mainloop()

def deletestudent():
    # giving the index no .
    index_no = studenttable.focus()
    # fetch the content
    content = studenttable.item(index_no)
    first_value = content['values'][0]
    query= "delete from studentdata where id='{}'".format(first_value)
    cur.execute(query)
    # query = 'delete from studentdata where id=%s'
    # cur.execute(query,(pp))
    con.commit()
    messagebox.showinfo('Notifications','Id {} deleted sucessfully...'.format(first_value))
    query = 'select * from studentdata'
    cur.execute(query)
    datas = cur.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=list)
   


def upadtestudent():
   
    def update():
        id = idval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addessval.get()
        gender = genderval.get()
        dob = dobval.get()
        date = dateval.get()
        time = timeval.get()

        query = 'update studentdata set name=%s,mobile=%s,email=%s,address=%s,gender=%s,dob=%s,date=%s,time=%s where id=%s'
        cur.execute(query,(name,mobile,email,address,gender,dob,date,time,id))
        con.commit()
        messagebox.showinfo('Notifications', 'Id {} Modified sucessfully...'.format(id),parent=updateroot)
        query = 'select *from studentdata'
        cur.execute(query)
        datas = cur.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            studenttable.insert('', END, values=list)
       

    updateroot=Toplevel(master=DataEntryFrame,)
    updateroot.grab_set()
    updateroot.geometry('470x585+220+120')
    updateroot.title('student management system')
    updateroot.config(bg='firebrick1')
    updateroot.resizable(False,False)
    #----------------------- add student label-----------
    idlabel=Label(updateroot,text='Enter ID',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    idlabel.place(x=10,y=10)

    namelabel=Label(updateroot,text='Enter NAME',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)

    mobilelabel=Label(updateroot,text='Enter MOBILE',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)

    emaillabel=Label(updateroot,text='Enter EMAIL',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)

    addresslabel=Label(updateroot,text='Enter ADREES',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    
    genderlabel=Label(updateroot,text='Enter GENDER',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)


    doblabel=Label(updateroot,text='Enter D.O.B',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    doblabel.place(x=10,y=370)

    datelabel=Label(updateroot,text='Enter date',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    datelabel.place(x=10,y=430)

    timelabel=Label(updateroot,text='Enter Time',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    timelabel.place(x=10,y=490)
# --------------------------------- ADD student entry---------------

    idval=StringVar()
    nameval=StringVar()
    mobileval=StringVar()
    emailval=StringVar()
    genderval=StringVar()
    addessval=StringVar()
    dobval=StringVar()
    dateval=StringVar()
    timeval=StringVar()

    identry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=idval)
    identry.place(x=250,y=10)

    nameentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)

    mobileentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)

    emailentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)

    addessentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    addessentry.place(x=250,y=250)

    gederentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=addessval)
    gederentry.place(x=250,y=310)

    dobentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dobval)
    dobentry.place(x=250,y=370)

    dateentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    dateentry.place(x=250,y=430)

    timeentry=Entry(updateroot,font=('roman',15,'bold'),bd=5,textvariable=dateval)
    timeentry.place(x=250,y=490)

    # -------------------- add Button -----

    submitbtn=Button(updateroot,text='Update',font=('roman',15,'bold'),width=20,bd=5,activebackground='blue',activeforeground='white',command=update)
    submitbtn.place(x=150,y=535)

    index_no = studenttable.focus()
    content = studenttable.item(index_no)
    data = content['values']
    if(len(data) != 0):
        idval.set(data[0])
        nameval.set(data[1])
        mobileval.set(data[2])
        emailval.set(data[3])
        addessval.set(data[4])
        genderval.set(data[5])
        dobval.set(data[6])
        dateval.set(data[7])
        timeval.set(data[8])


    updateroot.mainloop()

def showstudent():
    strr = 'select * from studentdata'
    cur.execute(strr)
    datas = cur.fetchall()
    studenttable.delete(*studenttable.get_children())
    for i in datas:
        list = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        studenttable.insert('', END, values=list)

def exporttudent():
    
    # give the index no
    index_no = studenttable.get_children() 
   
    id=[]
    name=[]
    mobile=[]
    email=[]
    address=[]
    gender=[]
    dob=[]
    addeddate=[]
    addedtime=[]

    for i in index_no:
        # three type of data values,image,text
        row_data = studenttable.item(i)
        data = row_data['values']
        id.append(data[0]),name.append(data[1]),mobile.append(data[2]),email.append(data[3]),address.append(data[4]),gender.append(data[5]),
        dob.append(data[6]),addeddate.append(data[7]),addedtime.append(data[8])

    # heading in excel
    heading = ['Id','Name','Mobile','Email','Address','Gender','D.O.B','Added Date','Added Time']

    data_f = pandas.DataFrame(list(zip(id,name,mobile,email,address,gender,dob,addeddate,addedtime)),columns=heading)
    
    # give the path to store data
    path = filedialog.asksaveasfilename()
    # csv=comma seperated value
    paths = r'{}.csv'.format(path)
    data_f.to_csv(paths,index=False)
    messagebox.showinfo('Notifications', 'Student data is Saved {}'.format(paths))

def exitstudent():
    res=messagebox.askyesnocancel('Notification','Do you want exit')
    if(res==True):
        root.destroy()

def connectdb():

    def submitdb():
        # for entire use variables (global con,mycursor)
        global con,cur
        host=Hostval.get()
        user=Userval.get()
        password=Passwordval.get()

        try:
            con=pymysql.connect(host=host,user=user,password=password)
            cur=con.cursor()
        except:
            messagebox.showerror('Notification ','Data is incorrect please try again ')
            return
        try:
            query='create database std'
            cur.execute(query)
            query='use std'
            cur.execute(query)
            query='create table if not exists studentdata(id int primary key,name varchar(20),mobile varchar(20),email varchar(20),address varchar(20),gender varchar(20),dob varchar(20),date varchar(20),time varchar(20))'
            cur.execute(query)
            messagebox.showinfo('Notification',' database create and Now you are connect to the database',parent=dbroot)
        except:
            query='use std'
            cur.execute(query)
            messagebox.showinfo('Notification','Now you are connect to the database',parent=dbroot)
        # for any problem back exit
        dbroot.destroy()

    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry("470x250+800+230")
    dbroot.resizable(False,False)
    dbroot.config(bg='blue')

    #---------------------- Connection Labels  ----------------
    Hostlabel=Label(dbroot,text='Enter Host :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Hostlabel.place(x=10,y=10)

    Userlabel=Label(dbroot,text='Enter User :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Userlabel.place(x=10,y=85)

    Passwordlabel=Label(dbroot,text='Enter Password :',bg='gold2',font=('times',20,'bold'),relief=GROOVE,borderwidth=3,width=12,anchor='w')
    Passwordlabel.place(x=10,y=150)
 


    #-------------------------- Connect DB Entry  ---------------------

    Hostval=StringVar()
    Userval=StringVar()
    Passwordval=StringVar()


    HostEntry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=Hostval)
    HostEntry.place(x=250,y=10)

    UserEntry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=Userval)
    UserEntry.place(x=250,y=85)

    PasswordEntry=Entry(dbroot,font=('roman',15,'bold'),bd=5,textvariable=Passwordval)
    PasswordEntry.place(x=250,y=150)


    submitbutton=Button(dbroot,text='submit',font=('roman',15,'bold'),bg=
    'red',bd=5,width=20,activebackground='blue',activeforeground='white',command=submitdb)
    submitbutton.place(x=150,y=200)

    dbroot.mainloop()

def tick():
    time_string=time.strftime("%H:%M:%S")
    date_string=time.strftime("%d/%m/%y")
    clock.config(text="Date :"+date_string+'\n'+'Time :'+time_string)
    clock.after(200,tick)

# color=['red','black','white','pink','green','blue','gold2']
color=['white']
def introLabelcolorTick():
    fg=random.choice(color)
    SlideLabel.config(fg=fg)
    SlideLabel.after(5,introLabelcolorTick)


def IntroLabelTick():
    global count,text
    if(count>=len(ss)):
        count=0
        text=''
        SlideLabel.config(text=text)
    else:
        text=text+ss[count]
        SlideLabel.config(text=text)
        count+=1
    SlideLabel.after(50,IntroLabelTick)

#------------------- This is module part  --------------# 

from tkinter import *
from PIL import Image,ImageTk
from tkinter import Toplevel,messagebox,filedialog
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import random
import pandas
import time

##---------------------  Screen  -------------##
root=Tk()
root.title("Student Manage system")
root.config(bg='#696969')
root.geometry("1170x700+80+10")
root.iconbitmap('image.ico')
root.resizable(True,True)
# for jpg image
img=Image.open('im2.jpg')
photo=ImageTk.PhotoImage(img)
pho_label=Label(image=photo)
pho_label.pack()

##---------------------   Left Side Frane   ---------------------# 
DataEntryFrame=Frame(root,bg='#707070',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=60,y=80,width=500,height=600)

frontlabel=Label(DataEntryFrame,text='---------welcome--------',width=30,font=('arial',22,'italic bold'),bg='#83838B')
frontlabel.pack(side=TOP,expand=True)

addbtn=Button(DataEntryFrame,text='1. add student',width=15,font=('chiller',25,'bold'),bd=6,bg='#999999',activebackground='#9A9ACD',foreground='white',relief=RIDGE,activeforeground='white',command=addstudent)
addbtn.pack(side=TOP,expand=True)

searchbtn=Button(DataEntryFrame,text='2. search student',width=15,font=('chiller',25,'bold'),bd=6,bg='#999999',activebackground='#9A9ACD',foreground='white',relief=RIDGE,activeforeground='white',command=searchstudent)
searchbtn.pack(side=TOP,expand=True)

deletebtn=Button(DataEntryFrame,text='3. delete student',width=15,font=('chiller',25,'bold'),bd=6,bg='#999999',activebackground='#9A9ACD',foreground='white',relief=RIDGE,activeforeground='white',command=deletestudent)
deletebtn.pack(side=TOP,expand=True)

updatebtn=Button(DataEntryFrame,text='4. update student',width=15,font=('chiller',25,'bold'),bd=6,bg='#999999',activebackground='#9A9ACD',foreground='white',relief=RIDGE,activeforeground='white',command=upadtestudent)
updatebtn.pack(side=TOP,expand=True)

showbtn=Button(DataEntryFrame,text='5. show student',width=15,font=('chiller',25,'bold'),bd=6,bg='#999999',activebackground='#9A9ACD',foreground='white',relief=RIDGE,activeforeground='white',command=showstudent)
showbtn.pack(side=TOP,expand=True)

exportbtn=Button(DataEntryFrame,text='6. Save in excel',width=15,font=('chiller',25,'bold'),bd=6,bg='#999999',activebackground='#9A9ACD',foreground='white',relief=RIDGE,activeforeground='white',command=exporttudent)
exportbtn.pack(side=TOP,expand=True)

exitbtn=Button(DataEntryFrame,text='7. exit data',width=15,font=('chiller',25,'bold'),bd=6,bg='#999999',activebackground='#9A9ACD',foreground='white',relief=RIDGE,activeforeground='white',command=exitstudent)
exitbtn.pack(side=TOP,expand=True)


########################  Right Side Frane    ################################### 
# 1st step
ShowDataFrame=Frame(root,bg='PINK',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=700,y=80,width=500,height=600)

# -------------------------  show data frame  -------------------

style=ttk.Style()
# styling purpose (style.configure)
style.configure('Treeview.Heading',font=('chiller',20,'bold'),foreground='black')
style.configure('Treeview',font=('times',20,'bold'),background='#CDCDBA',foreground='black',rowheight=40)

# 3rd step
scroll_bar_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_bar_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
scroll_bar_x.pack(side=BOTTOM,fill=X)
scroll_bar_y.pack(side=RIGHT,fill=Y)

# 2nd step 
studenttable=Treeview(ShowDataFrame,columns=['Id','Name','Mobile','Email','Address','Gender','D.O.B','ADDED DATE','ADDED TIME'],xscrollcommand=scroll_bar_x.set,yscrollcommand=scroll_bar_y.set,height=50)

scroll_bar_x.config(command=studenttable.xview)
scroll_bar_y.config(command=studenttable.yview)

# 4th step
studenttable.heading('Id',text='Id')
studenttable.heading('Name',text='Name')
studenttable.heading('Mobile',text='Mobile')
studenttable.heading('Email',text='Email')
studenttable.heading('Address',text='Address')
studenttable.heading('Gender',text='Gender')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('ADDED DATE',text='ADDED DATE')
studenttable.heading('ADDED TIME',text='ADDED TIME')

# for column width
studenttable.column('Id',width=100)
studenttable.column('Name',width=200)
studenttable.column('Mobile',width=200)
studenttable.column('Email',width=300)
studenttable.column('Address',width=200)
studenttable.column('Gender',width=100)
studenttable.column('D.O.B',width=150)
studenttable.column('ADDED DATE',width=150)
studenttable.column('ADDED TIME',width=150)
studenttable.pack(fill=Y,expand=1)

# only show heading ( only show heading 5th step)
studenttable['show']='headings'
#----------------------------  slides --------------------------#######  

ss='Welcome to student management system'
text=''
count=0

##---------------------  Welcome heading  ---------------------###

SlideLabel=Label(root,text=ss,font=('chiller',25,'italic bold'),relief=RIDGE,borderwidth=4,width=40,bg='#B9B9D3')
SlideLabel.place(x=350,y=0)
IntroLabelTick()
introLabelcolorTick()

####-----------------   Clock  ---------------------####

clock=Label(root,font=('times',14,'italic bold'),relief=RIDGE,borderwidth=4,bg='white')
clock.place(x=0,y=0)
tick()


########################### Connect To Database   ###################
connectionbutton=Button(root,text='Connect To Database',width=23,font=('chiller',19,'italic bold'),relief=RIDGE,borderwidth=4,bg='#A1A1A1',activebackground='blue',activeforeground='white',foreground='white',command=connectdb)
connectionbutton.place(x=930,y=0)

########################## Connect Label ########################
root.mainloop()
