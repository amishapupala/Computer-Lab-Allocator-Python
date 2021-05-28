from tkinter import *
import datetime
import csv
from tkinter import messagebox


window3=Tk()
window3.title("Admin Login")
window3.geometry('700x500')
class AdminLoginP( object ):

    def AdminLoginPage(self):
        
        global e1
        global e2
        e1=Label(window3, text="Username:",font=("Arial Bold",10)).grid(row=0)
        e2=Label(window3, text="Password:",font=("Arial Bold",10)).grid(row=1)

        
        e1 = Entry(window3)
        e2 = Entry(window3,show="*")

        e1.grid(row=0, column=1,padx=60, pady=2,sticky=NSEW)
        e2.grid(row=1, column=1,padx=60, pady=2,sticky=NSEW)
        B=Button(window3, text ="Submit",command=lambda:self.retrieve_input())
        B.place(x=100, y=50)
        mainloop()
        
    
    def retrieve_input(self):
        uname=e1.get()
        passwd=e2.get()
        if(uname=='admin' and passwd=='admin'):
            window3.destroy()
            from AdminPage import AdminP
        else:
            messagebox.showerror("Error","Invalid Username or password")  

w1=AdminLoginP()
w1.AdminLoginPage()