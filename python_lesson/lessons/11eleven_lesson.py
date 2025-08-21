# Xatolar ustida ishlash
# Kelib chiqishi mumkin bo'lgan xatoni oldini olish
# from tkinter.font import names

# try:
#     print(name)
#     list1 = [0, 1, 2, 3, 4]
#     print(list1[6])
# except Exception as e:
#     e.__str__ = 'Big error!!!'
#     print('Bunday ozgaruvchilar majud emas')
#     print('Bunday ozgaruvchilar majud emas', e)
#     print('Bunday ozgaruvchilar majud emas', e.__class__.__name__)
#     print('Bunday ozgaruvchilar majud emas', e.__str__)

# while True:
#     number = input('Enter a number: ')
#     try:
#         num = int(number)
#         if num == 1:
#             print('Hello')
#             try:
#                 print(nums)
#             except NameError:
#                 print(NameError)
#         elif num == 2:
#             try:
#                 list1 = [0, 1, 2, 3, 4]
#                 print(list1[6])
#             except IndexError:
#                 print(IndexError.__name__)
#         elif num == 3:
#             try:
#                 print(10 / 0)
#             except ZeroDivisionError as e:
#                 e.__str__='nolga bolinmaydi'
#                 print(e.__str__)
#     except Exception as n:
#         print('Son kiritish kerak edi!')
#


# Ummumiy ro'yxatdan o'tganlardan to'rri ro'yxatga o'tgani andenli xatosini adenli qilib beradi
# import string
# def validate_name(name):
#     for letter in name:
#         if letter in string.punctuation or letter in string.octdigits:
#             return False
#     return True
#
#
# def validate_email(email):
#     if '@' in email and '.' in email:
#         return True
#     else:
#         return False
#
#
# def validate_age(age):
#     try:
#         if 20 <= int(age) <= 60:
#             return True
#         else:
#             return False
#     except:
#         return False
#
#
# with open('registration',mode='r' ) as file:
#     good = open('good', mode='w')
#     bad = open('bad', mode='w')
#
#     for line in file:
#         if len(line.split(' ')) != 3:
#             bad.write(line)
#         else:
#             data = line.split(' ')
#             name = validate_name(data[0])
#             email = validate_email(data[1])
#             age = validate_age(data[2])
#             if name and email and age:
#                 good.write(line)
#             else:
#                 bad.write(line)
#
#     good.close()
#     bad.close()


# n=int(input("<UNK>"))
# def raqamlar_sum(n):
#     s = 0
#     while n > 0:
#         s+= n % 10
#         n = n // 10
#     return s
#
#
# def garoyib(n):
#     s = raqamlar_sum(n)
#     if n % (s * s) == 0:
#         return True
#     else:
#         return False
#
#
# def javob(n):
#     r = 0
#     x = 0
#     while n > r:
#         x += 1
#         if garoyib(n):
#             r += 1
#     return x
#
#
# n = int(input('>>>'))
# print(javob(n))

# a=input()
# g=input()
# v=input()
# m="qog'oz"
# n="quduq"
# k="qaychi"
# if ((a.lower()==v.lower()==m) and g.lower()==k) or ((a.lower()==v.lower()==k) and g.lower()==n) or ((a.lower()==v.lower()==n) and g.lower()==m):
#     print("G'ani")
# elif ((a.lower()==g.lower()==n) and v.lower()==m) or ((a.lower()==g.lower()==m) and v.lower()==k) or ((a.lower()==g.lower()==k) and v.lower()==n):
#     print("Vali")
# elif ((v.lower()==g.lower()==n) and a.lower()==m) or ((v.lower()==g.lower()==k) and a.lower()==n) or ((v.lower()==g.lower()==m) and a.lower()==k):
#     print("Ali")
# else:
#     print("?")


# Zon-zonziki o'yini
# ali = input()
# vali = input()
# gani = input()
# def winner(ali, vali, gani):
#     players = {'Ali': ali, 'Vali': vali, 'G\'ani': gani}
#     values = list(players.values())
#     unique = set(values)
#     if len(unique) == 1 or len(unique) == 3:
#         return '?'
#     rules = {
#         'quduq': 'qaychi',
#         'qaychi': 'qog\'oz',
#         'qog\'oz': 'quduq'
#     }
#     for player, sign in players.items():
#         others = [v for k, v in players.items() if k != player]
#         if all(rules[sign] == o for o in others):
#             return player
#     return '?'
# print(winner(ali, vali, gani))


# a,b=list(map(int,input().split()))
# print(f'{a}{b}')

# a=int(input())
# def min_contests(N):
#     min_count = float('inf')
#     found = False
#
#     for x in range(N // 5, -1, -1):
#         remaining = N - (5 * x)
#         if remaining % 3 == 0:
#             y = remaining // 3
#             total = x + y
#             min_count = min(min_count, total)
#             found = True
#             break
#
#     if found:
#         return min_count
#     else:
#         return -1
#
# print(min_contests(a))

#Qavariq ko'pburchakni topish formulasi
# N = int(input())
# for i in range(1,N+1):
#   diagonals = N * (N - 3) // 2
# print(diagonals)

# a=list(map(int,input().split()))
# b=int(input())
# print(b-sum(a))

# a,b=map(int,input().split())
# print(f"{10-a} {10-b}")