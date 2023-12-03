MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

PENNY = 0.01
DIME = 0.1
NICKEL = 0.05
QUARTER = 0.25

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0
on_machine = True

def calc_coins():
    print("Please insert coins.")
    quarters= int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = (quarters * QUARTER) + (dimes * DIME) + (nickles * NICKEL) + (pennies * PENNY)
    total = round(total,2)
    return total

def check_resources(drink):
    drinks = drink["ingredients"]
    for drink in drinks:
        for resource in resources:
            if (drink == resource and drinks[drink]> resources[resource]):
                print(f"Sorry there is not enough {resource}")
                return False
    return True

def make_coffe(drink, coin, choice):
    if drink["cost"] > coin:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print (f"Here is your {choice} ☕️. Enjoy!")
        return True

def descont_resources(drink):
    drinks = drink["ingredients"]
    for drink in drinks:
        for resource in resources:
            if (drink == resource):
                resources[resource] -= drinks[drink]

def descont_coin(money,drink):
    money += drink['cost']
    money = round(money,2)
    return money

def return_coin(money,coins):
    total = coins - drink['cost']
    total = round(money,2)
    print(f"Here is ${total} in change.")

while on_machine:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        on_machine = False
        exit()
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    else:
        if choice != "espresso" and choice != "latte" and choice != "cappuccino":
            print("Sorry, we don't have this drink...")
        else:
            drink = MENU[choice]
            if (check_resources(drink)):
                coins = calc_coins()
                if(make_coffe(drink, coins, choice)):
                    descont_resources(drink)
                    money = descont_coin(money,drink)
                    return_coin(money, coins)


        