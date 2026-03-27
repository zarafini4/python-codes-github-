from tkinter import *

root = Tk()
root.title("Password Strength Checker App")
root.geometry("400x400")
root.config(bg="lightyellow")

def check_strength():
    password = entry.get()
    length = len(password)

    if length <= 5:
        result_label.config(text="Weak", fg="red")
    elif 6 <= length <= 8:
        result_label.config(text="Medium", fg="orange")
    elif 9 <= length <= 12:
        result_label.config(text="Strong", fg="lightgreen")
    else:
        result_label.config(text="Very Strong", fg="darkgreen")

title = Label(root, text="Password Strength Checker", font=("Arial", 16, "bold"), bg="lightyellow")
title.pack(pady=20)

label = Label(root, text="Enter Password:", font=("Arial", 12), bg="lightyellow")
label.pack()

entry = Entry(root, show="*", font=("Arial", 12))
entry.pack(pady=10)

btn = Button(root, text="Check Strength", command=check_strength, bg="blue", fg="white")
btn.pack(pady=10)

result_label = Label(root, text="", font=("Arial", 14), bg="lightyellow")
result_label.pack(pady=20)

root.mainloop()