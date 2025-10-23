# create a funcionk
# take in user input
# if the word entered is built=inn
# print the list of numbers.

def numberLooper():
    numberInput = input("Please enter a number: " )
    numberList = []

    while numberInput != "quit":
        numberList.append(numberInput)
        print(numberList)
        numberInput = input("Please enter a number: " )
        print('code is working= able to enter numbers')
    else:
        print('loop has ended')
        print('code is working- able to quit')


numberLooper()
 


def numberListLoop():
    numberList = []
    userNumber =  input("Type in a number: ")
    while userNumber != 'quit':
        newNumber = int(userNumber)
        numberList.append(newNumber)
        print(numberList)
    else:
        print("Loop has stopped.")

numberListLoop()


def numberloop():
    numberList = []
    userInput = str(input(1))
    while userInput != "built-in":
        numberList.append(userInput)
        print(numberList)
        userInput = str(input(1))
    else:
        print("You have exited the loop.")
    
