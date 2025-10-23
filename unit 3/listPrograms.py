FourFoods =["Taco", "Pizza", "Burgers", "Pasta"]
print(FourFoods[0])
print(FourFoods[3])

FourFoods[1] = "Sushi"
print(FourFoods)

FourFoods.pop(2)
print(FourFoods)

FourFoods.insert(2, "Salad")
print(FourFoods)


def resturantMenu():
    print("What time of day are you ordering?")
    selection = input("Please select what the time of day")
    print("1. morning")
    print("2. afternoon")
    print("3. night")
    time = int(input())
    if time == "morning":
        print("Youve selected the morning menu")
    elif time == "afternoon":
        print("Youve selected the afternoon menu")
    elif time == "night":
        print("Youve selected the night menu")
    else:
        print("Sorry, I dont understand your selection")
        resturantMenu()
        

number = 0
while number < 10:
    number += 1
    print(number)
else:
    print('Done counting')

timer = 30
while timer < 0: # needs to be true
    timer -=1
    print(timer)
else:  # if its false we get this
    print('Done counting down')