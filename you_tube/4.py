prinspal = 0
rate = 0
time = 0
while True:
    prinspal = float(input("Enter the price of your ticket: "))
    if prinspal <= 0:
        print("Prinspal can't be less than or equal to zero")
    else:
        break
while True:
    rate = int(input("Enter the rate of your ticket: "))
    if rate <= 0:
        print("Interest can't be less than or equal to zero")
    else:
        break
while True:
    time = int(input("Enter the time of your ticket: "))
    if time <= 0:
        print("Time can't be less than or equal to zero")
    else:
        break
total = prinspal * pow((1 + rate / 100), time)
print(f'{total:.2f}')