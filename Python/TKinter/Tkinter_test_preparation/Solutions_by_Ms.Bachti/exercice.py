from tkinter import *

parent=Tk()
parent.geometry('400x400')
parent.title('exercice 1')
#*************Define fct showMessage**********************
def showMessage(event):
    lbl_message.configure(text="Button clicked ! ")

#****************************************************
lbl_message=Label(parent,font=('cursive',20),text="Click the button and check the message Text..")
lbl_message.pack(pady=10)
btn=Button(parent,text="click Me",bg="yellow",fg="white")
btn.bind('<Button-1>',showMessage)
btn.pack(pady=10)
parent.mainloop()
