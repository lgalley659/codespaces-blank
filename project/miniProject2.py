
def GPA():
    print("What is subject area")
    subject = input()
    print("What is the grade for week 1") 
    grade = input()
    print("What is the grade for week 2")   
    grade = input()
    print("What is the grade for week 3")      
    grade = input() 
    print("What is the grade for week 4")
    grade = input()
    print("What is the grade for week 5")
    grade = input()
    print("What is the grade for week 6")
    grade = input()
    print("What is the grade for week 7")
    grade = input()
    print("What is the grade for week 8")
    grade = input()
    print("What is the grade for week 9")
    grade = input()
    print("What is the grade for week 10")
    grade = input()
    print("What is the grade for week 11")
    grade = input()
    print("What is the grade for week 12")
    grade = input()
    print("What is the grade for week 13")
    grade = input()
    print("What is the grade for week 14")
    grade = input()
    print("What is the grade for week 15")
    grade = input()
    print("What is the grade for week 16")
    grade = input()
    print("What is the grade for week 17")
    grade = input()

def calculate_gpa():
    grades = []
   
    if GPA >= 90:
        letter_grade = "A"
    elif GPA >= 80:
        letter_grade = "B"
    elif GPA >= 70:
        letter_grade = "C"
    elif GPA >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
   
print("GPA")
print("letter grade")


def gpaCalculator():
    print('What subject is this GPA for? ')
    subject=  input()
    print('the user typed in: ' + subject)

    sum= 0
    weekcount= 1
    for x in weekcount in range (1,17):
        print(x)
        print('What is your grade for week ' + str(weekcount) + '?')
        grade= int(input())
        finalSum += grade
        weekcount += 1
        gpa = sum / weekcount
        print('your gpa is :' + str(gpa))
        if gpa > 70 and gpa <80:
            print("C")
        elif gpa > 80 and gpa<90:
            print("B")
        elif gpa > 90 and gpa < 100:
            print("A")  
gpaCalculator()


