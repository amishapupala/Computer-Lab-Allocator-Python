from tkinter import *
from tkinter import messagebox
import csv
window6=Tk()
window6.title("Computer Lab Allocator")
window6.geometry('700x500')
class UpdateStudRec():
    def UpdateDetail(self):
        '''window6=Tk()
        window6.title("Computer Lab Allocator")
        window6.geometry('700x500')'''
        global e1
        global e2
        global e3
        l1=Label(window6, text="Enter the roll number of the student whose data you want to delete:",font=("Arial Bold",10))
        e1 = Text(window6, height=1, width=20)

        lbl=Label(window6,text='Update Record:',font=("Arial Bold",17))
        lbl.place(x=250, y=65)
        l1.place(x=165, y=120)
        e1.place(x=280, y=150)
        lnew=Label(window6, text="Enter the new Details:",font=("Arial Bold",13))
        lnew.place(x=270, y=200)
        l2=Label(window6, text="Enter the new Name:",font=("Arial Bold",10))
        e2 = Text(window6, height=1, width=20)
        l2.place(x=180, y=250)
        e2.place(x=330, y=250)
        l3=Label(window6, text="Enter the new Date:",font=("Arial Bold",10))
        e3 = Text(window6, height=1, width=20)
        l3.place(x=180, y=290)
        e3.place(x=330,y=290)

        
        B=Button(window6, text ="Submit",command=lambda:self.UpdateRec())
        B.place(x=300, y=330)
        B2=Button(window6, text ="  Go Back  ",command=lambda:self.GoBack())
        B2.place(x=560, y=410)
        mainloop()

    def UpdateRec( self ):
        val1=e1.get("1.0",END)
        val2=e2.get("1.0",END)
        val3=e3.get("1.0",END)
        print(val1)
        print(val2)
        print(val3)
        with open('Library.csv', 'r') as inp, open('first_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if(len(row)>0):
                    if(row[1]==str(val1)):
                        updatedRec = [val2, val1,val3]
                        writer.writerow(updatedRec)
                    else:
                        writer.writerow(row)
        with open('first_edit.csv', 'r') as inp, open('Library.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if(len(row)>0):
                    writer.writerow(row)
        messagebox.showinfo(title="Successful", message="Record is Updated Successfully!")
    def GoBack(self):
        window6.destroy()
        from AdminPage import AdminP
up=UpdateStudRec()
up.UpdateDetail()