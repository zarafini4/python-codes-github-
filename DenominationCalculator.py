from tkinter import *

root= Tk()
root.title("Denomination Counter")
root.geometry("650x400")

lbl= Label(text= "Hey There!", fg= "blue", bg= "pink", height= 3, width= 14)
amount_lbl= Label(text= "Enter amount  here:", fg= "blue", bg= "pink", height= 3, width= 14)
amount_entry = Entry()

def calculate_denomination():
    amount= int(amount_entry.get())
    deno= [500, 200, 100, 50, 20, 10, 5, 2, 1]
    result= ""
    for i in deno:
        count= amount // i
        if count > 0:
            result += f"{i}: {count} \n"
        amount= amount % i
    result_lbl.config(text= result)

result_lbl= Label(text= "", fg= "blue", bg= "pink", height= 3, width= 14)
btn= Button(text= "Calculate", fg= "Black", bg= "#68686E", height= 3, width= 14, command= calculate_denomination)

lbl.pack()
amount_lbl.pack()
amount_entry.pack()
result_lbl.pack()
btn.pack()

root.mainloop()