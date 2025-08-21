#Son topish o'yini
import random

lower_num = 1
high_num = 10
answer = random.randint(lower_num, high_num)
guesses = 0
is_running = True
while is_running:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess > high_num or guess < lower_num:
            print("That number is out of range")
            print(f"Please select a number between {lower_num} and {high_num}")
        elif guess > answer:
            print("That number is too high")
        elif guess < answer:
            print("That number is too low")
        else:
            print(f"That number is correct {answer}")
            print(f"You guessed {guesses} correctly")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Please enter a number between {lower_num} and {high_num}")