#Quiz game:
questions = (
    "What is your name?: ",
    "What is your age?: ",
    "How old are you?: ",
    "How old are you?: ",)
opinions = (("A.123", "B.578", "C.456", "D.852"),
            ("A.123", "B.578", "C.456", "D.852"),
            ("A.123", "B.578", "C.456", "D.852"),
            ("A.123", "B.578", "C.456", "D.852"))
answers = ("C",
           "A",
           "B",
           "C")
guesses = []
score = 0
question_num = 0
for question in questions:
    print("-------------------------")
    print(question)
    for opinion in opinions[question_num]:
        print(opinion)

    guess = input("Enter your guess: ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print(f"{answers[question_num]} was wrong.")
        print("Incorrect!")
    question_num += 1

print("-------------------------")
print("         RESULT          ")
print("-------------------------")

print("Answers: ", end=' ')
for answer in answers:
    print(answer, end=' ')
print()
print("Gusses: ", end=' ')
for guess in guesses:
    print(guess, end=' ')
print()

score=int(score /len(guesses)*100)
print(f'Your score is {score}%')