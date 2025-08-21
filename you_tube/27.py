#Inheritance->meros ota-onadan meros
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} is sleeping')

class Dog(Animal):
    def speak(self):
        print(f'WOOF!')
class Cat(Animal):
    def speak(self):
        print(f'MEOW!')
dog = Dog('Olabayr')
cat = Cat('Tom')

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()
dog.speak()
