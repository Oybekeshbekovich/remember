# Kodirovka
# ACSII
#from importlib.resources import contents
#faylni o'qish
# file=open("the_layers.txt")
# content=file.read()
# print(content)
# file.close()
from os import write

# ==================================================
#Ba'zi bir elementlar va yozish yoki o'qish mumkin yoki mumkinmaslikni aniqlaydi
# UTF-8
# 'r'->o'qish
# 'w'->yozadi,agar file mavjud bo'lmasa yangi fayl ochib yozib ketadi,fayl ichidagi hamma narsani o'chirib tashlab boshidan yozadi.
# 'a'->yozadi,agar file mavjud bo'lmasa OSHIBKA qaytaradi,file ichidagi narsalarni saqlab filega kiritalayotgan malumottni yozib ketadi
# 'rb'-> bayt bo'yicha

# file=open("pushkin.txt",mode="r",encoding="utf-8")
# content1 = file.read()
# print(content1)
# print(file.encoding) #kodirovka
# print(file.writable()) #yozish mumkin mumkinmasligini tekshiradi
# print(file.readable()) #o'qish mumkin mumkinmasligini tekshiradi
# file.close()

# ================================================
#faylni ichidagini chaqlab qolib yangi qatordan yangi so'z qo'shadi
# file = open('text', mode='a', encoding='utf-8')
# content = 'Salomcha\n'
# file.write(content)
# file.close()

# ================================================
#txtning ichiga so'z qo'shish uchun!
# while True:
#     file=open('text',mode='a',encoding='utf-8')
#     user_text = input('Enter your message : ')
#     if user_text == 'stop':
#         break
#     file.write(user_text+'\n')
#     file.close()

# ================================================
#1-fayldagi narsani ochib o'qiydi va 2-faylga yozib chiqaradi
# file=open('pushkin.txt',mode='r',encoding='utf-8')
# file1=open('new_txt.txt',mode='w',encoding='utf-8')
#
# content=file.read()
# file1.write(content)
# file.close()
# file1.close()

# ================================================
#bitta ochib yopish with bilan
# with open('pushkin.txt', mode='r', encoding='utf-8') as file:
#     new_file2 =open('new_file2.txt', mode='w', encoding='utf-8')
#     content = file.read()
#     new_file2.write(content)
#     new_file2.close()
#     print("Fayl yopildimi? ",file.closed)
# print("Fayl yopildimi? ",file.closed)

# ================================================
# #rasmni ochish va uni ko'paytirish
# file = open('nature.jpg',mode='rb')
# picture = file.read()
# for i in range(1,11):
#     new_picture = open(f'picture/copy_images{i}.jpg',mode='wb')
#     new_picture.write(picture)
#     file.close()
# file.close()
#

# ================================================
#pythonni o'zida fillarni ustida ammalr bajaradi(fayllarni o'chirish,ko'paytirish)
#import os
# for i in range(1,11):
#     os.remove('reader_lesson'+str(i)+'.py')

# print(os.listdir())
# if 'picture' not in os.listdir():
#     os.mkdir('picture')
#
# os.rmdir('picture')

# ================================================
#kodivorka
# str='Hello'
# str_8=str.encode('utf-8')
# str_16=str.encode('utf-16')
# str_32=str.encode('utf-32')
# str_cp866=str.encode('cp866')
# str_cp1251=str.encode('cp1251')
# print(str_8.__sizeof__())
# print(str_16.__sizeof__())
# print(str_32.__sizeof__())
# print(str_cp866.__sizeof__())
# print(str_cp1251.__sizeof__())

# ================================================
#faylni o'qib, fayldagi har bir qatordan aynan biron narsani elementni tartiblab, nechi marotaba ishlatilganini aniqlaydi
# file = open('mbox-short.txt', mode='r',encoding='utf-8')
#
# count={}
# for line in file:
#     if line.startswith('From '):
#         data=line.split(" ")
#         time=data[6].split(":")
#         hours=time[0]
#         count[hours]=count.get(hours,0)+1
# file.close()
# for key,value in sorted(count.items()):
#     print(f'{key} da, {value} ta xabar kelgan!')

# ================================================
#ishlashga qancha vaqt ketgani aniqlaydi
import time
# son=int(input('Enter the son number: '))
# start=time.time()
# list1=[i for i in range(son)]
# end=time.time()
# print(end-start)

#=====================================================
#file ichidagi emaillarni topib ro'yxatini tuzib beradi
#1-exec
# emails = []
#
# with open('mbox_short', mode='r') as file:
#     for line in file:
#         line = line.strip()
#         if line.startswith('From '):
#             parts = line.split()
#             if len(parts) > 2:
#                 emails.append(parts[2])
#             str_emails='\n'.join(emails)
# print(str_emails)

#==================================================
#faylni ichidagi yozilgan bir qator so'zlarni yangi listga tartiblab yozib beradi
#2-exec
# new_list=[]
#
# with open('romeo',mode='r',encoding='utf-8')as file:
#     for line in file:
#         line1 = line.strip()
#         new_list.append(line1)
#
# print(sorted(new_list))