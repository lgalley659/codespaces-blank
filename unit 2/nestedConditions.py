# Nested Conditions = a conditional statement that has other condition
# statements with it. Condition inside of condition.

def sandwhichStore():
    print("Welcome to Ian foods. What would you like.")
    selection = input('Please select your main food item.')
    print("1. meatball sandwich")
    print("2. turkey sandwhich")
    print("3. honey turkey sandwhich")
    print("4. buffalo chicken")
    print("5. surprise me (mystery sandwhich)")
    selection = input("please select your main food item")
    if selection == 1:
        print("youve selected the meatball sandwhich")
        print("what sides do you want")
        print("1. fries")
        print("2. salad")
        print("3. chips")
        side = int(input())
        if side == 1:
            print("great meatball and fries")
        elif side == 2:
            print("healthy! meatball and salad")
        elif side == 3:
            print("nice, meatball and chips")
        else:
            print("sorry, dont understand your side")
    if selection == 2:
        print("sorry we are out of the turkey sandwhich")
        sandwhichStore()

sandwhichStore()

def atm():
    balance = 2000
    pin = 1234

    userPin = input("Please type in your bank pin number")
    print("1. withdraw money")
    print("2. deposit money")
    print("3. check your balance")
    selection = input()
    if selection == 1:
        amount = int(input("How much do you want to take out?"))
        if amount > balance:
            print("Sorry, you dont have that much in your acount")
        else:
            newBalance = balance- amount
            print("your new balance is :" + str(newBalance))
    else:
        print("Sorry incorrect")
        atm()

# Python lists - a way to organize data regardless of data type.

# List Syntax- create a variable and then  assign it to square brasckets.
# write the data you want in your list in the square practice.
    

