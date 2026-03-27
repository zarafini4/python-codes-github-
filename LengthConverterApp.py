from tkinter import *

root = Tk()
root.title("Length Converter App")
root.geometry("400x400")


def convert():
    try:
        inches = float(entry.get())
        cm = inches * 2.54
        result_label.config(text=f"{cm:.2f} cm")
    except:
        result_label.config(text="Enter a valid number")

title = Label(root, text="Length Converter", bg="lightblue")
title.pack(pady=20)

label = Label(root, text="Enter length in inches:", bg="lightblue")
label.pack()

entry = Entry(root)
entry.pack(pady=10)

btn = Button(root, text="Convert to cm", bg="green", fg="white", command=convert)
btn.pack(pady=10)

result_label = Label(root, text="", bg="lightblue")
result_label.pack(pady=20)

root.mainloop()