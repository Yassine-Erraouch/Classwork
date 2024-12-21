import tkinter as tk


window = tk.Tk()
window.title("Button click event handling")
window.geometry("400x100")

def on_click():
    label_text.set('Button Clicked')
    
    
label_text = tk.StringVar()
label_text.set("Click the button and check the message text:")
tk.Label(window, textvariable=label_text, font= ('garamond' , 14)).pack(pady=5)
btn = tk.Button(window, text="Click Me", font=('garamond' , 14), command=on_click)

btn.pack(pady=10)
#starting the window
window.mainloop()