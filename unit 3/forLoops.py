# For Loops - A type of construct that runs code 


halloweenCandy = ['snickers', 'starburst', "m&m's"]
for i in halloweenCandy:
    print(i)

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    multi= i * 3
    div=multi / 1.5
    print('These are the numbers multiplied by 3 and divided by 1/2:', str(div))


for i in range(0,50):
    print(i)

while range(0,50):
    print('x')

# use a for loop to ask a user to type in 5 words and print eatch word out in
# the terminal. Once the user has finished typing 5 words,
# the for loop should end.

#Clarification program should ask the user to type in one word. Then the program
# should print it out and ask them to type another word. Your program
# should do this 5 times.

#Hint # 1: you should use the range() function.
for x in range(5):
    word = print('please type in a word:')
    print(word)

#looping through strings
word = 'Python'
for letter in word:
    print(letter)
    if letter == "p":
        print("did you mean paper? ")
    elif letter == "y":
        print('did you mean') 

#looping through lists of numbers
shoppingPrices = [3.00, 5.40, 7.20, 9.00]
total = 0
for items in shoppingPrices:
    total += items
    
print(total)


studentBody = ['a', 'b', 'c']
present = []
tardy = []
absent = []
for student in studentBody:
    #if scanned in add to present list
    # present ,append(student)
    # else add to absent list
    # absent.append(student)
    print('these students are present: ')
    print(present)
    print('these students are absent: ')
    print(absent)


