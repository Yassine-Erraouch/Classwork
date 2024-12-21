from tkinter import *
import time

# creating the window

window = Tk()
window.title("Digital Clock")
window.geometry("300x150")

# creating a label to display the time
clock_label = Label(window, text="", font=("garamond", 48, "bold"))
clock_label.place(relx=0.5, rely=0.5, anchor=CENTER)

def update_time():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    window.after(1000, update_time)

# starting the window
update_time()
window.mainloop()