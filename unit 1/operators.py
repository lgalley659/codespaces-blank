# Operators
# Operators are a construct (build in system) that give 
# data types more actions and power

# Arithmetic Operator family
# Arithmetic Operators are simply math operators
# We use mathem,atical symbols such as the addition, substraction,
# Multiplication and division signs to do operations.

print(2 + 3)
print( 20 - 100)
print(40 / 2)
print(30.9 * 10)

#Assignment Operator Family
# These Operators assign values to variables
# (other wise known as containers)
# key - value pairs

# variables = container

schoolName = "Boys Latin "
age = 16

age += 1.5

age -= 3

number = 3
 print(age + number) #19

print(age)

#Logical Operator family
# It checks and compares if certain code conditions are true

print(3 > 1 and "Ian == Ian")
# the AND operator checks to see both condition are true
#if both are true the answer is true

print(2 == 1 or 3 < 2)
# The or operator checks if one of the conditions is true 
# So long as one of the condition is true, it will be true

print(not(3 > 1 and "lumen" and "lumen")) # false
# The NOT operator will give opposit the result.
 # the NOOT operator flips the result.

algebraPassed = True
historyPassed = True

# does this person need credit recovery
# true means they passed
 print(not(algebraPassed== True and historyPassed ==True))
