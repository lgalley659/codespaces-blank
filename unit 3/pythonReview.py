# 1.  A program that determines if a student has submitted their classwork.

def hasSubmitted(classwork_list, student_name):
    if student_name in classwork_list:
        return True
    else:
        return False
    
# 2. Create a function that will take in a string as an argument and output 
# that string in reverse order.

def my_function(x):
    return x[::-1]
mytxt = "Can this text go backwards"
print(my_function(mytxt))

3. # Create a number guessing function where the program will continuously 
# ask the user to enter a number until the guess the number correctly. 

def numberGuessingGame():
    correct_number = 42
    attempts = 0
    while True:
        user_guess = int(input("Please guess a number: "))
        attempts += 1
        if user_guess < correct_number:
            print("Your guess is too low. Try again.")
        elif user_guess > correct_number:
            print("Your guess is too high. Try again.")
        else:
            print(f"Congratulations! You've guessed the correct number {correct_number} in {attempts} attempts.")
            break

numberGuessingGame()