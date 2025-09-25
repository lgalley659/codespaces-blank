# Conditional statements = code that has a set of different
# outcomes based on the data that is given.

# conditional syntax = if/ else
# If = The condition we are looking to satisfy
# Else = the default/ exit. The thing that happens
# when our condition is NOT satisfied
weather = input ("Whats the weather like today?")

if weather == 'sunny':
    print("Its gonna be nice out. Wear shades.")
elif (weather =='rainy'):
    print('Remember to bring an umbrella')
elif(weather == 'chilly'):
    print('Bring a jacket')
else:
    print("Have a good day.")

password = input("Please enter your password")

if password == input:
    print('Welcome! You are logged in.')
else:
    print('Incorrect password.')

down = 3
yards = 2

if down == 3 and yards == 2:
    print("")
elif down == 2 and yards < 0:
    print('')
elif down == 3 and yards > 6:
    print('')
else: # this is the exit; assumes it is 4th down.
    print("punt")

if down == 2 and yards == 10:
    print("Short pass")


def permitCheck(age):
    if age >= 16:
        print("Congrats, you can get your driver permit.")
    else:
        print("Sorry, not old enough")

def gradeChecker(grade):
    if grade >= 70:
        print("You passed the test.")
    elif("if a grade is above 70 and below 80"):
        print('Its a C.')
    else:
        print("Sorry, you failed")
