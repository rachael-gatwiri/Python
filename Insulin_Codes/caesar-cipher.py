# Define a function called getDoubleAlphabet that takes a string argument and concatenates, or combines, the given string with itself
def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet


# The next function you define will request a message to encrypt from the user.
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt


#Getting a cipher key
"""
The cipher key is how far you will shift the letters. 
By using two alphabets, you can have a cipher key that is any integer from 1 to 25. 
Don’t count the key at index 26 because that key would shift you back to the original message.
"""
def getCipherKey():
    shiftAmount= input("Please enter a key (whole number from 1-25): ")
    return shiftAmount


# Encrypting a message
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = ""
    uppercaseMessage = ""
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        position = alphabet.find(currentCharacter)
        newPosition = position + int(cipherKey)
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else:
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage


# Decrypting a message
"""
Functions are useful because you can reuse them.
You will write a decryptMessage() function by reusing the encryptMessage() function. 
For this simple encryption, you can undo the encryption by shifting each letter back. 
Thus, instead of adding the cipher key, you will subtract the cipher key. 
To avoid rewriting most of the logic, you will pass in a negative cipher key.
"""
def decrypteMessage (message, cipherKey, alphabet):
    decryptKey = -1 * int (cipherKey)
    return encryptMessage(message, decryptKey, alphabet)


# Creating a main function
def runCaesarCipherProgram():
    myAlphabet = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
    print(f'Alphabet : {myAlphabet}')

    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alphabet2: {myAlphabet2}')

    myMessage = getMessage()
    print(myMessage)

    myCipherKey = getCipherKey()
    print(myCipherKey)

    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')

    myDecryptedMessage = decrypteMessage(myEncryptedMessage, myCipherKey, myAlphabet)
    print(f'Decrypted Message: {myDecryptedMessage}')

runCaesarCipherProgram()
#To help with debugging and understanding the program, print() statements were added, but they are not strictly necessary for the program to operate correctly.





