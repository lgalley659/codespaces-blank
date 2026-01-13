import random

#Function needs to have a list of 4 words/ strings
#Function needs to randomly select one of the words/ strings from the list
def scrembleWordGame():
    wordPool = ["Pennsylvania", "North carolina "]
    print('welcome to word scramble!')

    randomWordSelect = random.randint(0,3)
    correctword = ''

    if randomWordSelect == 00:
        correctword = wordPool[0]
    elif randomWordSelect == 1:  
        correctword = wordPool[1]
    elif randomWordSelect == 2:    
        correctword = wordPool[2]
    elif randomWordSelect == 3:
        correctword = wordPool[3]
   
    convertedSelection = list(correctword)
    random.shuffle(convertedSelection)
    scrambled = "".join(convertedSelection)

    print("Geuss the correct word: " + scrambled)
    userGeuss = input()


    while userGuess != correctword: 
           userGuess = input("Enter your guess: ")
           if userGuess == correctword:
            print("Correct!")
           else:
            print("Try again.")
    