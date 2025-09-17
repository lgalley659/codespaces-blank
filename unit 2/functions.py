# Function -  a function is a set of code instructions 
# for a computer to follow.

# a function comes in 2 phases

# phase 1: function definition
# we are describing the instructions on what we want
# this code to do.it only runs when we call it.

def example(): 
    print('Good Morning')

def example2():
    print('good day')

# phase 2: function call/invocation
# when we are ready to use a function,
# we write it to use it.
example()
example2()

def math():
    a = input ('enter a number: ')
    b = 10    
    print(int(a) + b)

math()

# phase 1: function definition
# we are describing the instruction for our custom code.
# we are adding logic to the comuters vocabulary.
# this code does not run- it only gives it meaning
# not the action.
 
# we indent to inform the computer that we are about to write 
# code instructions. If we dont, we will get an error.

# Create a function that calculates 2 unique user inputed

def calculate():
    a = input('Please enter a number: ')
    b = input('Please ender another number: ')
    print(int(a) + int(b))
    print(int(a) - int(b))
    print(int(a) / int(b))
    print(int(a) * int(b))
    print(int(a) % int(b))
    print(int(a) ** int(b))
    print(int(a) // int(b))

calculate()