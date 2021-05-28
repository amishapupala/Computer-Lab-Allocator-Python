from tkinter import *
from tkinter import messagebox
import csv
window6=Tk()
window6.title("Computer Lab Alocator")
window6.geometry('700x500')
class DeleteRec():
    def DelDetail(self):
        '''window6=Tk()
        window6.title("Computer Lab Alocator")
        window6.geometry('700x500')'''
        global e1
        l1=Label(window6, text="Enter the roll number of the student whose data you want to delete",font=("Arial Bold",10))
        e1 = Text(window6, height=1, width=20)

        lbl=Label(window6,text='Delete a record:',font=("Arial Bold",17))
        lbl.place(x=160, y=110)
        l1.place(x=160, y=170)
        e1.place(x=280, y=200)
        
        B=Button(window6, text ="Submit",command=lambda:self.DelRec())
        B.place(x=320, y=250)
        B2=Button(window6, text ="  Go Back  ",command=lambda:self.GoBack())
        B2.place(x=560, y=410)
        mainloop()

    def DelRec( self ):
        val=e1.get("1.0",END)
        print(val)
        with open('Library.csv', 'r') as inp, open('first_edit.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if(len(row)>0):
                    if(row[1]!=str(val)):
                        writer.writerow(row)
        
        with open('first_edit.csv', 'r') as inp, open('Library.csv', 'w') as out:
            writer = csv.writer(out)
            for row in csv.reader(inp):
                if(len(row)>0):
                    writer.writerow(row)
        messagebox.showinfo(title="Successful", message="Record is deleted successfully")
    def GoBack(self):
        window6.destroy()
        from AdminPage import AdminP
d1=DeleteRec()
d1.DelDetail()