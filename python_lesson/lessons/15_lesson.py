from pprint import pprint


# object->grid==fly
# object->gepard==run
# isinstanse()->ekzemplarni class tegishligiga tekshiruv amalga oshiradi

# print(isinstance(4,int))
# print(isinstance("a",str))

# class Car:
#     model = "BMW"
#     engine = 3.5
#
# c=Car()
# pprint(Car.__dict__)
# print(type(c))

# class Person:
#     name="Oybek"
#     age=18
#
# #getattr()->artibut qiymatini olish
# # print(getattr(Person, "name"))
# # print(getattr(Person, "age"))
#
# #setattr()->class ichidagi atribut qiymatini o'zgartiradi
# setattr(Person, "name", "Jamshid")
# setattr(Person, "age", 17)
# pprint(Person.__dict__)

# class Car:
#     model = "BMW"
#     engine =3.5
# a1=Car()
# b1=Car()
# a1.model = "Lada"
# b1.size = 80
#
# print(a1.__dict__)
# print(a1.model)
# print(b1.__dict__)
# print(b1.model)

# class Cat:
#     breed = 'pers'
#     def __init__(self, name,breed, age,color):
#             print("Hello",name,"!",breed,age,color)
#             self.name = name
#             self.breed = breed
#             self.age = age
#             self.color = color
# tom=Cat('Tom','Brian','19',"red")


# class Person:
#     def can_walk(self):
#         print("You can walk")
#     def can_breathe(self):
#         print("You can breathe")
# class Doctor(Person):
#     def can_cure(self):
#         print("I can cure")
# class Architecture(Person):
#     def can_build(self):
#         print("I can build")

# d=Doctor()
# d.can_cure()
# d.can_walk()
# d.can_breathe()
#
# a=Architecture()
# a.can_build()
# a.can_walk()
# a.can_breathe()

#print(issubclass(Doctor, Person))

class Person:
    def __init__(self, name='human'):
        self.name = name
    def can_walk(self):
        print('can walk')
    def can_breath(self):
        print('can breath')
class Oybek(Person):
    def can_code(self):
        print('I can code')
    def combine(self):
        self.can_breath()
        self.can_walk()
        self.can_code()
class Jamshid(Person):
    def can_code(self):
        print('You can code')
    def combine(self):
        self.can_breath()
        self.can_walk()
        self.can_code()
p1=Oybek()
p2=Jamshid()

p1.combine()
p2.combine()
