from tkinter import *
from PIL import ImageTk, Image
import sqlite3


root = Tk()
root.title("Learn GUI Jun")
root.iconbitmap(r'Icons\PurpleFish.ico')
root.geometry("600x500")

# Databases

# Create a database or connect to one
Myconn = sqlite3.connect('address_book.db')

# Create cursor
Mycursor = Myconn.cursor()


'''
# Create table
Mycursor.execute("""CREATE TABLE addresses (
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integar
    )
                 """)
'''

def clikced_submit():
    # Clear text boxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zipcode.delete(0, END)

# Create Text Boxes

f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=10)

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=10)

address_entry = Entry(root, width=30)
address_entry.grid(row=2, column=1, padx=10)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=10)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=10)

zipcode = Entry(root, width=30)
zipcode.grid(row=5, column=1, padx=10)

# Create Text Labels
f_name_label = Label(root, text="First Name:")
f_name_label.grid(row=0,column=0)

l_name_label = Label(root, text="Last Name:")
l_name_label.grid(row=1,column=0)

address_entry_label = Label(root, text="Address:")
address_entry_label.grid(row=2,column=0)

city_label = Label(root, text="City:")
city_name_label.grid(row=3,column=0)

state_label = Label(root, text="State:")
state_label.grid(row=4,column=0)

zipcode_label = Label(root, text="Zipcode:")
zipcode_label.grid(row=5,column=0)

#Create submite buttons

submit_btn = Button(root, text= "Add Record To Database", command=clikced_submit)
submit_btn.gird(row=6,column=0, columnspan=2,pady=10,padx=10,ipadx=100)




# Commit changes
Myconn.commit()

# Close Connection
Myconn.close()

mainloop()
