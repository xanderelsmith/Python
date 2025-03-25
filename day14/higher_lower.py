from gamedata import data
import random


def getBiggerVar(data1, data2):
    if int(data1)>int(data2):
        return 'A'
    else:
        return 'B'
        
isGameOver=False
current_score=0
firstChoice= random.choice(data)
while not isGameOver: 
    
    secondChoice = random.choice(data)
    while secondChoice == firstChoice:
        secondChoice = random.choice(data)
    print(f'Compare A:\t{firstChoice['name']},{firstChoice['description']},from {firstChoice['country']},')
    print(f'Against B:\t{secondChoice['name']},{secondChoice['description']},from {secondChoice['country']},')
    answer=input("Who has more followers? Type 'A' or 'B': ").lower()

    if (answer==getBiggerVar(firstChoice['follower_count'],secondChoice['follower_count']).lower()):
        current_score+=1
        print(f'You\'re right! Current Score {current_score} \n\n\n')
        if(answer!='a'):
            firstChoice=secondChoice
    else:
        isGameOver=True
        print(f'Sorry, that\'s wrong. Final Score: {current_score}')
        
