from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image



root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\PurpleFish.ico')
root.geometry("600x500")

def clicked_show():
    global myLabel
    myLabel.destroy()
    myLabel = Label(root,text=var.get())
    myLabel.pack()



# var = IntVar() #StringVar()

var = StringVar()



c = Checkbutton(
    root, text="Check this box",
    variable = var, onvalue="I am truly fine", offvalue="Let there be light"
    )
c.deselect()
c.pack()

myButton = Button(root, text="Show Selection", command=clicked_show)
myButton.pack()

myLabel = Label(root,text= var.get())
myLabel.pack()

mainloop()