from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from time import time, ctime


root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\ruby.ico')

# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askyesno("This is Jun popup!", "Hi")
    if response == 1:
        Label(root, text= ctime()).grid(row=1,column=0)
    else:
        Label(root, text= "No"), grid(row=1,column=0)
        

Button_01 = Button(root, text= "Pop up", anchor=CENTER, padx= 10, pady = 10, command= popup)
Button_01.grid(row=0, column=0,padx=20,pady=20)





mainloop()