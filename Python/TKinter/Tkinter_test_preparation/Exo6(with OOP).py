from tkinter import *
import time



# creating the class
class DigitalClock:
    # constructor
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("300x150")

        self.clock_label = Label(root, text="", font=("garamond", 48, "bold"))
        self.clock_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.update_time()

    # updating the time
    def update_time(self):    
        current_time = time.strftime("%H:%M:%S")
        self.clock_label.config(text=current_time)
        self.root.after(1000, self.update_time)
    
    
# creating the main window
root = Tk()
digital_clock = DigitalClock(root)
root.mainloop()