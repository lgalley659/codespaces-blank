#1. Create a function that will determine a persons letter grade based on the number entered
# for example: 98 = A+, 79 = C, 60 = F
#you can use input or a parameter to pass in your numbers.

def determine_letter_grade(score):
    if score >= 97:
        return "A+"
    elif score >= 93:
        return "A"
    elif score >= 90:
        return "A-"
    elif score >= 87:
        return "B+"
    elif score >= 83:
        return "B"
    elif score >= 77:
        return "C+"
    elif score >= 70:
        return "C-"
    elif score >= 67:
        return "D+"
    elif score >= 60:
        return "D-"
    else:
        return "F"
    
# 2. Create a function that will convert kilograms to pounds.
# 1 kilogram is roughly 2.2 pounds.
def kg_to_pounds(kg):
    pounds = kg * 2.2
    return pounds

#3. Create a function that will go through the list of school items and removes the following banned 
# items for the students backpacks.
# Your function should print out the new revised list with the banned items removed.
#Banned items: gum, soda, snacks.
def remove_banned_items(school_items):
    banned_items = {"gum", "soda", "snacks"}
    revised_list = [item for item in school_items if item not in banned_items]
    return revised_list    

school_items = ["notebook", "pencil", "gum", "soda", "backpack", "snacks", "calculator"]
revised_school_items = remove_banned_items(school_items)
print("Revised school items:", revised_school_items)    





