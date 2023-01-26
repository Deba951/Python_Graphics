from tkinter import *
from tkinter.ttk import *

from time import strftime

# Creating a window
root = Tk()
root.title("DC-Clock")

# Fetching the current time
def show_time():
    time = strftime("%H:%M:%S %p")
    label.config(text=time)
    label.after(1000, show_time)

# Deigning the window
label = Label(root, font=("ds-digital", 100), background="#171717", foreground="#00abae")
label.pack(anchor='center')

# Calling the function
show_time()
mainloop()