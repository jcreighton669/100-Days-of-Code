from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- CONSTANTS ------------------------------- #
WHITE = "#FFFFFF"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q',
               'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure that you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: "
                                                              f"\nUsername: {username} "
                                                              f"\nPassword: {password} "
                                                              f"\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                file.close()


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
website_input.focus()
username_input = Entry(width=35)
username_input.grid(column=1, row=2, columnspan=2)
username_input.insert(0, "jcreighton669@bears.shawu.edu")
password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_password_button = Button(text="Generate Password", command=generate)
generate_password_button.grid(column=2, row=3)

add_info_button = Button(text="Add", width=36, command=save)
add_info_button.grid(column=1, row=4, columnspan=2)

window.mainloop()