from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
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

# ---------------------------- SEARCH INFO --------------------------------- #
def search_info():
    website = website_entry.get()
    try:
        with open("./password_manager_files/password_manager.json", mode="r") as file:
            data = json.load(file)
        data_info = data[website]
        messagebox.showinfo(title=website, message=f"Email: {data_info['email']} \nPassword: {data_info['password']}")
    except FileNotFoundError:
        messagebox.showinfo(title="Ops...", message="No Data File Found")
    except KeyError:
        messagebox.showinfo(title="Ops...", message="No details for the website exists")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website:{
            "email": email,
            "password": password,
        }
    }

    if(website == "" and email == "" and password == ""):
        messagebox.showinfo(title="Ops...", message="Please, insert all informations")
    else:
        try:
            with open("./password_manager_files/password_manager.json", mode="r") as file:
                data = json.load(file)
                
        except FileNotFoundError:
            with open("./password_manager_files/password_manager.json", mode="w") as file:
                json.jump(new_data, file, indent = 4)
        else:       
            data.update(new_data) 
            with open("./password_manager_files/password_manager.json", mode="w") as file:
                json.dump(data, file, indent= 4)

        finally:
            website_entry.delete(0,END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

            website_entry.focus()
            email_entry.insert(END, string="bruna@mail.com")        


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

website_entry= Entry(width=21)
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

email_entry= Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(END, string="bruna@mail.com")

password_entry= Entry(width=21)
password_entry.grid(column=1, row=3, sticky="EW")


#Buttons
generate_button = Button(text = "Search",  highlightthickness = 0, command=search_info)
generate_button.grid(column = 2, row = 1, sticky="EW")

generate_button = Button(text = "Generate Password",  highlightthickness = 0, command=password_generator)
generate_button.grid(column = 2, row = 3, sticky="EW")

generate_button = Button(text = "Add", width=36,  highlightthickness = 0, command=save_password)
generate_button.grid(column = 1, row = 4, columnspan=2, sticky="EW")



window.mainloop()