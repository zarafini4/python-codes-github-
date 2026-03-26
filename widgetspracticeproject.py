import tkinter as tk

window = tk.Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2

        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, f"Result: {result}")
    except:
        textbox.delete("1.0", tk.END)
        textbox.insert(tk.END, "Invalid input!")

label_title = tk.Label(window, text="Enter two numbers to find their product")
label_title.pack()

label1 = tk.Label(window, text="Enter first number:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Enter second number:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

button = tk.Button(window, text="Calculate", command=calculate)
button.pack()

textbox = tk.Text(window, height=2, width=30)
textbox.pack()

window.mainloop() 
from tkinter import *
from dateandtime import date

window= Tk()
window.title("Getting Started With Wigets")
window.geometry("400x300")

lbl= Label(text= "Hey There! Widgets are applications that the user can interact with.", fg= "blue", bg= "pink", height= 3, width= 12)
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