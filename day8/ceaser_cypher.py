import pyfiglet

text = "caesar cipher 3"
ascii_art = pyfiglet.figlet_format(text)
print(ascii_art)
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','w','y','z']




# TODO-1: Create a function called 'encrypt()' that takes "Original_text" and "Shift_amount" as 2 inputs.
def ceaser(original_text,shift,encode_decode):
    encryptedtext=''      
    for text in original_text:
        
        currentIndex=alphabet.index(text)
        if(encode_decode=='decode'):
            shift*=-1
            
        data=currentIndex+shift
        
        encryptedtext+=alphabet[data%len(alphabet)]
    print(f"Here is the {encode_decode}d word:{encryptedtext}")
    return encryptedtext
    
    
wordInput=input("Input the word\n")   
direction= input("Type 'encode' to encrypt, type 'decode' to decode:\n ").lower();

shift=int(input("Type the shift number: \n"))
encryptedText=ceaser(wordInput.lower(),shift,encode_decode=direction)
