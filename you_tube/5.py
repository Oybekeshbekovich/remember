# Shopping cart program
foods = []
prices = []
total = 0
while True:
    food = input("Enter food name or (q to quit): ")
    if food.lower() == "q" or food.lower == "quit":
        break
    else:
        price = float(input(f"Enter price of food {food}:$"))
        foods.append(food)
        prices.append(price)
print('---------------------------------')
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
print()
print(f"Total: {total}")
