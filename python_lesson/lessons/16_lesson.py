# Class OOP

# class User:
#     type = 'human'  # umumiy attribut berish
#
#     # Konstruktor->berilgan argument bo'yicha initializaciya qilish funksiyasi
#     def __init__(self, name, lastname, age, work='IT', salary=100):
#         self.name = name  # mening name maydonimda name argumentini qabul qilaman
#         self.lastname = lastname
#         self.age = age
#         self.work = work
#         self.salary = salary
#
#     def tanishtir(self):
#         return f"My name is {self.name} {self.lastname}, {self.age} years old"
#
#     def tanishtir_print(self):
#         print(f"My name is {self.name} {self.lastname}, {self.age} years old")
#
#     def __str__(self):
#         return f"{self.__class__.__name__} ga tegishli obektman, {self.__dir__()} attribut va standart metodlarim bor!"
#
#     def day_salary(self):
#         return round(self.salary / 25)
#     #==
#     def __eq__(self, other):
#         return self.age==other.age
#     #!=
#     def __ne__(self, other):
#         return self.age!=other.age
#     #>
#     def __gt__(self, other):
#         return self.age>other.age
#     #<
#     def __lt__(self, other):
#         return self.age<other.age
#     #>=
#     def __ge__(self, other):
#         return self.age>=other.age
#     #<=
#     def __le__(self, other):
#         return self.age<=other.age
# user1 = User('Oybek', 'Rahmonberdiyev', 18,'Prep',100 )
# user2 = User(name='Jamshid', lastname='Mavlonov', age=19,work='Krouxfoffise',salary=100)


# print(user1)
# print(user2)

# print(user1.type)
# print(user2.type)

# print(user1.name)
# print(user2.name)

# print(user1.tanishtir())
# print(user2.tanishtir())

# user1.tanishtir_print()
# user2.tanishtir_print()

# print(user1)
#
# print(user1.day_salary())
# print(user2.day_salary())

# getattr
# setattr
# delattr
# hasattr

# print(getattr(user1,'name'))
# print(getattr(user2,'friends','Bunday attribut mavjud emas!'))

# print(user1==user2)
# print(user1!=user2)
# print(user1<user2)
# print(user1>user2)
# print(user1>=user2)
# print(user1<=user2)

#Vorislik qilish
#Meros olish

# class Student(User):
#     def __init__(self, name, lastname, age, work, salary,unversitet):
#         super().__init__(name, lastname, age, work, salary)
#         self.unversitet = unversitet
#
#     def __str__(self):
#         return f'{self.unversitet} talabasi!!!'
#
# newstudent=Student('Oybek', 'Rahmonberdiyev', 18,'Prep',100,'TATU')
# print(newstudent)
# print(user1)

# class Ikki_Shahar_Orasidagi_Masofa:
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#     def destanse(self,other):
#         return ((self.x-other.x)**2 + (self.y-other.y)**2)**0.5
#
# moscow=Ikki_Shahar_Orasidagi_Masofa(350,500)
# london=Ikki_Shahar_Orasidagi_Masofa(426,471)
# paris=Ikki_Shahar_Orasidagi_Masofa(343,362)
# print(f'Mascow to London {moscow.destanse(london)}')
# print(f'Mascow to Paris {moscow.destanse(paris)}')
# print(f'Paris to London {paris.destanse(london)}')

# class Salomlashish:
#     def __init__(self,name):
#         self.name = name
#     def salomlashish(self):
#         return f'Salom {self.name}!'
#
# name=input('Ismingizni kiriting: ')
# p1=Salomlashish(name)
# print(p1.salomlashish())


