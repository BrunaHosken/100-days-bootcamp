import sheety 

print("Welcome to Bruna's Flight Club.\n We find the best flight deals and email them to you.")

first_name= input("What's your first name? ")
last_name= input("What's your last name? ")

email1 = "email1"
email2 = "email2"

while email1 != email2:
    email1 = input("What's your email? ")
    if email1.lower() == "quit" or email1.lower() == "exit":
        exit()
    email2 = input("Please verify your email: ")
    if email2.lower() == "quit" or email2.lower() == "exit":
        exit()

print("OK. You're in the club!")
sheety.post_user(first_name, last_name, email1)