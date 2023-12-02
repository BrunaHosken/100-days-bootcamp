.py
#Day 3
# Control Flow and Logical Operators

#if else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif (age >= 45 and age <= 55):
    print("Everything is going ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adults tickets are $12.")

  wants_photo = input("Dou you want photo taken? Y or N. ")
  if (wants_photo == "Y" or wants_photo == "y"):
    bill += 3
    print("Photo ticket price is $3.")

  print(f"Your final bill is ${bill}.")

else:
  print("Sorry, you are not tall enough to ride the rollercoaster.")


