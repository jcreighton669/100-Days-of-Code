from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#FFFFFF"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(bg=WHITE, text="Website: ")
website_label.grid(column=0, row=1)
username_label = Label(bg=WHITE, text="Email/Username: ")
username_label.grid(column=0, row=2)
password_label = Label(bg=WHITE, text="Password: ")
password_label.grid(column=0, row=3)

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

add_info_button = Button(text="Add", width=36)
add_info_button.grid(column=1, row=4, columnspan=2)

window.mainloop()