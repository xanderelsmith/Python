import random


cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    """returns a random card from the deck"""
    chosenCard=random.choice(cards)
    return chosenCard
    
userCards=[]
computerCards=[]   
# deal the user and computer 2 cards each using deal_cards and append



def calculate_score(cardsList: list):
    """Takes a list of cards and returns the score calculated as Cards"""
    if 21 in cardsList and len(cardsList)==2:
        # blackJACK!!!!!!
        return 0
    elif 11 in cardsList and sum(cardsList)>21:
        cardsList.remove(11)
        cardsList.append(1)    
           
    return sum(cardsList)

isGameOver = False

for _ in range(2):
    userCards.append(deal_card())
    computerCards.append(deal_card())
      
userScore=calculate_score(userCards)
print(f'{userCards}  {userScore}')
print(f'{computerCards[0]}')

if userCards==0 and computerCards==0 and userScore==21:
   isGameOver=True 
else:
    input('Do you want to draw another card:\t')