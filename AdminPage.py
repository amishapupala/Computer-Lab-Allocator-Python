from tkinter import *


window4 = Tk()
class AdminP():
    def view(self):
        print('v')
        
        from ViewRecord import ViewRec
        #self.openRec()

    def insert(self):
        print('i')
        #window4.destroy()
        from InsertRecord import InsertRec
        InsertRec()

    def update(self):
        print('u')
        #window4.destroy()
        from UpdateRecord import UpdateStudRec 
        

    def delete(self):
        print('d')
        #window4.destroy()
        from DeleteRecord import DeleteRec
        
        

    def adminPg(self):
        
        window4.title("Welcome to Computer Lab Alloctor")
        window4.geometry('700x500')
        page1text = Label(window4, text="This is page 1")
        lbl=Label(window4,text='What operation do you want to perform?',font=("Arial Bold",17))

        lbl.place(x=140, y=110)

        Vbtn=Button(window4, text=" View Record ",font=("Arial Bold",9), command=lambda:self.view())
        Ibtn = Button(window4, text="Insert Record",font=("Arial Bold",9), command=lambda:self.insert())
        Ubtn =Button(window4, text="Update Record",font=("Arial Bold",9), command=lambda:self.update())
        Dbtn=Button(window4, text="Delete Record",font=("Arial Bold",9), command=lambda:self.delete())

        Vbtn.place(x=210, y=180)
        Ibtn.place(x=390, y=180)
        Ubtn.place(x=210, y=240)
        Dbtn.place(x=390, y=240)


        mainloop()

ap=AdminP()
ap.adminPg()