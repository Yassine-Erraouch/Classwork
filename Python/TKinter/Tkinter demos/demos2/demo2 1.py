from tkinter import *
ui=Tk()
ui.title('My First Window')

ui.geometry("1412x1500")
file_path = r'Python\TKinter\Tkinter demos\demos2\armor_chest_plate.png'
photos1=PhotoImage(file= file_path)
ui.resizable(False,False)
#ui.iconbitmap('myImg.ico')
l=Label(ui,image=photos1).place(x=0,y=0)
l1=Label(ui,text="Give a : ",fg="white",bg="black",font="Bold 20").place(x=100,y=80)
l2=Label(ui,text="Give b : ",fg="white",bg="black",font="Bold 20").place(x=100,y=180)
ui.mainloop()
print(file_path)