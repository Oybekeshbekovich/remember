#SLOT MACHINE->Random moshina
import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]


def print_row(row):
    print('*****************')
    print('|'.join(row))
    print('*****************')


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0


def main():
    balance = 100
    print('*********************')
    print(' W e l c o m e ! ! ! ')
    print('*********************')
    while balance > 0:
        print(f'Your balance is:  ${balance}')
        bet = input('Enter your bet: ')
        if not bet.isdigit():
            print('Please enter a valid number.')
            continue
        bet = int(bet)
        if bet > balance:
            print('Insufficient balance.')
            continue
        balance -= bet
        row = spin_row()
        print('Spinning...\n')
        print_row(row)
        payout = get_payout(row, bet)

        if payout > 0:
            print(f'You win! \n Your payout is:  ${payout}')
        else:
            print(f'You lose!')
        balance += payout

        play_again = input('Do you want to play again? (y/n): ').lower()
        if play_again == 'n':
            print('Thank you for playing.')
            break


if __name__ == '__main__':
    main()