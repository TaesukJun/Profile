from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from PIL import ImageTk, Image



root = Tk()
root.title("Scrollbars Example")
root.iconbitmap(r'Icons\PurpleFish.ico')
root.geometry("600x500")



def on_configure(event):
    canvas.configure(scrollregion=canvas.bbox('all'))


# Create a canvas and add scrollbars
canvas = Canvas(root, borderwidth=0, background="#ffffff")
vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
hsb = Scrollbar(root, orient="horizontal", command=canvas.xview)

canvas.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

# Pack the canvas and scrollbars
canvas.pack(side="left", fill="both", expand=True)
vsb.pack(side="right", fill="y")
hsb.pack(side="bottom", fill="x")

# Add a frame to the canvas (this will be the scrollable part)
frame = Frame(canvas, background="#ffffff")
canvas.create_window((0, 0), window=frame, anchor="nw")

# Add some widgets to the frame
for i in range(20):
    label = Label(frame, text=f"Label {i}")
    label.pack(pady=5, padx=10)

# Bind the event to update the scroll region when the size changes
frame.bind("<Configure>", on_configure)

# Run the Tkinter main loop
root.mainloop()

