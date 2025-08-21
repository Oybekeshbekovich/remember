#Object and class->haqida
from car import Car

car1=Car('BMW',2022,'black',True)
car2=Car('Audi',2022,'blue',True)
car1=Car('BMW',2022,'black',True)
car2=Car('Audi',2022,'black',True)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car2.stop()