from data import MENU, resources


water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0
isDispensing = True
print(resources)
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
    elif money<MENU[selectedDrink]['cost']:
        print("You dont have enough money. Type 'balance' to view balance")
        money=int(input('Please input coins to make purchase:\t'))
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
        money=money - MENU[selectedDrink]['cost']
        resources['water'] = water
        resources['milk'] = milk
        resources['coffee'] = coffee
        print(f'Here is your {selectedDrink}. Enjoy!')
