import mysql.connector as co              #for sql connectivity
from prettytable import PrettyTable     #to print output in tabular form
import random                   #to generate fee id and admission numbers
from datetime import date     #for using in fee receipt

#making a function to dispaly output in box borders for ease of readibility
def print_msg_box(msg, indent=1, width=None, title=None):
    """Print message-box with optional title."""
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * len(title):<{width}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)

#for viewing all admisission details
def show_admin_details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
        cursor=mycon.cursor()
        cursor.execute("select * from admission" )
        data = cursor.fetchall()
        t = PrettyTable([' Admission_Number','Roll_Number','Name','Address','Phone_no','Class'])
        for x in data:
            l=list(x)
            t.add_row(l)
        print(t)
        mycon.close 
        cm=input("press any key to continue\n")
        print(cm)
    except:
        print("error")

#report card generator
def viewer1():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project") 
        cursor=mycon.cursor()
        ac=int(input("Enter admission number:\n"))
        print('\t\t\tEdupod School\t\t\t')
        st1= "select Sname from Student where Adm_No='%s'"%(ac)
        cursor.execute(st1)
        data = cursor.fetchall()
        n=data[0][0]
        a= "select class from Student where Adm_No='%s'"%(ac)
        cursor.execute(a)
        data = cursor.fetchall()
        c=data[0][0]
        b= "select section from Student where Adm_No='%s'"%(ac)
        cursor.execute(b)
        data = cursor.fetchall()
        s=data[0][0]
        st= "select Subject1,Subject2,Subject3 from Student where Adm_No='%s'"%(ac)
        cursor.execute(st)
        data=cursor.fetchall()
        out='''        Report Card
        Name:{}
        Class:{}
        Section:{}'''.format(n,c,s)
        print_msg_box(out,width=25)
        s1=data[0][0]
        s2=data[0][1]
        s3=data[0][2]
        t = PrettyTable(['Subject1','Subject2','Subject3']) 
        for x in data:
           l=list(x)
           t.add_row(l)
        print(t)
        marks1(s1,s2,s3)
        cm=input("press any key to continue\n") 
        print(cm)
        cursor.close()
        mycon.close()
    except:
       print("error")
       cm=input("press any key to continue\n") 
       print(cm)
    

#result generator
def marks1(s1,s2,s3) :
    if s1>=33 and s2>=33 and s3>=33 :
        an="Result: PASS"
        print_msg_box(an)  
        per=(s1+s2+s3)/3
        sa="Percentage:{}".format(per)
        print_msg_box(sa)
        if per>=60: 
            ka="FIRST DIVISION"
        elif per>=50:
            ka="SECOND DIVISION" 
        else:   
            ka="THIRD DIVISION"
        print_msg_box(ka) 
    else:
        an="Result: FAIL"
        print_msg_box(an)

def search_admin_details():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    try:
        st= "select * from admission where Admission_Number='%s'"%(ac)
        cursor.execute(st)
        data = cursor.fetchall()
        t = PrettyTable([' Admission_Number','Roll_Number','Name','Address','Phone_no','Class'])
        for i in data:
            l=list(i)
            t.add_row(l)
        print(t)
        cm=input("press any key to continue\n")
        print(cm)
    except:
        print("Record not found")

def delete_admin_details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")
        cursor=mycon.cursor() 
        ac=int(input("Enter admission number:\n"))
        st="delete from admission where Admission_Number='%s'"%(ac)
        cursor.execute(st) 
        mycon.commit()
        print ('Data deleted successfully')
        cm=input("press any key to continue\n")
        print(cm)
    except:
        print("Error")

#editing admission table details
def edit_admin_details():
    try:
        print("Make your choice")
        print("1: Edit name")
        print("2: Edit Address")
        print("3: Phone number")
        print("4: Return \n")
        print("\t\t") 
        cc=int(input("Enter your choice"))
        if cc==1: 
            edit_name()
        elif cc==2: 
            edit_address()
        elif cc==3: 
            edit_phno()
        elif cc==4:
            return None
        else:
            print("Error: Invalid Choice try again")
        cm=input("press any key to continue\n")
        print(cm)
            
    except:
        print("Error")

#editing submenus for admission table
def edit_name():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter correct name:\n')
        if nm.isalpha():
            break
        else:
            print("Please enter a valid value")
    st= "update admission set Name='%s' where Adm_no='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('Data updated successfully')
    cm=input("press any key to continue\n")
    print(cm)

def edit_address():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter correct Address:\n')
        if nm.isalpha() or nm.isspace():
            break
        else:
            print("Please enter a valid value")
    st= "update admission set Address='%s' where Adm_no='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('Data updated successfully')
    cm=input("press any key to continue\n")
    print(cm)

