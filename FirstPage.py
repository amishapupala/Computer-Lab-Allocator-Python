from tkinter import *

#from AdminLogin import *
window1=Tk()
window1.title("Welcome to Computer Lab alloctor")
window1.geometry('700x500')
class FP():
    def FirstP(self):
        global var
        var = StringVar(window1)
        var.set("~~Select here~~")
        lbl=Label(window1,text='Select Your Designation',font=("Arial Bold",10))
        lbl.place(x=90, y=155)
        drop_menu = OptionMenu(window1, var,  "Admin", "Student",command=self.GetOption)
        drop_menu.grid(row=0, column=0)
        drop_menu.place(x=290, y=150)
        B1 = Button(window1, text ="Submit", command=lambda:self.NextPage())
        B1.place(x=230, y=193)
        window1.mainloop()

    def GetOption(self,event):
        global chosen_option
        value=var
        chosen_option = str(value.get())
        print(chosen_option)



    def NextPage(self):
        if(chosen_option=="Admin"):
            window1.destroy()
            from AdminLogin import AdminLoginP
            
        else:
            window1.destroy()
            from StudentLogin import StudentLogin


f1=FP()
f1.FirstP()
