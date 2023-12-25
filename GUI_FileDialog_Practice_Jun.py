from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image



root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\PurpleFish.ico')


#root.filename = filedialog.askopenfilename(
#    initialdir=r"C:\Users\taesu\Desktop", title ="Select A File",
#    filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))
#    )


def Img_open():
    global my_img_1
    root.filename = filedialog.askopenfilename(
        initialdir= r'C:\Users\taesu\Desktop', title ="Select A File",
        filetypes=(("png files","*.png"),("jpg files","*.jpg"),("all files","*.*"))
        )
    my_img_1 = ImageTk.PhotoImage(Image.open(root.filename))
    mylabel_01 = Label(root, text=root.filename).pack()
    my_label_02 = Label(image = my_img_1).pack()

Button(root, text="Open Image Files", padx=20,pady = 20, command=Img_open).pack(padx=20,pady = 20)

root.filename = filedialog.askdirectory(
    initialdir= r'C:\Users\taesu\Desktop', title ="Select A FileDir"
    )

mylabel_01 = Label(root, text=root.filename).pack()


mainloop()