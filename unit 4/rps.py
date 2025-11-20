# Requirements for Rock-Paper-Scissors Game: Having 3 options to choose from (rock, paper, scissors) 
#determining if you win, lose or tie. 

"we could use strings to represent the options"
"we can use a loop to keep the game going"

import random
def rps():
    options = ['rock', 'paper', 'scissors']
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(options)
    print("Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors'):
         print("You win!")
    elif (user_choice == 'scissors' and computer_choice == 'paper'):
         print("You win!")
    elif (user_choice == 'paper' and computer_choice == 'rock'):
         print("You win!")
    else:
        print("You lose!")

"Step 1: welcome the user to the game"
"Step 2: give them the option to play the game or see the game rules"
"step 3: if the user selects rules, show them the rules, else start the game"
"step 4: Inform the user the gamer has started and ask them to make a selection; R,P,S"
"step 5:computer makes a random selection"
"step 6: determine the user/ player if they won, lose, or tied"
'and keep track of score and round'
"step 7:(LOOP) Show the user the RPS options and they will continue to play up until round 4"
"step 8: Determine and inform the user if they won and return them to the main menu"

def rpsGame():
     print("welcokme to Rock Paper Scissors: the gane!")
     print('Please select one of the following:')
     print('Enter p to start game,')
     print('Enter r to see the rules,')
     selection = input()
     if selection == "n":
          print("here are the game rules...")
     elif selection == "p":
          print('the game is starting...')
          choice = input("please mke a selection, r= rock, p= paper, s= scissors: ")
          choiceCPu = random.choice(rpsOptions_cpu)
          #make a way to show the full selection word; examples: if s
          # the program should print scissors
          if choiceUser == 'r':
               selectwWord = 'rock'
          elif choiceUser == 'p':
               selectwWord = 'paper'
          elif choiceUser == 's':
               selectwWord = 'scissors'
               
          print('user selected: ' + choiceUSer)
          print('cpu selected: '+ choiceCPu)
     else:
          print("sorry, we didn't understand your entry.")


rpsGame()
