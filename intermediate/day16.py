#day16
#OOP

from turtle import Turtle, Screen
from prettytable import PrettyTable

timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("black","purple")
timmy.forward(100)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon", ['Pikachu', 'Squirtle', 'Charmander', 'Eevee'])
table.add_column("Type", ['Electric', 'Water', 'Fire', 'Normal'])
table.align = "l"

print(table)