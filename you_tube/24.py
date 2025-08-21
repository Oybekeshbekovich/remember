#Hangman->so'z topish o'yini
from wordlist import word
import random

hangman_art = {
    0: ("   ",
        "   ",
        "   "),
    1: (" 0 ",
        "   ",
        "   "),
    2: (" 0 ",
        " | ",
        "   "),
    3: (" 0 ",
        "/| ",
        "   "),
    4: (" 0 ",
        "/|\\",
        "   "),
    5: (" 0 ",
        "/|\\ ",
        "/  "),
    6: (" 0 ",
        "/|\\",
        "/ \\")
}


def display_man(wrong_guess):
    print('*******************')
    for line in hangman_art[wrong_guess]:
        print(line)
    print('*******************')


def display_hint(hint):
    print(' '.join(hint))


def display_answer(answer):
    pass


def main():
    answer = random.choice(word)
    hint = ['_'] * len(answer)
    wrong_guess = 0
    guessed_letters = set()
    is_running = True
    while is_running:
        display_man(wrong_guess)
        display_hint(hint)
        guess = input('Enter your guess: ').lower()

        if len(guess) != 1 or not guess.isalpha():
            print('*******************')
            print('You guessed wrong letters. Try again!')
            continue
        if guess in guessed_letters:
            print(f'{guess} is in the word!')
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess.lower()
            print('You guessed the word!')
        else:
            wrong_guess += 1
        if "_" not in hint:
            display_man(wrong_guess)
            display_answer(answer)
            print('YOU WIN!')
            is_running = False
        if wrong_guess >= len(hangman_art) - 1:
            display_man(wrong_guess)
            display_answer(answer)
            print('YOU LOSE!')
            print(f'The orginal word is: {answer}')
            is_running = False


if __name__ == '__main__':
    main()