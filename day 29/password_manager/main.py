from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list.append(random.choice(letters).upper())
    [password_list.append(random.choice(numbers)) for i in range(2)]
    [password_list.append(random.choice(symbols)) for i in range(2)]
    numb_left = int(spinbox.get()) - 5
    [password_list.append(random.choice(letters)) for i in range(numb_left)]
    random.shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)
    entry_of_password.delete(0, END)
    entry_of_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_password():
    missing_data = False
    variables = {
        "website": entry_of_website.get(),
        "email": entry_of_user.get(),
        "password": entry_of_password.get()
    }

    for data in variables:
        if variables[data] == "":
            variables[data] = "None"
            missing_data = True

    password = variables['password']
    website = variables['website']
    email = variables['email']

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if missing_data:
        massage = f"Some data is missing.\nShould it be added as:\n{website} | {email} | {password}"
        user_choice = messagebox.askokcancel(title="Confirmation", message=massage)

    else:
        massage = f"Should this be added:\n{website} | {email} | {password}"
        user_choice = messagebox.askokcancel(title="Confirmation", message=massage)

    if user_choice:
        try:
            with open("data.json", "r") as data_file:
                # reading old data
                data = json.load(data_file)
                # updating old data with new data
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # saving updated data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

    # end of the save, clear sections if user confirmed
    pyperclip.copy(password)
    entry_of_website.delete(0, END)
    entry_of_password.delete(0, END)


def search():
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            website = entry_of_website.get().lower()

    except FileNotFoundError:
        massage = f"You don't have anything saved yet\ntry adding some first"
        messagebox.showinfo(title="Error", message=massage)

    else:
        notfound = True

        for entry in data:
            if entry.lower() == website:
                email = data[entry]["email"]
                password = data[entry]["password"]
                massage = f"website: {website}\nusername: {email}\npassword: {password}"
                messagebox.showinfo(title="Searched Data", message=massage)
                pyperclip.copy(password)
                notfound = False

        if notfound:
            massage = f"Could not find the website: {website}"
            messagebox.showinfo(title="Error", message=massage)


# ---------------------------- UI SETUP ------------------------------- #

# program window
window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=40, bg="black")

# lock image
image_lock = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
canvas.create_image(100, 100, image=image_lock, anchor="center")
canvas.grid(column=1, row=0)

# text sections:
website_lable = Label(text="Website:", bg="black", fg="white")
user_lable = Label(text="Email/Username:", bg="black", fg="white")
password_lable = Label(text="Password:", bg="black", fg="white")

# placing text sections:
website_lable.grid(column=0, row=1, pady=1)
user_lable.grid(column=0, row=2, pady=1)
password_lable.grid(column=0, row=3, pady=1)

# text input sections:
entry_of_website = Entry(window, width=29)
entry_of_website.focus()
entry_of_user = Entry(window, width=48)
entry_of_user.insert(0, "spam_baleus@gmail.com")
entry_of_password = Entry(window, width=29)

# placing text input sections:
entry_of_website.grid(column=1, row=1, pady=1)
entry_of_user.grid(column=1, row=2, columnspan=2, pady=1)
entry_of_password.grid(column=1, row=3, pady=1)

# creating buttons:
generate_password_button = Button(text="Generate Password", height=1, command=password_generator)
add_button = Button(text="Add", width=39, command=save_password)
search_button = Button(text="Search", width=15, command=search)
# set the spinbox value
my_var = StringVar(window)
my_var.set("12")
spinbox = Spinbox(from_=6, to=22, width=2, textvariable=my_var)

# placing created buttons:
generate_password_button.grid(column=2, row=3, pady=1)
add_button.grid(column=1, row=4, columnspan=2, pady=1)
spinbox.grid(column=3, row=3, pady=1)
search_button.grid(column=2, row=1, pady=1)

# creating

window.mainloop()
