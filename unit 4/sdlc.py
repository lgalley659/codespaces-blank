
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
