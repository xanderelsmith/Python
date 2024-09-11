import random
word_list=["aadvark","crocodile","fish"]


chosenword = random.choice(word_list)
print(chosenword)
placholder=''
for textindex in range(0,len(chosenword)):
   placholder+='_'
print(placholder)
# TODO-1 - Create a "placeholder" with the same number of blanks as 

guess=input('Guess a letter:\t').lower()
# TODO-2 - Create a "display" that puts the guess letter in the right 

print(guess)
placeholder=''
for textindex in range(0,len(chosenword)):
    text = chosenword[textindex].lower()
    if(guess==text):
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
    

