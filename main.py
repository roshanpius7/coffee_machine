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


def is_resource_sufficient(order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coin():
    total = int(input("enter number of quarters :")) *0.25
    total += int(input("enter number of dimes :")) * 0.10
    total += int(input("enter number of nickels :")) * 0.05
    total += int(input("enter number of pennies :")) * 0.01
    return total

def transaction_successfull(amount_paid, drink_amount):
    if amount_paid >= drink_amount:
        change=round(amount_paid-drink_amount)
        print(f" here is your change${change} ")
        global profit
        profit+=drink_amount
        return True
    else:
        print("sorry money is not sufficient , Money is refunded")
        return False


def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
     resources[item] -=order_ingredients[item]

    print(f"enjoy your {drink_name} 😊")



is_on=True

while is_on:
 choice=input("What would you like? (espresso/latte/cappuccino):")
 if choice=="off":
     is_on=False
 elif choice=="report":
     print(f"Water:{resources['water']}ml ")
     print(f"Milk: {resources['milk']} ml")
     print(f"Coffee:{resources['coffee']}g")
     print(f"Money: ${profit}")
 else:
     drink = MENU[choice]
     if is_resource_sufficient(drink["ingredients"]):
         payment =process_coin()
         if transaction_successfull(payment,drink["cost"]):
             make_coffee(choice,drink["ingredients"])




# windows key + . gives emoji keyboard