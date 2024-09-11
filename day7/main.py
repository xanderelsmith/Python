import random
word_list=["aadvark","crocodile","fish"]

# TODO-1 -Rmotely choose a word from the word-list and assign to a variable
index=random.randrange(0,len(word_list)-1)
chosenword = word_list[index]
print(chosenword)
# TODO-2 - Ask the User to guess a letter and assign the variable the answer to a variable called guess. Make guess lowercase
guess=input('Guess a letter:\t')
print(guess.lower())
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it is 
# "wrong" if it's true
if (chosenword.__contains__(guess)):
    print('true')
else:
    print('False')
    

