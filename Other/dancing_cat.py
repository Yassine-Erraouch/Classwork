import tkinter as tk

# Define the rainbow colors and the width of each color segment
rainbow_colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
color_width = 80  # Width of each color block

class RainbowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rainbow Animation")
        self.root.geometry("600x400")

        # Create a canvas to display the rainbow
        self.canvas = tk.Canvas(root, bg="black", width=600, height=100)
        self.canvas.pack()

        # Create a label to display the text after the rainbow
        self.label_text = tk.Label(root, font=("Courier", 24), fg="white", bg="black")
        self.label_text.pack(pady=20)

        # Start the rainbow animation
        self.animate_rainbow(0)

    def animate_rainbow(self, color_index):
        # If the rainbow isn't complete, keep adding colors
        if color_index < len(rainbow_colors):
            # Calculate where to start the new color
            x1 = color_index * color_width
            x2 = (color_index + 1) * color_width

            # Draw the color segment on the canvas
            self.canvas.create_rectangle(x1, 0, x2, 100, fill=rainbow_colors[color_index], outline=rainbow_colors[color_index])

            # Move to the next color
            self.root.after(300, self.animate_rainbow, color_index + 1)
        else:
            # Once the rainbow is complete, show the message
            self.label_text.config(text="You're gay!")

# Create the Tkinter window and start the application
root = tk.Tk()
app = RainbowApp(root)
root.mainloop()
