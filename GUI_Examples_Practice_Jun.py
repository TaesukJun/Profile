from tkinter import *


############ Icons, Images, and Exit Buttons ##################
from PIL import ImageTk, Image

root = Tk()
root.title("Learn GUI Jun")

root.iconbitmap(r'C:\JunDrive\Python\Pictures\ruby.ico')


my_img = ImageTk.PhotoImage(Image.open(r"C:\JunDrive\Python\Pictures\0370_bw_Index0004_20231121031004.png"))
my_label = Label(image = my_img)
my_label.pack()


#button_quit = Button(root, text="Exit", command = root.quit)
#button_quit.pack()


root.mainloop()

"""


############ Simple Calculator ##################


root = Tk()
root.title("Simple Calculator Jun v01")

e = Entry(root, width = 50, bg = "green", fg = "black", borderwidth = 5)

e.grid(row = 0, column = 0, columnspan = 4, rowspan = 1, padx = 10, pady = 10)


global current
current = 0
global mode
mode = ""


def click_put_num(number):
    temp = e.get()
    e.delete(0, END)
    e.insert(0, int(str(temp) + str(number)))
    return

def click_clear():
    e.delete(0, END)
    global current
    global mode
    current = 0
    mode = ""
    return

def click_add():
    temp = int(e.get())
    global current
    global mode
    if mode == "add":
        e.delete(0, END)
        current= int(temp + current)
    else:
        current = int(temp)
        e.delete(0, END)
        mode = "add"
    return


def click_substract():
    temp = int(e.get())
    global current
    global mode
    if mode == "substract":
        e.delete(0, END)
        current = int(current - temp)
    else:
        current = int(temp)
        e.delete(0, END)
        mode = "substract"
    return


def click_equal():
    global mode
    global current

    
    temp = int(e.get())
    e.delete(0,END)
    
    
    if mode == "add":
        temp = temp + current
    if mode == "substract":
        temp = current - temp
        
        
    e.insert(0, temp)
    current = 0
    mode = ""
    
    return

button_00 = Button(root, text= " 0 " , padx = 40, pady = 30, command = lambda: click_put_num(0))
button_01 = Button(root, text= " 1 " , padx = 40, pady = 30, command = lambda: click_put_num(1))
button_02 = Button(root, text=" 2 ", padx = 40, pady = 30, command = lambda: click_put_num(2))
button_03 = Button(root, text=" 3 ", padx = 40, pady = 30, command = lambda: click_put_num(3))
button_04 = Button(root, text=" 4 ", padx = 40, pady = 30, command = lambda: click_put_num(4))
button_05 = Button(root, text=" 5 ", padx = 40, pady = 30, command = lambda: click_put_num(5))
button_06 = Button(root, text=" 6 ", padx = 40, pady = 30, command = lambda: click_put_num(6))
button_07 = Button(root, text=" 7 ", padx = 40, pady = 30, command = lambda: click_put_num(7))
button_08 = Button(root, text=" 8 ", padx = 40, pady = 30, command = lambda: click_put_num(8))
button_09 = Button(root, text=" 9 ", padx = 40, pady = 30, command = lambda: click_put_num(9))

button_substract = Button(root, text=" - ", padx = 40, pady = 30, command = click_substract)
button_add = Button(root, text=" + ", padx = 40, pady = 30, command = click_add)
button_equal = Button(root, text=" = ", padx = 40, pady = 30, command = click_equal)
button_clear = Button(root, text=" Clear ", padx = 40, pady = 30, command = click_clear)

# Put the button on the screen

rel_x_postion = 0
rel_y_postion = 0

button_00.grid(row = 4+rel_y_postion , column = 0+rel_x_postion)

button_01.grid(row = 3+rel_y_postion, column = 0+rel_x_postion)
button_02.grid(row = 3+rel_y_postion, column = 1+rel_x_postion)
button_03.grid(row = 3+rel_y_postion, column = 2+rel_x_postion)

button_04.grid(row = 2+rel_y_postion, column = 0+rel_x_postion)
button_05.grid(row = 2+rel_y_postion, column = 1+rel_x_postion)
button_06.grid(row = 2+rel_y_postion, column = 2+rel_x_postion)

button_07.grid(row = 1+rel_y_postion, column = 0+rel_x_postion)
button_08.grid(row = 1+rel_y_postion, column = 1+rel_x_postion)
button_09.grid(row = 1+rel_y_postion, column = 2+rel_x_postion)

button_substract.grid(row = 2+rel_y_postion, column = 4+rel_x_postion)
button_add.grid(row = 3+rel_y_postion, column = 4+rel_x_postion)
button_equal.grid(row = 4+rel_y_postion, column = 4+rel_x_postion)
button_clear.grid(row = 5+rel_y_postion, column = 0+rel_x_postion)




def myClick():
    Result_txt = "Hello, " + e.get()
    myLabel = Label(root, text = Result_txt)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", padx = 50, pady = 30, command = myClick, fg = "blue", bg = "red")

#fg = color font / bg = color for background
#padx = lateral size, pady = vertical size
#state = DISABLED => cannot clickable

#myButton.grid(row = 0, column = 0)
#myButton.pack()


root.mainloop()

############ Input Box ##################

root = Tk()

e = Entry(root, width = 50, bg = "green", fg = "black", borderwidth = 5)
e.pack()
e.insert(0,"Enter Your Name")
 


def myClick():
    Result_txt = "Hello, " + e.get()
    myLabel = Label(root, text = Result_txt)
    myLabel.pack()


myButton = Button(root, text="Enter Your Name", padx = 50, pady = 30, command = myClick, fg = "blue", bg = "red")

#fg = color font / bg = color for background
#padx = lateral size, pady = vertical size
#state = DISABLED => cannot clickable

#myButton.grid(row = 0, column = 0)
myButton.pack()


root.mainloop()

############ Button ##################

root = Tk()


def myClick():
    myLabel = Label(root, text = "Look! I clicked a Button!!!")
    myLabel.pack()


myButton = Button(root, text="Click Me!!!!!!!!!", padx = 50, pady = 30, command = myClick, fg = "blue", bg = "red")

#fg = color font / bg = color for background
#padx = lateral size, pady = vertical size
#state = DISABLED => cannot clickable

#myButton.grid(row = 0, column = 0)
myButton.pack()


root.mainloop()


############ Text & grid ##################

root = Tk()

# Creating a Label Widget
myLabel_01 = Label(root, text = "Hello World!")
myLabel_02 = Label(root, text = "My name is Jun")
myLabel_03 = Label(root, text = " pls ")

# Shoving it onto the screen
myLabel_01.grid(row = 0, column = 0)
myLabel_02.grid(row = 1, column = 5)
myLabel_03.grid(row = 1, column = 1)


myLabel_01 = Label(root, text = "Hello World!").grid(row = 0, column = 0)
myLabel_02 = Label(root, text = "My name is Jun").grid(row = 1, column = 5)
myLabel_03 = Label(root, text = " pls ").grid(row = 1, column = 1)


root.mainloop()


############ First ##################

root = Tk()

# Creating a Label Widget
myLabel = Label(root, text = "Hello World!")


# Shoving it onto the screen
myLabel.pack()



root.mainloop()

"""