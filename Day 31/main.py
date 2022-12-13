from tkinter import *
from tkinter import messagebox
import random
BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526)

card_front_image = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0)
card_back_image = PhotoImage(file="images/card_back.png")

x_mark_image = PhotoImage(file="images/wrong.png")
check_mark_image = PhotoImage(file="images/right.png")

x_mark_button = Button(image=x_mark_image, highlightthickness=0)
check_mark_button = Button(image=check_mark_image, highlightthickness=0)


x_mark_button.grid(row=1, column=0)
check_mark_button.grid(row=1, column=1)


window.mainloop()