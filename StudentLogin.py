
from Student import student
from pprint import pprint
from tkinter import messagebox
from tkinter import *
import datetime
import csv


class StudentLogin( object ):
    def __init__( self ):
        self.students = {}

    def studLoginPage(self):
        window2=Tk()
        window2.title("Student Details")
        window2.geometry('700x500')
        global e1
        global e2
        l1=Label(window2, text="Student Name:",font=("Arial Bold",10))
        l2=Label(window2, text="Roll Number:",font=("Arial Bold",10))

        
        e1 = Text(window2, height=1, width=20)
        e2 = Text(window2, height=1, width=20)
        lbl=Label(window2,text='Enter the Following Details:',font=("Arial Bold",17))
        lbl.place(x=160, y=110)
        l1.place(x=160, y=170)
        e1.place(x=300, y=170)
        l2.place(x=160, y=220)
        e2.place(x=300, y=220)
        B=Button(window2, text ="Submit",command=lambda:self.retrieve_input())
        B.place(x=270, y=270)
        mainloop()
        
    
    def retrieve_input(self):
        #global name=e1.get()
        
        name=e1.get("1.0",END)
        rollno=e2.get("1.0",END)
        date=datetime.datetime.today().strftime('%Y-%m-%d,%H:%M')
        print(name)
        print(rollno)
        print(date)
                
        with open('Library.csv','a') as out:
            csvWriter = csv.writer(out)
            row = (name,rollno,date)
            csvWriter.writerow(row)
        #self.writeOut()
        messagebox.showinfo(title="Successful", message="Record is Inserted successfully!")
    

        

    
studentLogin= StudentLogin()

studentLogin.studLoginPage()



#pprint(studentLogin.students)
#studentLogin.writeOut()