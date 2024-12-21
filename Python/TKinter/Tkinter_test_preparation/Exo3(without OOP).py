import tkinter as tk

#creating the window

window = tk.Tk()
window.title("Timer")
window.geometry("300x300")

# creating the fonts
font_regular= ('garamond', 16)
font_bold = ("garamond", 18, "bold")

# creating the string vars for the entries and the timer label
minutes_text = tk.StringVar()
seconds_text = tk.StringVar() 
timer_text = tk.StringVar()

# setting the strings vars to a default value of 0
minutes_text.set('0')
seconds_text.set('0')

#creating the inputs, labels and buttons

    #the minutes label and entry
tk.Label(window, text="Minutes: ", font=font_regular).grid(row=0, column=0, padx=10, pady=5)
minutes_entry = tk.Entry(window, textvariable=minutes_text, font=font_regular)
minutes_entry.grid(row=0, column=1, padx=10, pady=5)

    # the seconds label and entry
tk.Label(window, text="Seconds: ", font=font_regular).grid(row=1, column=0, padx=10, pady=5)
seconds_entry = tk.Entry(window, textvariable=seconds_text, font=font_regular)
seconds_entry.grid(row=1, column=1, padx=10, pady=5)

    #the timer label
tk.Label(window, textvariable=timer_text, font=font_bold).grid(row=2, column=0, columnspan=2)

    #the start and stop buttons
    strt_btn = tk.Button(windwo, text="Start", font= font_regular,)
