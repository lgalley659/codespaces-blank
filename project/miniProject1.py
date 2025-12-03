
 
def quiz():
    questions =
        
        [   ("question 1": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C"),
    
           ("question 2": "What is 2 + 2?",
            "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
            "answer": "B"),

           ("questio 3": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Saturn", "D) Mars"],
            "answer": "B"),
        
            ("question 4": "How many oceans are there on Earth?",
            "options": ["A) 7 ", "B) 4 ", "C) 5 ", "D) 11"],
            "answer": "C"),
            ("question 5": "What is the boiling point of water?",
            "options": ["A) 90°C", "B) 100°C", "C) 110°C", "D) 120°C"],
            "answer": "B") ]


        questions:
        print(["question"])
        for option in ["options"]:
            print(option)
        user_answer = input("Please enter your answer (A, B, C, or D): ").
        
        if user_answer == ["answer"]:
            score += 1
            print("Correct!")
        else:
            print("Wrong! The correct answer was (['answer']).")

    print("You got (score) out of (questions) correct.")

while True:
    quiz()
    retry = input("Do you want to retry the question? (yes/no): ").lower()
    if retry != 'yes':
        print("Thank you for playing!")
        break

def quiz():