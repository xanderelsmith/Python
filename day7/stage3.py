import random
from wordlist import word_list
answerwordlist=[]
chosenword = random.choice(word_list).lower()
# print(chosenword)
# TODO-1 - Use a while loop to let the User guess again 

fields=''
for textindex in range(0,len(chosenword)):
   fields+='_'
print(fields)

answerstate=''
placeholder=''
while (placeholder!=chosenword):
    placeholder=''
    guess=input('Guess a letter:\t').lower()
    # TODO-2 - Change the for loop so that you keep the previous correct     
    for text in chosenword:
                      
        if guess==text:
            if (not answerwordlist.__contains__(guess)):
                answerwordlist.append(guess)
            
            placeholder+=guess
        elif(text in answerwordlist):
            placeholder+=text           
        else:
            placeholder+='_'
    print(placeholder)
    
    # TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is 
    # "wrong" if it's true
    if (chosenword.__contains__(guess)):
        print('true')
    else:
        print('False')
    
        

