from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame


root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\PurpleFish.ico')
root.geometry("600x500")


pygame.mixer.init()

def soundplay():
    pygame.mixer.music.load(r"Sounds\흐헤헤.flac")
    pygame.mixer.music.play(loops=-1)

def soundstop():
    pygame.mixer.music.pause()





my_button = Button(root, text="Nice", font = ("Times new roman",32),
       padx = 20, pady = 20,
       command=soundplay
                   ).pack(padx = 20, pady = 20)

stop_button = Button(
    root, text="Stop", font = ("Times new roman",32),
    padx = 20, pady = 20,
    command=soundstop
    
    ).pack(padx = 20, pady = 20)

mainloop()