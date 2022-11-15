from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I Am a Label", font=("Arial", 24))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


# Button
def button_clicked():
    my_label.config(text=input_area.get())


button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Don't Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
input_area = Entry(width=10)
input_area.grid(column=3, row=2)
window.mainloop()
