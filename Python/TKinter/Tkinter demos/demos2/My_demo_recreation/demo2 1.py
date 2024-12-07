from tkinter import *
from PIL import Image, ImageTk  # Import Image and ImageTk from Pillow

ui = Tk()
ui.title('My First Window')

ui.geometry("1412x1500")

# Correct the file path to the full path if needed
file_path = r'Python\TKinter\Tkinter demos\demos2\armor_chest_plate.png'

# Open the image using Pillow
image = Image.open(file_path)

# Convert the image to a format compatible with Tkinter
photos1 = ImageTk.PhotoImage(image)

ui.resizable(False, False)

# Display the image
l = Label(ui, image=photos1).place(x=0, y=0)

# Add some text labels
l1 = Label(ui, text="Give a : ", fg="white", bg="black", font="Bold 20").place(x=100, y=80)
l2 = Label(ui, text="Give b : ", fg="white", bg="black", font="Bold 20").place(x=100, y=180)

ui.mainloop()

# Print file path for debugging
print(file_path)
