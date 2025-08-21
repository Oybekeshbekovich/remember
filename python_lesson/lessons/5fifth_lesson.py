# a=[1]
# b=[]
# for i in range(1,10+1):
#     if i%2==0:
#         a.append(i)
#     else:
#         b.append(i)
# print(f'{sum(a)}')
# print(f'{sum(b)}')

# Lug'atlar

# dict1 = {}
# dict2=dict()
# print(dict1)
# print(dict2)

# friends={
#     '12345':'MMM',
#     '14785':'NNNN',
#     '12369':'pppp'
# }
# print(friends,type(friends))
# print(friends)

#Kalit metodlari
# #Kalit orqali qiymat topish
# print(friends['12345'])
#
# #Kalit orqali o'zgartirish
# friends['12369']='Okkf'
# print(friends['12369'])


# #Kalit orqali o'chirish (del metodi)
# del friends["12369"]
# print(friends)


##Kalit qo'shish
# data ={}
# data['1234578']='Oybek'
# print(data)


## Kalit olish
# for friend in friends:
#     print(friend)

#Lug'atlardagi qiymatlarni olish metodlar
# #items-metodi
# for number,name in friends.items():
#     print(number,name)
#
# #key()-metodi
# for number in friends.keys():
#     print(number)
#
# #values()-metodi
# for name in friends.values():
#     print(name)

# friends = {
#     '12345': 'MMM',
#     '14785': 'NNNN',
#     '12369': 'pppp'
# }
# friends2 = {}
# print(friends2)
# for number, name in friends.items():
#     friends2[name] = number
# print(friends2)
# print(friends)

# Nushalash metodi
# friends3=friends2.copy()
# print(friends)
# print(friends2)
# print(friends3)

# #Tozalash metodi
# friends3.clear()
# print(friends)
# print(friends2)
# print(friends3)

#Userlar bilan ish
# user1 = {
#     'id': 1,
#     'name': 'Oybek',
#     'lastname': 'Rakhmonberdiyev'
# }
# user2 = {
#     'id': 2,
#     'name': 'Jamshid',
#     'lastname': 'Mavlonov'
# }
# user3 = {
#     'id': 3,
#     'name': 'Aziz',
#     'lastname': 'Axmedov'
# }
# users = [user1, user2, user3]
# for user in users:
#     # print(user)
#     print(f"Foydalanuvchi ismi: {user['name']} \nFoydalanuvchi familyasi: {user["lastname"]}")

#Lug'atlar ustida ishlar bo'yicha namuna
# user = [
#     {
#         'id': 1,
#         'name': 'Oybek',
#         'lastname': 'Rakhmonberdiyev',
#         'interests': ['coding', 'playing', 'writing'],
#         ('adress', 'bank_info'): {
#             'adress': 'Jizzax',
#             'bank_info': 'MK'
#         }
#     },
#     {
#         'id': 2,
#         'name': 'Jamshid',
#         'lastname': 'Mavlonov',
#         'interests': ['listening', 'writing', 'watching'],
#         ('adress', 'bank_info'): {
#             'adress': 'Baxmal',
#             'bank_info': 'Aloqa'
#         }
#     },
#     {
#         'id': 3,
#         'name': 'Aziz',
#         'lastname': 'Axmedov',
#         'interests': ['gaming', 'reading', 'writing'],
#         ('adress', 'bank_info'): {
#             'adress': 'Jizzax',
#             'bank_info': 'Hamkor'
#         }
#     }
#
# ]
# marks = {
#     1: {
#         'python': 3,
#         'c++': 2
#     },
#     2: {
#         'python': 2,
#         'c++': 2
#     },
#     3: {
#         'python': 3,
#         'c++': 3
#     }
# }
#Lug'atning qiymatlarini chiqarish
# for user in user:
#     for key, value in user.items():
#         print(key, value)
#         if type(value) is list:
#             print(f'--- {key}')
#             for item in value:
#                 print(f'--{item}')
#         elif type(value) is dict:
#             print(f'--- {key}')
#             for k, v in value.items():
#                  print(f'-{k}:{v}')
#         elif type(value) is int:
#             print(key,value)
#             for course,mark in marks[value].items():
#                 print(f'---{course}:{mark}')
#         else:
#             print(key,value)
#     print('---------------------------')

#2-namuna
# user = [
#     {
#         'id': 1,
#         'name': 'Oybek',
#         'lastname': 'Rakhmonberdiyev',
#         'interests': ['coding', 'playing', 'writing'],
#         ('adress', 'bank_info'): {
#             'adress': 'Jizzax',
#             'bank_info': 'MK'
#         }
#     }
# ]
#
# print(user[0]['interests'])
# print(user[0]['interests'][0])
#
# for key in user[0].keys():
#     print(key)
# for value in user[0].values():
#     print(value)
# for key,value in user[0].items():
#     print(key,value)