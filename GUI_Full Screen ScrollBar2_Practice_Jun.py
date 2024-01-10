from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

from tkinter import ttk

root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\PurpleFish.ico')
root.geometry("600x500")


#Create Main Frame
main_01 = Frame(root)
main_01.pack(fill=BOTH, expand = 1)

#Create Canvas
my_canvas = Canvas(main_01)
my_canvas.pack(side=LEFT,fill=BOTH,expand=1)

#Add ScrollBar to Canvas
my_scrollbar_v = ttk.Scrollbar(main_01,orient=VERTICAL, command=my_canvas.yview)
my_scrollbar_v.pack(side=RIGHT, fill=Y)
my_scrollbar_h = ttk.Scrollbar(main_01,orient=HORIZONTAL, command=my_canvas.xview)
my_scrollbar_h.pack(side=BOTTOM, fill=X)

#Configure Canvas
my_canvas.configure(yscrollcommand=my_scrollbar_v.set)
my_canvas.configure(xscrollcommand=my_scrollbar_h.set)
my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))


#Create Another Frame INSIDE Canvas
main_02 = Frame(my_canvas)

#Add New Frame to Window In Canvas
my_canvas.create_window((0,0), window=main_02, anchor='nw')


for i in range(100):
    Button(main_02, text = f'Button {i}').grid(row = i,column=0,pady=10,padx=10)
for i in range(100):
    Button(main_02, text = f'Button {i}').grid(row = 0,column=i+1,pady=10,padx=10)

mainloop()