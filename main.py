import random

score = 0
rounds = 0
name = ""
question_and_answers = {
    "What is the capital of Canada?": "Ottawa",
    "How many continents are there in the world?": "7",
    "What is the largest mammal on Earth?": "Blue Whale",
    "Who wrote 'Harry Potter and the Philosopher's Stone'?": "J.K. Rowling",
    "What is the currency of Japan?": "Yen",
    "In which year did the Titanic sink?": "1912",
    "What is the chemical symbol for gold?": "Au",
    "Which planet is known as the 'Red Planet'?": "Mars",
    "What is the square root of 144?": "12",
    "Who is known as the 'Father of Computer Science'?": "Alan Turing"
}


def welcome_user():
    global rounds
    global name
    name = input("Enter your name...\n")
    print(f"Welcome {name}!\n")
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? \n"))
            if rounds > 0:
                break
            else:
                print("Please enter a positive number.\n")
        except ValueError:
            print("Please enter a valid integer.\n")


def generate_questions():
    global score
    random_question = random.choice(list(question_and_answers.keys()))

    print(f"\n{random_question}")
    user_answer = input("Your answer: ")
    correct_answer = question_and_answers[random_question]

    if user_answer.lower() == correct_answer.lower():
        score += 1
    else:
        print(f"\nIncorrect. Correct Answer: {correct_answer}")


welcome_user()

for i in range(rounds):
    generate_questions()

print(f"\nThanks for playing, {name}! Your final score is: {score}/{rounds}")
