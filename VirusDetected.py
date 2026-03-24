from tkinter import *
from tkinter import messagebox

root= Tk()
root.geometry("200x200")

def msg():
    messagebox.showwarning("Alert", "Stop! Virus Found.")

def msg2():
    messagebox.showinfo("Info", "Virus is harmful for devices. Get your virus scan done.")

button= Button(text= "Scan For Virus", fg= "Black", bg= "Grey", height= 3, width= 12, command= msg)
button.place(x=40, y=80)

button2= Button(text= "Show info", fg= "Black", bg= "Grey", height= 3, width= 12, command= msg2)
button2.place(x=40, y=20)

root.mainloop()