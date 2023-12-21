############ Buid Image Viewer ##################
from tkinter import *

from PIL import ImageTk, Image

root = Tk()
root.title("Learn GUI Jun")

root.iconbitmap(r'Icons\ruby.ico')


my_img_1 = ImageTk.PhotoImage(Image.open(r"Images\Hitokage_pokemon.png"))
my_img_2 = ImageTk.PhotoImage(Image.open(r"Images\Hushigiso.png"))
my_img_3 = ImageTk.PhotoImage(Image.open(r"Images\pikachu_02.png"))
my_img_4 = ImageTk.PhotoImage(Image.open(r"Images\Hushigidane.png"))
my_img_5 = ImageTk.PhotoImage(Image.open("Images\pikachu.png"))


image_list = [my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

image_num = 0



Jun_sign = Label(root, text="Jun", bd = 3, relief = SUNKEN, anchor = W)
Jun_sign.grid(row = 2, column = 0, columnspan = 2, sticky = W+E)
status = Label(root, text="Image %d of %d" %(image_num+1,len(image_list)))
status.grid(row = 2, column = 2)

my_label = Label(image = image_list[image_num])
my_label.grid(row = 0, column = 0, columnspan = 3)


def click_back(num):
    global my_label
    global image_num
    global button_back
    global button_mid
    global button_forward
    
    
    image_num = num - 1
    
    if image_num < 1:
        #image_num = 0
        #print(1)
        button_back.grid_forget()
        button_back = Button(root, text= " << " , padx = 20, pady = 15, state=DISABLED)
        button_back.grid(row = 1, column = 0)
        
    my_label.grid_forget()
    my_label = Label(image = image_list[image_num])
    my_label.grid(row = 0, column = 0, columnspan = 3)
    
    if image_num == len(image_list)-2:
        button_forward.grid_forget()
        button_forward = Button(root, text= " >> " , padx = 20, pady = 15, command = lambda: click_forward(image_num))
        button_forward.grid(row = 1, column = 2)
    
    button_mid.grid_forget()
    button_mid = Button(root, text= " %d " %(image_num+1), padx = 20, pady = 15, state=DISABLED)
    button_mid.grid(row = 1, column = 1)
    
    status = Label(root, text="Image %d of %d" %(image_num+1,len(image_list)))
    status.grid(row = 2, column = 2)
    
    return image_num

def click_forward(num):
    global my_label
    global image_num
    global button_forward
    global button_back
    global button_mid
    image_num = num + 1
    if image_num > (len(image_list)-2):
        #image_num = 0
        #print(1)
        button_forward.grid_forget()
        button_forward = Button(root, text= " >> " , padx = 20, pady = 15, state=DISABLED)
        button_forward.grid(row = 1, column = 2)
        
    my_label.grid_forget()
    my_label = Label(image = image_list[image_num])
    my_label.grid(row = 0, column = 0, columnspan = 3)
    
    if image_num == 1:
        button_back.grid_forget()
        button_back = Button(root, text= " << " , padx = 20, pady = 15, command = lambda: click_back(image_num))
        button_back.grid(row = 1, column = 0)
    
    button_mid.grid_forget()
    button_mid = Button(root, text= " %d " %(image_num+1), padx = 20, pady = 15, state=DISABLED)
    button_mid.grid(row = 1, column = 1)
    
    status = Label(root, text="Image %d of %d" %(image_num+1,len(image_list)))
    status.grid(row = 2, column = 2)
    
    return

if image_num == 0:
    button_back = Button(root, text= " << " , padx = 20, pady = 15, command = lambda: click_back(image_num), state=DISABLED)
else:
    button_back = Button(root, text= " << " , padx = 20, pady = 15, command = lambda: click_back(image_num))
button_mid = Button(root, text= " %d " %(image_num+1), padx = 20, pady = 15, state=DISABLED)
button_forward = Button(root, text= " >> " , padx = 20, pady = 15, command = lambda: click_forward(image_num))

button_back.grid(row = 1, column = 0)
button_mid.grid(row = 1, column = 1, pady = 10)
button_forward.grid(row = 1, column = 2)


#button_quit = Button(root, text="Exit", command = root.quit)
#button_quit.pack()


root.mainloop()