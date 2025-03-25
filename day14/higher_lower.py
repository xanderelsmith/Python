from gamedata import data
import random


def getBiggerVar(data1, data2):
    if (data1>data2):
        return 'A'
    else:
        return 'B'
        
isGameOver=False
firstChoice= random.choice(data)
while isGameOver==False: 
    
    secondChoice = random.choice(data)
    print(f'Compare A:\t{firstChoice['name']},{firstChoice['description']},from {firstChoice['country']},')
    print(f'Against B:\t{secondChoice['name']},{secondChoice['description']},from {secondChoice['country']},')
    answer=input("Who has more followers? Type 'A' or 'B': ").lower()

    if (answer==getBiggerVar(firstChoice['follower_count'],secondChoice['follower_count']).lower()):
        print('SuccessFul')
        if(answer!='a'):
            firstChoice=secondChoice
    else:
        isGameOver=True
        print('GameOver')
        
