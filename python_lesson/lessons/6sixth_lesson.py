# Funksiyalar

# def <Funksiya nomi>():
# Logika

# def say_hello():
#     print('salomcha')
#
# def exit():
#     pass

# from funksiya import say_hello,exit
#
# say_hello()

#Ism kiritsa Salom beradigan funksiya
# def say_hello2(name=None):
#     print(f'Salom,{name}!')
# a=input('Enter your name: ')
# say_hello2(a)

#Ism,yosh va ishni so'raydigan funksiya
# def request_data(name, age, work='bekorchimisizi?'):
#     print(f'Sizminigiz: {name}, Sizni yoshinigiz: {age}. Siz {work}siz')
#
#
# name = input('Enter your name: ')
# age = input('Enter your age: ')
# work = input('Enter your work: ')
# request_data(name, age, work)
# request_data(name, age)

#Calculator
# def calculator(operator=None,a=None,b=None):
#     if operator == '+':
#         return a + b
#     elif operator == '-':
#         return a - b
#     elif operator == '*':
#         return a * b
#     elif operator == '/':
#         return a / b
#     elif operator == '//':
#         return a // b
#     elif operator == '**':
#         return a ** b
#     else:
#         return ValueError("ERROR")
#
# operator,a,b=int(input("enter first number: "))
# print(calculator(operator,a,b))
# #pozitsion argumnet
#
# #nomlangan argument
# print(calculator(a=1,b=2,operator='-'))

#funksiya orqali agar ro'yxatda son son qatnashgan bo'lsa kvadratga oshiradi, satr bo'ladigan bo'lsa unda "salom" so'zini qo'shib beradi
# def requst_list(list1):
#     list2 = []
#     for i in list1:
#         if type(i) is int:
#             list2.append(i**2)
#         elif type(i) is str:
#             list2.append(i+' salom')
#     return list2
# print(requst_list([1,2,3,'Jamshid','Oybek',7,8,'Sardor']))

# s = "I love programming"
# def reverse_words(s):
#     return ' '.join(reversed(s.split()))
# print(reverse_words(s))