#day 8
#function parameters e caesar cipher

def greet():
  print("Hello")
  print("How are you?")
  print("I'm fine, thank you")

greet()

print("---------------------------------")

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How are you {name}?")

greet_with_name("John")
greet_with_name("Mary")

print("---------------------------------")

def greet_with(name, location = "Brazil"):
  print(f"Hello {name}")
  print(f"I'm from {location}")

greet_with(name = "John", location = "Spain")
greet_with("Mary", "France")
greet_with("John")