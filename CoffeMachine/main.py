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
    "coffee": 100,
}

def isValid(orderIngredients):
    for item in orderIngredients:
        if orderIngredients[item] >= resources[item]:
            print(f"sorry, we ran out of ingredients for {item}")
            return False
    return True


def processCoins():
    print("enter your money")
    total = int(input("how many quarters")) * 0.25
    total += int(input("how many dimes")) * 0.1
    total += int(input("how many nickles")) * 0.05
    total += int(input("how many pennies")) * 0.01
    return total

def makeCoffee(drinkName, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print("here is your coffee")

def isSuccessful(payment, cost):
    if payment >= cost:
        # god damn, a way to call a global variable inside local stuff wtf
        global profit
        profit += payment
        change = round(payment - cost, 2)
        print(f"here is your change{change}")
        return True
    else:
        print("you poor, go grind some")
        return False

isRunning = True
while isRunning:
    choice = input("what would you like? 1- espresso 2- capa 3- latte")
    if choice == "off":
        isRunning = False
    elif choice == "report":
        print(f"water = {resources['water']}ml")
        print(f"milk = {resources['milk']}ml")
        print(f"coffee = {resources['coffee']}ml")
        print(f"profit = {profit}ml")
    else:
        drink = MENU[choice]
        if isValid(drink["ingredients"]):
            payment = processCoins()
            if isSuccessful(payment, drink["cost"]):
                makeCoffee(choice, drink["ingredients"])
