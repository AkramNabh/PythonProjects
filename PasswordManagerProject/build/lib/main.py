from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
from distutils.core import setup
import py2exe
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(0, random.randint(8, 10))]
    password_symbols = [random.choice(numbers) for _ in range(0, random.randint(2, 4))]
    password_numbers = [random.choice(symbols) for _ in range(0, random.randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)


    password = "".join(password_list)

    if len(password_entry.get()) == 0:
        password_entry.insert(0,password)
    else:
        password_entry.delete(0, END)
        password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def button_trigger():
    email = email_entry.get()
    password = password_entry.get()
    website = website_entry.get()
    new_data = {website: {
        "email":email,
        "password":password
    }}

    print(website, password, email)
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="nice try", message="check what you have left empty")
    else:
        try:
            with open("AniceWalkOnTheBeach.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("AniceWalkOnTheBeach.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open("AniceWalkOnTheBeach.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx= 50, pady= 50)

canvas = Canvas(width= 200, height= 200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)


# Labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username")
email_label.grid(column=0, row=2)
password_label = Label(text="Password")
password_label.grid(column=0, row=3)


# Entries
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.insert(END, "akramnabh@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


# Buttons

password_generator = Button(text="Generate Password",command=generatePassword)
password_generator.grid(column=2, row=3)
add_button = Button(width=36, text="Add",command=button_trigger)
add_button.grid(column=1, row=4,columnspan=2)

# checkButtons
symbol_state = IntVar()
symbol_checkButton = Checkbutton(text="symbols?", variable=symbol_state)
symbol_state.get()
symbol_checkButton.grid(column=3, row=3)
number_state = IntVar()
number_checkButton = Checkbutton(text="numbers?", variable=symbol_state)
number_state.get()
number_checkButton.grid(column=3, row=4)

window.mainloop()
