import tkinter as tk


root = tk.Tk()
root.title("first TKinter window")
root.geometry("600x400")
root.configure(bg="pink")
#label
label = tk.Label(root, text="love yourself!" , font=("Roboto", 20), bg="pink")
label.pack()
#button
def on_click():
    label.config(text="you loved yourself ☆*: .｡. o(≧▽≦)o .｡.:*☆")

button = tk.Button(root, text="click to love yourself", command=on_click, relief="raised", bg="pink")
button.pack()

entry = tk.Entry(root)
entry.pack()

def show_text():
    text = entry.get()
    label.config(text=f"you're a dickhead {text} :D")
#running the window
root.mainloop()
