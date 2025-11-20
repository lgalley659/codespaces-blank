
def signup():
    dob = int(input(' What year were you born? '))
    tiktok_kids = []
    tiktok_teens = []
    tiktok_standard = []
    currntYr = 2025
    userAge = currntYr - dob
    if userAge > 8 and userAge < 12:
        print('Welcome to tiktok kids')
        tiktok_kids.append(userAge)
    elif userAge > 12 and userAge < 18:
        print('Welcome to tiktok teens')
        tiktok_teens.append(userAge)
    else:
        print('Welcome to standard tiktok')
        tiktok_standard.append(userAge)
signup()



# Step 1. ideation - what features should you have in your calculator app?
# Please write the 3 or 4 features as strings.
feature1 = "Addition"
feature2 = "Subtraction"
feature3 = "Multiplication"
feature4 = "Division"
print("Welcome to the Calculator App!")

# step 2. analysis and requirements - how would you code out your calculator
# Please write atleast 1 function for 1 of your features.
def addition(num1, num2):
    return num1 + num2
def subtraction(num1, num2):
    return num1 - num2
def multiplication(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error! Division by zero."

def add():
    num1 = int(input("Please type in a number: "))
    num2 = int(input("Please type in another number: "))
    sum = num1 + num2
    print(sum)
    bonusNum = int(input("would you like to add another number to the sum?:" ))
    if bonusNum: == 'y':
             numX = int(input("Please type in number: "))
             sum += numX
             print(sum)

        
