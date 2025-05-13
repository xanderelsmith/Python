from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffeeMaker=CoffeeMaker()
moneyMachine=MoneyMachine()
menuConfig = Menu()
isDispensing = True
while isDispensing:
    choice=input( 'What would you like? (espresso/latte/cappuccino):\t',).lower()
    if choice == 'off':
        isDispensing = False
        print('Thank you for using our coffee machine!')
    elif choice =='report':
        coffeeMaker.report()
        moneyMachine.report()
    else:    
        drinkData=menuConfig.find_drink(choice)        
        if coffeeMaker.is_resource_sufficient(drink=drinkData) and moneyMachine.make_payment(drinkData.cost):
            coffeeMaker.make_coffee(drinkData)
            
                
            
    