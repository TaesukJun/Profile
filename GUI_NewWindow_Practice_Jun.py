from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from time import time, ctime


root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\ruby.ico')


def Winopen():
    global my_img
    top = Toplevel()
    top.title("Learn GUI Jun2")
    top.iconbitmap(r'Icons\ruby.ico')

    Label_01 = Label(top,text="Hi").pack()
    my_img = ImageTk.PhotoImage(Image.open("images\Hushigiso.png"))
    Label_02 = Label(top, image = my_img).pack()
    Button(top,text="close window",padx=20,pady=20, command=top.destroy).pack(padx=20,pady=20)



Button(root, text="Open 2nd window",padx=20,pady=20, command=Winopen).pack(padx=20,pady=20)

mainloop()