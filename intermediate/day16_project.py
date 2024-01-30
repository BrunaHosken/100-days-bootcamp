#coffe machine oop project

from coffee_maker_files.coffe_maker import CoffeeMaker
from coffee_maker_files.money_machine import MoneyMachine
from coffee_maker_files.menu import Menu

money_machine = MoneyMachine()
coffe_maker = CoffeeMaker()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice= input(f"What would you like? ({options}): ") 
    if choice == "off":
        is_on = False
    elif  choice == "report":
        coffe_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if(drink != None):
            if(coffe_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost)):
                coffe_maker.make_coffee(drink)
        