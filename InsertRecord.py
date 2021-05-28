from pprint import pprint
from tkinter import *
import datetime
from tkinter import messagebox
import csv

window5=Tk()
window5.title("Student Details")
window5.geometry('700x500')
class InsertRec( object ):
    def __init__( self ):
        self.students = {}

    def InsRec(self):
        
        
        global e1
        global e2
        l1=Label(window5, text="Student Name:",font=("Arial Bold",10))
        l2=Label(window5, text="Roll Number:",font=("Arial Bold",10))

        
        e1 = Text(window5, height=1, width=20)
        e2 = Text(window5, height=1, width=20)
        lbl=Label(window5,text='Enter the following Details of the Student',font=("Arial Bold",17))
        lbl.place(x=160, y=110)
        l1.place(x=160, y=170)
        e1.place(x=300, y=170)
        l2.place(x=160, y=220)
        e2.place(x=300, y=220)
        B=Button(window5, text ="Submit",command=lambda:self.retrieve_input())
        B.place(x=270, y=270)
        B2=Button(window5, text ="  Go Back  ",command=lambda:self.GoBack())
        B2.place(x=560, y=410)
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
        with open('Library.csv', 'r') as inp, open('first_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if(len(row)>0):
                    writer.writerow(row)
        messagebox.showinfo(title="Successful", message="Record is Inserted successfully")
    
    def GoBack(self):
        window5.destroy()
        from AdminPage import AdminP




    '''def writeOut( self ):
        
        with open('Library.csv','w') as out:
            csvWriter = csv.writer(out)
            csvWriter.writerow(('ID','name','rollno','date'))
            
            for item in self.students:
                b = self.students[item][0]
                name = self.students[item][1]
                rollno = self.students[item][2]
                date=self.students[item][3]

                row = (b.id,b.name,b.rollno,b.date)
                
                csvWriter.writerow(row)'''

        

    
ir= InsertRec()

ir.InsRec()

'''studentLogin.studInfo('1','aaa','1111',datetime.datetime.now().time())
studentLogin.studInfo('2','bbb','2222',datetime.datetime.now().time())
studentLogin.studInfo('3','ccc','3333',datetime.datetime.now().time())
studentLogin.studInfo('4','ddd','4444',datetime.datetime.now().time())
studentLogin.studInfo('5','eee','5555',datetime.datetime.now().time())'''

pprint(ir.students)
#studentLogin.writeOut()