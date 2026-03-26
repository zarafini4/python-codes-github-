import tkinter as tk
from datetime import date

root = tk.Tk()
root.title("Age Calculator App")
root.geometry("400x400")
root.configure(bg="light blue")

def calculateage():
        name = entry_name.get()
        day = int(entry_day.get())
        month = int(entry_month.get())
        year = int(entry_year.get())

        today = date.today()
        age = today.year - year

        if (today.month, today.day) < (month, day):
            age -= 1

        result_label.config(text=f"Hello {name}! You are {age} years old.")


title_label = tk.Label(root, text="Age Calculator", bg="lightblue", font=("Arial", 16))
title_label.pack(pady=10)

frame1 = tk.Frame(root, bg="lightblue")
frame1.pack(pady=5)
tk.Label(frame1, text="Name:", bg="lightblue").pack(side="left")
entry_name = tk.Entry(frame1)
entry_name.pack(side="left")

frame2 = tk.Frame(root, bg="lightblue")
frame2.pack(pady=5)
tk.Label(frame2, text="Day:", bg="lightblue").pack(side="left")
entry_day = tk.Entry(frame2, width=5)
entry_day.pack(side="left")

frame3 = tk.Frame(root, bg="lightblue")
frame3.pack(pady=5)
tk.Label(frame3, text="Month:", bg="lightblue").pack(side="left")
entry_month = tk.Entry(frame3, width=5)
entry_month.pack(side="left")

frame4 = tk.Frame(root, bg="lightblue")
frame4.pack(pady=5)
tk.Label(frame4, text="Year:", bg="light blue").pack(side="left")
entry_year = tk.Entry(frame4, width=8)
entry_year.pack(side="left")

calc_button = tk.Button(root, text="Calculate Age", command=calculateage)
calc_button.pack(pady=15)

result_label = tk.Label(root, text="", bg="lightblue", font=("Arial", 12))
result_label.pack()

root.mainloop()