def edit_phno():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter correct phone number:\n')
        if nm.isdigit():
            break
        else:
            print("Please enter a valid value")
    st= "update admission set Phone_number='%s' where Adm_no=%s"%(nm,ac) 
    cursor.execute(st)
    print("Success") 
    cm=input("press any key to continue\n")
    print(cm)

def Add_Records():
    try:
        mycon=co.connect(host="localhost",user="root",passwd="ishaan2002",database="Project")
        cursor=mycon.cursor()
        while True:
            ses=input("Enter Session:\n")
            if ses.isalnum():
                break
            else:
                print("Please enter a valid value")
        while True:
            sname=input("Enter Student name:\n")
            if sname.isalpha() or sname.isspace():
                break
            else:
                print("Please enter a valid value")
        while True:
            clas=input("Enter Class:\n")
            if clas.isdigit():
                break
            else:
                print("Please enter a valid value")
        while True:
            se=input("Enter section:\n")
            if se.isalpha():
                break
            else:
                print("Please enter a valid value")
       
        nm=int(input("Enter Roll no:\n"))
        s1=int(input("Enter Marks in subject 1:\n"))
        s2=int(input("Enter Marks in subject 2:\n"))
        s3=int(input("Enter Marks in subject 3:\n"))
        while True:
            ai=input("Enter admission number:\n:\n")
            if ai.isalnum():
                break
            else:
                print("Please enter a valid value")
        query="insert into Student values('{}','{}','{}','{}',{},'{}','{}','{}','{}')".format(ses,sname,clas,se,nm,s1,s2,s3,ai)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in admission table")
        cm=input("press any key to continue\n")
        print(cm)
    except:
        print("Error")
        cm=input("press any key to continue\n")
        print(cm)

def Show_Stu_Details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
        cursor=mycon.cursor()
        cursor.execute("select * from Student" )
        data = cursor.fetchall()
        t = PrettyTable(['Session','SName','Class','Section','Student_roll_Number','Subject1','Subject2','Subject3','Admission_Number'])
        for x in data:
            l=list(x)
            t.add_row(l)
        print(t)
        mycon.close
        cm=input("press any key to continue\n")
        print(cm) 
    except:
        print("error")
        cm=input("press any key to continue\n")
        print(cm)

def Search_Stu_Details():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        av=input("Enter admission number:\n:\n")
        if av.isdigit():
            break
        else:
            print("Please enter a valid value")
    try:
        st= "select * from Student where Adm_no='%s'"%(av)
        cursor.execute(st)
        data = cursor.fetchall()
        t = PrettyTable(['Session','SName','Class','Section','Student_roll_Number','Subject1','Subject2','Subject3','Admission_Number'])
        for x in data:
            l=list(x)
            t.add_row(l)
        print(t)
        cm=input("press any key to continue\n")
        print(cm)
    except:
        print("Record not found")
        cm=input("press any key to continue\n")
        print(cm)


def Delete_Stu_Details():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")
        cursor=mycon.cursor() 
        ac=int(input("Enter admission number:\n:\n"))
        st="delete from Student where Adm_no='%s'"%(ac)
        cursor.execute(st) 
        mycon.commit()
        print ('Data deleted successfully')
        cm=input("press any key to continue\n")
        print(cm)
    except:
        print("Error")
        cm=input("press any key to continue\n")
        print(cm)

#student database editing interface
def Edit_Stu_Details():
    try:
        print("Make your choice")
        print("1: Edit name")
        print("2: Edit class")
        print("3: edit section")
        print("4: edit roll no.")
        print("5: Edit Session")
        print("6: Edit Marks")
        print("7: Exit \n")
        print("\t\t") 
        cc=int(input("Enter your choice"))
        if cc==1: 
            Sedit_name()
        elif cc==2: 
            Sedit_class()
        elif cc==3: 
            Sedit_section()
        elif cc==4:
            Sedit_rollno()
        elif cc==5:
            Sedit_ses()
        elif cc==6:
            Sedit_marks()
        elif cc==7:
            return
        else:
            print("Error: Invalid Choice try again")
    except:
        print('error')

#editing submenus accessible via previous function
def Sedit_name():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter correct name:\n')
        if nm.isalpha() or nm.isspace():
            break
        else:
            print("Please enter a valid value")   
    st= "update Student set SName='%s' where Adm_no='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('Data updated successfully')
    cm=input("press any key to continue\n")
    print(cm)

