alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','w','y','z']

direction= input("Type 'encode' to encrypt, type 'decode' to decode:\n ").lower();
shift=int(input("Type the shift number: \n"))


# TODO-1: Create a function called 'encrypt()' that takes "Original_text" and "Shift_amount" as 2 inputs.
def ceaser(original_text,shift,encode_decode=direction):
    encryptedtext=''      
    for text in original_text:
        currentIndex=alphabet.index(text)
        if(encode_decode=='decode'):
            data=currentIndex+shift
        else:
            data=currentIndex-shift 
        encryptedtext+=alphabet[data%len(alphabet)]
    print(encryptedtext)
    return encryptedtext
    
#TODO-2: Inside the "encrypt" function, shift each letter of the "original_text" forwards in the alphabet
# by the shift amount and print the encrypted text.

#TODO-4: What happens if you try to shift 2 forwards by 9? Can you fix the code?

#TODO-3: Call the "encrypt()" function and pass in the user inputs. You should be able to test the code and encrypt a message
encryptedText=ceaser('HelloWorld'.lower(),shift,encode_decode=direction)
