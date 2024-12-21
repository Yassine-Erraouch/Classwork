import tkinter as tk


#creating the window
window = tk.Tk()
window.title("menu window")
window.geometry("400x100")


#creating the menu bar

menu_bar = tk.Menu(window)
window.config(menu=menu_bar)

#creating a menu
file_menu = tk.Menu(menu_bar,tearoff=0)

#adding the menu items
    #adding the File section
file_menu.add_command(label="New")

file_menu.add_command(label="Open")

#adding separator
file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=window.destroy
)
#showing the menu in the window
menu_bar.add_cascade(
    label="File",
    menu=file_menu
)
    #adding the Edit section
edit_menu = tk.Menu(menu_bar, tearoff=0)
    #adding the Help Section
help_menu = tk.Menu(menu_bar, tearoff=0)
    #showing the menus on the menu bar
menu_bar.add_cascade(
    label="Edit",
    menu=edit_menu
)

menu_bar.add_cascade(
    label="Help",
    menu=help_menu
)



#starting the window
window.mainloop()
