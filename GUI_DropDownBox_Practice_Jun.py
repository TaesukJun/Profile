from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image



root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\PurpleFish.ico')
root.geometry("600x500")

def clicked_show():
    myLabel = Label(root, text=selected.get())
    myLabel.pack()

selected = StringVar()


#selected.set("Monday" )
#drop = OptionMenu(root, selected, "Monday", "Tuesday", "Wednesday", "Thursday")
#drop.pack()




options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday"
    ]

selected.set(options[0])
drop = OptionMenu(root, selected, *options)
drop.pack()



MyButton = Button(root, text = "Show Selection", command=clicked_show)
MyButton.pack()

mainloop()