from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\ruby.ico')

#r = IntVar() #StringVar() #IntVar
#r.set("2")



def clicked(value):
    global myLabel
    myLabel.destroy()
    myLabel = Label(root, text = value)
    myLabel.pack()

MODES = [
    ("Pepperoni","Pepperoni"),
    ("Cheese","Cheese"),
    ("Mushroom","Mushroom"),
    ("Onion","Onion"),
    ]

pizz = StringVar()
pizz.set("Pepperoni")

for text, mod in MODES:
    Radiobutton(root, text=text, variable=pizz , value = mod ).pack(anchor=W)

#Radiobutton(root, text="Option 1", variable = r, value = 1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable = r, value = 2, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 3", variable = r, value = 3, command=lambda: clicked(r.get())).pack()

#myLabel = Label(root, text = pizz.get())
#myLabel.pack()
                


myButton = Button(root, text="click me!", command=lambda: clicked(pizz.get()))
myButton.pack()


myLabel = Label(root, text = pizz.get())
myLabel.pack()

mainloop()