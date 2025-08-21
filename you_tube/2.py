from random import random
import random
#Outer loop and inner loop:->bo'yiga va eniga kiritilgan narsalar
rows=int(input("Enter the number of rows: "))
columns=int(input("Enter the number of columns: "))
symbol=input("Enter the symbol: ")
for i in range(rows):
    for j in range(columns):
        print(symbol,end=" ")
    print()