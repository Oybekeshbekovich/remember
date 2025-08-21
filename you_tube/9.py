#Menu tanlash va umumiy hisobni beradi
menu = {
    'osh': 12.00,
    'manti': 15.60,
    'jiz': 20.10,
    'somsa': 14.50
}
cart = []
total = 0
print('-------MENU-------')
for keys, value in menu.items():
    print(f'{keys:10}: {value:.2f}')
print('------------------')
while True:
    food = input("Select food (q to quit): ").lower()
    if food == 'q':
        break
    elif menu.get(food) is not None:
        cart.append(food)
print()
for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print()
print(f"Total cart: ${total:.2f}")