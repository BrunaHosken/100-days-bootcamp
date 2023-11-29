from calculator_files.art import logo
from replit import clear


def operations(num1, num2, operator):
  if operator == "+":
    return num1 + num2
  if operator == "-":
    return num1 - num2
  if operator == "*":
    return num1 * num2
  if operator == "/":
    return num1 / num2


def calculator():
  print(logo)
  should_continue = True
  first_number = float(input("What's the first number? "))

  while should_continue:
    print("+")
    print("-")
    print("*")
    print("/")
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number? "))
    result = operations(first_number, second_number, operation)
    print(f"{first_number} + {second_number} = {result}")
    option = input(
        f"Type 'y' to continue calculating with {result}. Type 'n' to start a new calculation. "
    )

    if option == 'y':
      first_number = result
    else:
      clear()
      should_continue = False
      calculator()


calculator()
