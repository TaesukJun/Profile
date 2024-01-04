from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def clicked_slide():
    Label(root,text= Slider_h.get()).pack()

# https://www.tutorialspoint.com/python/tk_scale.htm

root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\PurpleFish.ico')
root.geometry("600x500")

Slider_v = Scale(root, from_= 0, to= 200,width=30, sliderlength=40, length= 200)
#default sliderlength = 30
#default length = 100
#default width = 15
Slider_v.pack()
Slider_v.set(100)

Slider_h = Scale(root, from_= 0, to= 200, orient = HORIZONTAL)
Slider_h.pack()





Button(root,text="Here",command=clicked_slide).pack()



w = Scrollbar(root)
w.pack(side = RIGHT, fill=Y)


mainloop()