# List = A collection system for storing and organizing multiples
# pieces of data

# Lists syntax(how it is written)
# When we want to create a list, we first create a variable, and then
# assign it to the square brackets

shoppingList = ['apples','oranges','water',1,2,3,True,['bread','milk']]
print(shoppingList)

# if we want to access an item from a list, we use the index system.
# we write the lists variable name, and then use the brackets and pass in the
#number position

# list are zero based -indexed; meaning the list count always store at zero.(0)

print(shoppingList[4])

trunkParty = ['fan','mini-fridge','laptop','tv','air fryer']

def addItemForCollege():
    newItem = input("Please adda a new item to the college trunk party list.")
    list.append(newItem)
    print(list)

addItemForCollege(trunkParty)

trunkParty = ['fan','mini-fridge','laptop','tv','air fryer']
print(trunkParty)

numbersList = [100, 23, 450, 63, 1, 6, 19, 1000]
numbersList.append(67)
print(numbersList)

