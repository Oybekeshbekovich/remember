#Banking programm

def show_balance(balance):
    print(f'Your balance is ${balance:.2f}')


def deposit():
    print('------------------------------')
    amount = float(input('Enter amount to deposit: '))
    if amount < 0:
        print('----------------------------------')
        print('You cannot deposit negative amount')
        return 0
    else:
        print('----------------------------------')
        return amount


def withdraw(balance):
    print('--------------------------------')
    amount = float(input('Enter amount to withdraw: $'))
    if amount > balance:
        print('-----------------------------------')
        print('You cannot withdraw positive amount')
        return 0
    elif amount < 0:
        print('-----------------------------')
        print('You cannot withdraw negative amount')
        return 0
    else:
        print('-----------------------------')
        return amount


def main():
    balance = 0
    is_running = True
    while is_running:
        print('-------------------')
        print('   BANK PROGRAMM   ')
        print('-------------------')
        print('1.Your balance')
        print('2.Deposit')
        print('3.Withdraw')
        print('4.Exit')
        choice = input('Enter your choice: ')
        if choice == "1":
            print('---------------------')
            show_balance(balance)
            print()
        elif choice == "2":
            balance += deposit()
            print()
        elif choice == "3":
            balance -= withdraw(balance)
            print()
        elif choice == "4":
            is_running = False
            print()
        else:
            print('Invalid choice')
    print('---------------------------')
    print('Thank you! Have a nice day!')
    print('---------------------------')


if __name__ == '__main__':
    main()