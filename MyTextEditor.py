from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

window= Tk()
window.title("Codingal's Text Editor")
window.geometry("600x500")
window.columnconfigure(1, minsize= 800, weight= 1)
window.rowconfigure(0, minsize= 800, weight= 1)

def open_file():
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    txt_edit.delete(1.0, END)
    with open(filepath, "r")as input_file:
        a= input_file.read()
        txt_edit.insert(END, a)
        input_file.close()
    
    window.title(filepath)

def save_file():
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not filepath:
        return
    with open(filepath, "w")as output_file:
        a= txt_edit.get(1.0, END)
        output_file.write(a)
    
    window.title(filepath)

txt_edit= Text(window)
fr_buttons= Frame(window, relief= RAISED, borderwidth= 1)
btn_open= Button(fr_buttons, text= "OPEN", fg= "Black", bg= "Grey", command= open_file)
btn_save= Button(fr_buttons, text= "SAVE AS", fg= "Black", bg= "Grey", command= save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()