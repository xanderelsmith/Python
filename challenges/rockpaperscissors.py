import random
playerchoice =int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
rock='rock'
paper='paper'
scissors='scissors'
choices=[rock, paper,scissors]
if playerchoice<len(choices):
    print(f'you chose {choices[playerchoice]}')

computerchoice=random.randint(0,len(choices)-1)
print(f'computeer chose {choices[computerchoice]}')
if playerchoice>len(choices)-1:
    print('Invalid Input')
elif computerchoice==2 and playerchoice==0:
    print('You won')
elif playerchoice>computerchoice:
    print('You Won')
elif playerchoice==computerchoice:
    print('Its a draw')

else:
    print('Computer won')

