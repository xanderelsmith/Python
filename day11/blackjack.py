import random


cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]

def deal_card():
    """returns a random card from the deck"""
    chosenCard=random.choice(cards)
    return chosenCard


def compare(u_score,c_score):
    if u_score==c_score:
        print('Draw 🙃')
    elif u_score==0:
        print('User Wins a blackjack 😁,')
    elif c_score == 0:
        print('Computer Wins a blackjack 🤖,')
    elif u_score>21:
        print('user goes over, Computer wins 🤖')
    elif c_score>21:
        print('computer lose,you win')
    elif u_score>c_score:
        print('user wins')
    else:
        print('you lose,Computer wins')
    
    
    
def calculate_score(cardsList: list):
    """Takes a list of cards and returns the score calculated as Cards"""
    if  sum(cardsList)==21 and len(cardsList)==2:
        # blackJACK!!!!!!
        return 0
    if 11 in cardsList and sum(cardsList)>21:
        cardsList.remove(11)
        cardsList.append(1)    
           
    return sum(cardsList)
       
def playGame():
    userCards=[]
    computerCards=[]   
    # deal the user and computer 2 cards each using deal_cards and append




    isGameOver = False


    for _ in range(2):
        userCards.append(deal_card())
        computerCards.append(deal_card())
    

    while not isGameOver: 
        computer_score = calculate_score(computerCards)   
        userScore=calculate_score(userCards)
        print(f'my card {userCards} and score: {userScore}')
        print(f'computer\'s first card {computerCards[0]}')

        if userScore==0 or computer_score==0 or userScore>=21:
            isGameOver=True 
        else:
            usershouldeal = (input("Type 'y' to get another card,type 'n' to pass :")).lower()
            if usershouldeal=='y':
                userCards.append(deal_card())            
            else:
                isGameOver=True


    while computer_score < 17 and computer_score != 0:
        computerCards.append(deal_card())
        computer_score = calculate_score(computerCards)
    
    
    print(f'you dealt  a hand of {userScore} while computer, {computer_score}')
    compare( u_score=userScore,c_score=computer_score)

while input("Do you want to play a game of BlackJack ,'y' or 'n':\t")=='y':
    print('\n'*23)
    playGame()