def Sedit_marks():
    while True:
        n=int(input("Enter subject no of marks to be changed or enter 0 to exit"))
        mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
        cursor=mycon.cursor()
        while True:
            ac=input("Enter admission number:\n")
            if ac.isdigit():
                break
            else:
                print("Please enter a valid value")
        if n==1:
            nm=int(input('Enter correct marks:\n'))
            st= "update Student set Subject1='%s' where Adm_no='%s'"%(nm,ac) 
            cursor.execute(st)
            mycon.commit()
            print ('Data updated successfully')
        elif n==2:
            nm=int(input('Enter correct marks:\n'))
            st= "update Student set Subject2='%s' where Adm_no='%s'"%(nm,ac) 
            cursor.execute(st)
            mycon.commit()
            print ('Data updated successfully')
        elif n==3:
            nm=int(input('Enter correct marks:\n'))
            st= "update Student set Subject3='%s' where Adm_no='%s'"%(nm,ac) 
            cursor.execute(st)
            mycon.commit()
            print ('Data updated successfully')
        elif n==0:
            return None
        else:
            print("invlaid input")
        cm=input("press any key to continue\n")
        print(cm)

def Sedit_rollno():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter correct Roll no:\n')
        if nm.isdigit():
            break
        else:
            print("Please enter a valid value")
    st= "update Student set Student_roll_number='%s' where Adm_no='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('Data updated successfully')
    cm=input("press any key to continue\n")
    print(cm)
