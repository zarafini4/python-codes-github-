from tkinter import *
from dateandtime import date

window= Tk()
window.title("my demo window")
window.geometry("300x400")

lbl= Label(text= "Hey There!", fg= "blue", bg= "pink", height= 3, width= 12)
name_lbl= Label(text= "Full Name:", fg= "blue", bg= "pink", height= 3, width= 12)

name_entry = Entry()

def display():
    name= name_entry.get()
    global message
    message= "Welcome to this application \n Today's date is:"
    greet= "Hello " + name + "\n"
    textbox.insert(END, greet)
    textbox.insert(END, message)
    textbox.insert(END, date.today())

textbox= Text(height= 3)
btn= Button(text= "chk:", fg= "blue", bg= "pink", height= 3, width= 12, command= display)
lbl.pack()
name_lbl.pack()
name_entry.pack()
textbox.pack()
btn.pack()
window.mainloop()