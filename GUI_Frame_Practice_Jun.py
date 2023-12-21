from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Learn GUI Jun")

root.iconbitmap(r'Icons\ruby.ico')

frame = LabelFrame(root, text="This is my Frame", padx= 30, pady=30)
frame.pack(padx=20,pady=20)

frame2 = LabelFrame(root, text="This is my Frame2", padx= 30, pady=30)
frame2.pack(padx=20,pady=20)

b = Button(frame, text="Don't click here!")
b.grid(row=0,column=0)

b2 = Button(frame, text="or here")
b2.grid(row=1,column=1)  

b3 = Button(frame2, text="What is this?")
b3.pack()
       
# Usually .pack() and .gird() cannot be used simultaneously.
# But this is adjusted to frame by frame as you can pack the frame but inside frame you can grid the element.



root.mainloop()
                  
