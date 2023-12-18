from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letters_list = [choice(letters) for _ in range(randint(8, 10) - 1)]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4) - 1)]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4) - 1)]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(END, string=password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if(website != "" and email != "" and password != ""):
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} \nPassword: {password} \nIs it ok to save?")
        if(is_ok):
            data_saved = f"{website} | {email} | {password} \n"

            with open(f"./password_manager_files/password_manager.txt", mode="a") as file:
                file.write(data_saved)
                website_entry.delete(0,END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

            website_entry.focus()
            email_entry.insert(END, string="bruna@mail.com")
    else:
        messagebox.showinfo(title="Ops...", message="Please, insert all informations")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
photoimage = PhotoImage(file = "./password_manager_files/logo.png")
canvas.create_image(115, 100, image = photoimage)
canvas.grid(column = 1, row = 0)


#Labels
website_label = Label(text="Website:")
website_label.grid(column = 0, row = 1)

email_label = Label(text="Email/Usarname:")
email_label.grid(column = 0, row = 2)

password_label = Label(text="Password:")
password_label.grid(column = 0, row = 3)

#Inputs

website_entry= Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_entry= Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(END, string="bruna@mail.com")

password_entry= Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")


#Buttons
generate_button = Button(text = "Generate Password",  highlightthickness = 0, command=password_generator)
generate_button.grid(column = 2, row = 3, sticky="EW")

generate_button = Button(text = "Add", width=36,  highlightthickness = 0, command=save_password)
generate_button.grid(column = 1, row = 4, columnspan=2, sticky="EW")



window.mainloop()