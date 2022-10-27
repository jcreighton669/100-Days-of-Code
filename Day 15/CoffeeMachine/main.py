MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

QUARTER_VALUE = 0.25
DIME_VALUE = 0.10
NICKEL_VALUE = 0.05
PENNY_VALUE = 0.01


def print_report():
    """Prints the available resources inside the coffee machine."""
    print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g "
          f"\nMoney: ${profit}")


# TODO: Prompt options include drinks, report, off
def check_resources_available(drink_ingredients):
    """Confirms that the drink selection can be made."""
    for item in drink_ingredients:
        if drink_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the value of the coins inserted for the drink selection"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * QUARTER_VALUE
    total += int(input("How many dimes?: ")) * DIME_VALUE
    total += int(input("How many nickels?: ")) * NICKEL_VALUE
    total += int(input("How many pennies?: ")) * PENNY_VALUE
    return total


def is_payment_successful(payment_made, drink_cost):
    """Returns the whether a drink can be made."""
    if payment_made >= drink_cost:
        change = round(payment_made - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that is not enough money. Your change is returned.")
        return False


def make_coffee(drink_name, ingredients):
    """Makes the drink and removes the used resources from the machine."""
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {drink_name} ☕. Please enjoy!")


def coffee_machine():
    """Coffee Machine Main Function"""
    is_on = True

    while is_on:
        option = input("-> What would you like? (espresso/latte/cappuccino): ").lower()
        if option == "report":
            print_report()
        elif option == "off":
            is_on = False
        else:
            drink = MENU[option]
            if check_resources_available(drink["ingredients"]):
                payment = process_coins()
                if is_payment_successful(payment, drink["cost"]):
                    make_coffee(option, drink["ingredients"])


coffee_machine()
