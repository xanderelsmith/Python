import random
from art import logo
print(logo)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100')
inputData =input('Choose a difficulty. Type \'easy\' and \'hard\':\t').lower()
easy=10
hard=5
selectedLevel=0
if inputData=='easy':
    selectedLevel=easy
else:
    selectedLevel=hard
    
selectedNumber=random.choice(range(1,100))
guess=0
while selectedNumber!=guess:
        for data in range(0,selectedNumber):
            print(f'You have {selectedLevel} attempts remaining to guess the number')
            guess=int(input('Make a guess:\n'))
            if guess==selectedNumber:
                print('You guessed the number!')
                break
            elif guess>selectedNumber:
                print('You selected a bigger number')
                selectedLevel-=1
            else:
                print('you selected a smaller number')
                selectedLevel-=1  
                  
if selectedLevel>0:
    print('GameOver')
    
   