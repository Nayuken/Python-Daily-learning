#Digital coffee machine
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

resources = {
    "water": 300,
    "milk": 100,
    "coffee": 24,
    "money": 0,
}
#TODO 1. Resource check function based on above dictonary
def check_Resources(bev_name):
    #Checks the coffee machine to make sure it has enough coffee and water
    if resources["water"] < MENU[str(drinkSelect)]["ingredients"]["water"]:
        print("There is not enough water for this drink, please select another.\n")

    elif resources["coffee"] < MENU[str(drinkSelect)]["ingredients"]["coffee"]:
        print("There is not enough coffee for this drink, please select another.\n")

    #Milk check for the drinks that include milk
    elif drinkSelect == str("latte") or drinkSelect == str("cappuccino") and resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
        print("There is not enough milk for this drink please select another drink.\n")

    #if all resources are avaliable will print a thank you statement
    else:
        print("Your total today will be: $" + str(MENU[str(drinkSelect)]["cost"]))
        print("please insert coins.")
        coin_counter()
        resource_Counter()

#TODO 2. Create coin counter function to calculate coins total amount
def coin_counter():
    q_Check = input("How many quarters?: ")
    d_Check = input("How many dimess?: ")
    n_Check = input("How many nickels?: ")
    p_Check = input("How many pennies?: ")
    coin_Total = (float(q_Check) * .25) + (float(d_Check) * .10) + (float(n_Check) * .05) + (float(p_Check) * .01)
    if coin_Total < MENU[str(drinkSelect)]["cost"]:
        print("Sorry that's not enough money. Money refunded\n")
    else:
        change_total = coin_Total - MENU[str(drinkSelect)]["cost"]
        coffee_Revenue = coin_Total - change_total
        resources["money"] = +coffee_Revenue
        print("You paid: $" + str(coin_Total) + ". Your change back is: $" + str(round(change_total,2)))

#TODO 3. resource counter function to deducte resources after payment has been confirmed
def resource_Counter():
    if resources["water"] > MENU[str(drinkSelect)]["ingredients"]["water"]:
        resources["water"] = resources["water"] - MENU[str(drinkSelect)]["ingredients"]["water"]

    if resources["coffee"] > MENU[str(drinkSelect)]["ingredients"]["coffee"]:
        resources["coffee"] = resources["coffee"] - MENU[str(drinkSelect)]["ingredients"]["coffee"]

    if drinkSelect == str("latte") or drinkSelect == str("cappuccino") and resources["milk"] > MENU["latte"]["ingredients"]["milk"]:
        resources["milk"] = resources["milk"] - MENU[str(drinkSelect)]["ingredients"]["milk"]

    print("Here is your " +str(drinkSelect)+". Enjoy!\n")

#TODO 4. Coffee maker choice selection portion
print("What would you like to drink? (espresso/latte/cappuccino):")
drinkSelect = input()
#Keeps loop working as long as the input "off" is never entered.
while drinkSelect != str("off"):
        # Checks to see if input above matches cases, in this situation coffee options, it also uses the options as reference in the function above to check if input matches a dictonary key
        if drinkSelect == str("espresso") or drinkSelect == str("latte") or drinkSelect == str("cappuccino"):
            print("You have selected an " + drinkSelect + ' hot beverage.')
            check_Resources(drinkSelect)
            print("Please select another beverage: (espresso/lattee/cappuccino)")
            drinkSelect = input()

        # Checks input for "report" entry and prints out the resource dictonary key in response if it matches once done returns user to loop
        elif drinkSelect == str("report"):
            print("Resources currently avaliable:\n" + str(resources))
            print("\nPlease select a beverage option: (espresso/lattee/cappuccino)")
            drinkSelect = input()

        # Makes sure that no other inputs can proceed and returns user to original loop
        elif drinkSelect != str("off") or drinkSelect != str("report") or drinkSelect != str(
                "espresso") or drinkSelect != str("latte") or drinkSelect != str("cappuccino"):
            print("Please select a beverage option ONLY: (espresso/lattee/cappuccino)")
            drinkSelect = input()

        # exits our loop
        elif drinkSelect == str("off"):
            exit()
#Once exited from loop prints out shut off message
print("Coffee maker shutting off")

