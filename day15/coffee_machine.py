from data import MENU, resources


water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0
isDispensing = True


def check_transaction_successfull(selectedDrink, money):
    if money < MENU[selectedDrink]['cost']:
        print(
            "Sorry that's not enough money. Money refunded. Type 'balance' to view balance")
        return False
    elif money > MENU[selectedDrink]['cost']:
        change = round(money - MENU[selectedDrink]['cost'], 2)
        print(
            f"Transaction successfull!, Here is ${change} dollars in change.")
        return True
    else:
        print("Transaction successfull!")
        return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.10
    total += int(input("How many nickles?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total


while isDispensing:
    selectedDrink = input(
        'What would you like? (espresso/latte/cappuccino)\t',).lower()
    if selectedDrink == 'off':
        isDispensing = False
        print('Thank you for using our coffee machine!')
    elif selectedDrink == 'report':

        print(f'Water: {resources['water']}ml')
        print(f'Milk: {resources['milk']}ml')
        print(f'Coffee: {resources['coffee']}g')
        print(f'Money: ${money}')
    elif selectedDrink == 'balance':
        print(f'You have ${money} left')

    elif selectedDrink != 'latte' and selectedDrink != 'cappuccino' and selectedDrink != 'espresso':
        print('Not a valid selection')
    elif money < MENU[selectedDrink]['cost']:
        print(MENU[selectedDrink]['cost'])
        print("You dont have enough money. Type 'balance' to view balance")
        money = process_coins()
        money = check_transaction_successfull(selectedDrink, money)

       

    elif (MENU[selectedDrink]['ingredients']['water'] > water):
        print("You don't have enough water!")
    elif (MENU[selectedDrink]['ingredients']['milk'] > milk):
        print("You don't have enough milk!")
    elif (MENU[selectedDrink]['ingredients']['coffee'] > coffee):
        print("You don't have enough coffee!")
    else:
        water = water - MENU[selectedDrink]['ingredients']['water']
        milk = milk - MENU[selectedDrink]['ingredients']['milk']
        coffee = coffee - MENU[selectedDrink]['ingredients']['coffee']
        money = money - MENU[selectedDrink]['cost']
        resources['water'] = water
        resources['milk'] = milk
        resources['coffee'] = coffee
        print(f'Here is your {selectedDrink}. Enjoy!')
