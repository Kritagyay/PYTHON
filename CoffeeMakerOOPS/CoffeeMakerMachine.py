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

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def transaction_successfull(money,drink_cost):
    if money>=drink_cost:
        change=round(money-drink_cost,2)
        print(f"Here's the change ${change}")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry you have'nt entered enough money to make your drink! Money is refunded")
        return False




def is_resource_sufficient(ingredients):
    for item in ingredients:
        if ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item} to make your coffee.")
            return False
        else:
            return True

def coins():
    print("Please enter coins.")
    total=int(input("How many quaters? "))*0.25
    total+=int(input("How many dimes? "))*0.1
    total+=int(input("How many nickles? "))*0.05
    total+=int(input("How many pennies? "))*0.01
    return total

def make_coffee(drink_name,ingredients):
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f"Here's your drink {drink_name}")





continue_work=True
while continue_work:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice=="off":
        continue_work=False
    elif choice=="report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee:{resources['coffee']} g")
        print(f"Money:${profit} ")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment=coins()
            if transaction_successfull(payment,drink['cost']):
                make_coffee(choice,drink['ingredients'])








