import random

def  getRandomWord():
    '''this function generate a word of length 3 with random alphabats'''
    
    sample = "abcdefghijklmnopqrstuvwxyz"
    word=""
    for i in range(0,3):
        word = word + sample[random.randint(0,25)]
    return word


def decodedWord(word):
    ''' this function is removing word of lenth 3 from starting and at end that we add while encrypting it and also remove the last alphabat and add it in front'''
    
    newWord = word[3:-3]
    return newWord[-1]+ newWord[0:-1]

def decodeMessage(mes):
    result = ""
    for word in mes:
        if(len(word)<3):
            reWord=word[::-1] #reversing the word
            result = result + " " + reWord  
        elif(len(word)>=3):
            result = result + " " + decodedWord(word)
    result  = result.strip() # removing extral space if occur while converting
    print(result)


def encryptionWord(word):
    '''this function is adding a word of lenth 3 in starting and end with random alphabat and also removing first alphabat of actual word and adding it at end '''
    return  getRandomWord()+word[1:] + word[0] + getRandomWord()

def encryptionMessage(mes):
    result = ""
    for word in mes:
        if(len(word)<3):
            reWord=word[::-1] #reversing the word
            result = result + " " + reWord

        elif(len(word)>=3):
            result = result + " " + encryptionWord(word)
    
    result  = result.strip() # removing extral space if occur while converting
    print(result)

    

choice = int(input('what you wont to do \n type: "0" for encryption and "1" for decode:\n'))
message = input("Enter the message:\n")

if(choice == 0):
    encryptionMessage(message.split())
elif( choice == 1):
    decodeMessage(message.split())