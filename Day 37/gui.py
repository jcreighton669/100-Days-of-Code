from tkinter import *
from tkcalendar import Calendar

window = Tk()
window.title("Page Count Reading Tracker")
window.minsize(width=500, height=300)
window.config(padx=100, pady=150)

pages_label = Label(text="Pages Read")
pages_label.config(padx=20, pady=20)
pages_label.grid(column=1, row=1)

date_label = Label(text="Date Read (YYYY/MM/DD)")
date_label.config(padx=20, pady=20)
date_label.grid(column=1, row=2)

pages_input = Entry()
pages_input.grid(column=3, row=1)

submit_button = Button(text="Submit",)
submit_button.grid(column=2, row=3)


window.mainloop()
