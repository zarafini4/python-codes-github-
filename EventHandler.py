from tkinter import *

window= Tk()
window.title("Event Handler")
window.geometry("100x100")

def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)
 
def handle_click(event):
    print("The button is clicked")

button= Button(text= "Click Me!", fg= "Blue", bg= "pink", height= 3, width= 12, command= "display")
button.pack()
button.bind("<Button-1>", handle_click)

window.mainloop()