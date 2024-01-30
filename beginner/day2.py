#day2
#data types

#String
print("Hello"[0])
print("Hello"[-1])

#Integer
print(123 + 456)
print(123_456_789)

#Float
print(3.1415)

#Boolean
print(True)
print(False)

#Conversions
#Int to string
num_char = len(input("Name: "))
new_num_char = str(num_char)
print(type(num_char))
print("your name has " + new_num_char + " characters")

#Int to Float
a = float(123)
print(a)

#Float to Int
num_int = int(123.456)
print(num_int)

#String to Int
num_int = int("123456")
print(num_int)

#operations
print(3 + 5)
print(7 - 4)
print(3 * 2)
print(6 / 3)
print(2**3)
print(3 * 3 + 3 / 3 - 3)

#number manipulation and F strings
print(round(8 / 3, 2))
print(8 // 3)

result = 4 / 2
result /= 2
print(result)

score = 0
score += 1  #-=, *=
print(score)

height = 1.8
isWinning = True

print(
    f"Your score is {score} and your height is {height}. Are you winning? {isWinning}"
)

print("\n----------------------------------------")
print("Day 2 Project - Tip Calculator")
print("\nWelcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = float(input("What tip would you like to give? 10, 12 or 15? "))
people = float(input("How many people to split the bill? "))

amount = (total_bill / people) * (1 + (tip / 100))
final_amount = round(amount, 2)
final_amount = "{:.2f}".format(amount)

print(f"Each person should pay: ${final_amount}")