def Sedit_section():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=("Enter admission number:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter correct section:\n')
        if nm.isalpha() or nm.isspace():
            break
        else:
            print("Please enter a valid value")
    st= "update Student set Section='%s' where Adm_no='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('Data updated successfully')
    cm=input("press any key to continue\n")
    print(cm)
def Sedit_ses():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter correct session:\n')
        if nm.isalnum():
            break
        else:
            print("Please enter a valid value")
    st= "update Student set Session='%s' where Adm_no='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('Data updated successfully')
    cm=input("press any key to continue\n")
    print(cm)

def Sedit_class():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter correct class:\n')
        if nm.isdigit():
            break
        else:
            print("Please enter a valid value")
    st= "update Student set Student_roll_number='%s' where Adm_no='%s'"%(nm,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('Data updated successfully')
    cm=input("press any key to continue\n")
    print(cm)


#student database interaction interface
def Studentmenu():
    while True:
        print("\t\t............................")
        print("\t\t****WELCOME TO EDUPOD****")
        print("\t\t............................")
        print("\n\t\t****Student Data Menu****")
        print("1:Add Student Record")
        print("2:Show Student Details")
        print("3:Search Student Record")
        print("4:Delete Student Record")
        print("5:Edit Student Record")
        print("6:Exit:\n")
        print("\t\t-----------------------------")
        choice=int(input("Enter your choice:1-6"))
        if choice==1:
            Add_Records()
        elif choice==2:
            Show_Stu_Details()
        elif choice==3:
            Search_Stu_Details()
        elif choice==4:
            Delete_Stu_Details()
        elif choice==5:
            Edit_Stu_Details()
        elif choice==6:
            return
        else:
            print("Invalid choice.Try again.")

#for adding records to admission table
def admin_details():
    try:
        mycon=co.connect(host="localhost",user="root",passwd="ishaan2002",database="Project")
        cursor=mycon.cursor()
        rno=int(input("Enter Roll no.:\n"))
        while True:
            sname=input("Enter Student name:\n")
            if sname.isalpha() or sname.isspace():
                break
            else:
                print("Please enter a valid value")
        while True:
            address=input("Enter Address(without spaces):\n")
            if address.isalpha() or address.isspace():
                break
            else:
                print("Please enter a valid value")
        while True:
            phon=input("Enter Phone no:\n")
            if phon.isdigit():
                break
            else:
                print("Please enter a valid value")
        while True:
            clas=input("Enter Class:\n")
            if clas.isdigit():
                break
            else:
                print("Please enter a valid value")
        
        
        
        cursor.execute("select Admission_Number from Admission" )
        data = cursor.fetchall()
        while True:
            t=random.randrange(100000,999999)
            if t not in data:
                adno=t
                print("Admission no assigned is",adno)
                break
        query="insert into admission values('{}',{},'{}','{}','{}','{}')".format(adno,rno,sname,address,phon,clas)
        cursor.execute(query)
        mycon.commit()
        print("Record has been saved in admission table")

        cm=input("press any key to continue\n")
        print(cm)
        mycon.close()
        cursor.close()
    except:
        print("Error")
        cm=input("press any key to continue\n")
        print(cm)

#for searching specific fee data
def searcher():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    try:
        st= "select * from Fees where Admission_No='%s'"%(ac)
        cursor.execute(st)
        data = cursor.fetchall()
        t = PrettyTable(['Admission_No','Total Fees','Amount Left','Mode of Payment','Fee ID'])
        for x in data:
            l=list(x)
            t.add_row(l)
        print(t)
        cm=input("press any key to continue\n")
        print(cm)
    except:
        print("Record not found")
        cm=input("press any key to continue\n")
        print(cm)

#viewing all fee data
def viewer():
    try:
        mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
        cursor=mycon.cursor()
        cursor.execute("select * from Fees" )
        data = cursor.fetchall()
        t = PrettyTable(['Admission_No','Total Fees','Amount Left','Mode of Payment','Fee ID'])
        for x in data:
            l=list(x)
            t.add_row(l)
        print(t)
        mycon.close()
        cm=input("press any key to continue\n")
        print(cm) 
    except:
        print("error")
        cm=input("press any key to continue\n")
        print(cm)

#payment interface function
def payer():
    mycon=co.connect(host="localhost", user="root", passwd="ishaan2002", database="Project")  
    cursor=mycon.cursor()
    while True:
        ac=input("Enter admission number:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        nm=input('Enter amount paid by person:\n')
        if nm.isdigit():
            break
        else:
            print("Please enter a valid value")
    while True:
        mp=input("enter mode of payment:\n")
        if ac.isdigit():
            break
        else:
            print("Please enter a valid value")
    
    cursor.execute("select Admission_No from Fees" )
    data = cursor.fetchall()

    #automated random fee id generator
    while True:
        t=random.randrange(100000,999999)
        if t not in data:
            ids=t
            break
    st= "update Fees set Amount_Left=Total_Fees-'%s' where Admission_No='%s'"%(nm,ac) 
    cursor.execute(st)
    st= "update Fees set Mode_of_Payment='%s' where Admission_No='%s'"%(mp,ac) 
    cursor.execute(st)
    st= "update Fees set Fee_ID='%s' where Admission_No='%s'"%(ids,ac) 
    cursor.execute(st)
    mycon.commit()
    print ('Data updated successfully')
    
    
    #fee receipt
    today = date.today()
    msg='''             Fee Receipt

    Fee ID:{}

    Date:{}

    Admission No:{}

    Amount of {} paid to SSMRV Trust

    Mode of payment:{}

             Edupod'''.format(ids,today,ac,nm,mp)
    print(print_msg_box(msg,width=50))
    cm=input("press any key to continue\n")
    print(cm)
    mycon.close()
    
#for adding records to feemenu
def adder():
    try:
        mycon=co.connect(host="localhost",user="root",passwd="ishaan2002",database="Project")
        cursor=mycon.cursor()
        adno=int(input("Enter Admission no.:\n"))
        tf=int(input("Enter total fees:\n"))
        al=tf    
        mode='fee not paid yet'
        fid='none'
        query="insert into Fees values('{}','{}',{},'{}','{}')".format(adno,tf,al,mode,fid)
        cursor.execute(query)
        mycon.commit()
        mycon.close()
        cursor.close()
        print("Record has been saved in Fees table")
        cm=input("press any key to continue\n")
        print(cm)
    except:
        print("Error")
        cm=input("press any key to continue\n")
        print(cm)

#function for navigating feemenu   
def Feemenu():    
    fc=int(input('''What would you like to do
    1-View table
    2-Add records
    3-Edit records
    4-Search record\n'''))
    if fc==1:
        viewer()
    if fc==2:
        adder()
    if fc==3:
        payer()
    if fc==4:
        searcher()


#main program for choosing required submenu
while True:
    print("\t\tWelcome to School Management System\t\t")
    print("\n\t\tEdupod\t\t")
    print('''Options
    1: Admission
    2: Student Data
    3: Fees Details
    4: Report card
    5: Exit\n''')
    ch=int(input("Please choose an option"))
    if ch==1:
        #inbuilt admission submenu
        print("\t\t*****Edupod School Management System*****\t\t") 
        print("\t\t*****Admission*****\t\t")
        print("1: Admission Details")
        print("2: Show admission details")
        print("3: Search admin details")
        print("4: Deletion of records")
        print("5: Update Admission Details")
        print("6: Return\n")
        print("\t\t") 
        choice=int(input("Enter your choice"))
        if choice==1: 
            admin_details()
        elif choice==2: 
            show_admin_details()
        elif choice==3: 
            search_admin_details()
        elif choice==4: 
            delete_admin_details()
        elif choice==5: 
            edit_admin_details()
        elif choice==6:
            continue


    if ch==2:
        print(ch)
        Studentmenu()
    if ch==3:
        Feemenu()

    if ch==4:
        viewer1()

    if ch==5:
        print("Closing program")
        break







                                                              


                                     

