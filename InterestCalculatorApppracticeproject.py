import tkinter as tk

root = tk.Tk()
root.title("Interest Calculator App")
root.geometry("400x400")
root.configure(bg="lightyellow")

def calculate():
    try:
        p = float(entry_principal.get())
        t = float(entry_time.get())
        r = float(entry_rate.get())

        si = (p * t * r) / 100

        ci = p * (1 + r/100) ** t - p

        result_label.config(
            text=f"Simple Interest: {si:.2f}\nCompound Interest: {ci:.2f}"
        )

    except:
        result_label.config(text="Please enter valid numbers!")

title = tk.Label(root, text="Interest Calculator", font=("Arial", 16), bg="lightyellow")
title.pack(pady=10)

frame1 = tk.Frame(root, bg="lightyellow")
frame1.pack(pady=5)
tk.Label(frame1, text="Principal:", bg="lightyellow").pack(side="left")
entry_principal = tk.Entry(frame1)
entry_principal.pack(side="left")

frame2 = tk.Frame(root, bg="lightyellow")
frame2.pack(pady=5)
tk.Label(frame2, text="Time (years):", bg="lightyellow").pack(side="left")
entry_time = tk.Entry(frame2)
entry_time.pack(side="left")

frame3 = tk.Frame(root, bg="lightyellow")
frame3.pack(pady=5)
tk.Label(frame3, text="Rate (%):", bg="lightyellow").pack(side="left")
entry_rate = tk.Entry(frame3)
entry_rate.pack(side="left")

btn = tk.Button(root, text="Calculate", command=calculate)
btn.pack(pady=15)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightyellow")
result_label.pack()

root.mainloop()