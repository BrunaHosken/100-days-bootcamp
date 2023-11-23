#Day 3
#Randomisation and python lists

import random

import my_module

#random
random_integer = random.randint(1, 10)
print(random_integer)

print(my_module.pi)

random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}\n")

#List
states_of_america = ["California", "Texas", "Florida", "New York", "Illinois"]
print(states_of_america)
print(states_of_america[0])
print(states_of_america[-1])

states_of_america[1] = "Washington"
print(states_of_america)

states_of_america.append("Ohio")
print(states_of_america)

states_of_america.extend(["Colorado", "Nevada"])
print(states_of_america)

print(states_of_america[len(states_of_america) - 1])

fruits = [
    "Straberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
    "Pears"
]
vegetables = ["Kale", "Tomatoes", "Celery", "Potatoes", "Spinach"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)
print(dirty_dozen[1][1])
