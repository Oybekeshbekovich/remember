# Kortejlar - statik ro'yxatlar

# a=(55,43,22.33,'c') #statik -ro'yxat
# b=[55,43,22.33,'c'] #dinamik -ro'yxat

# print(a.__sizeof__())#byte
# print(b.__sizeof__())#byte
#
# # a[0]=34
# # b[0]=34
#

# a=tuple('salomcha')
# print(a)

# c=('salomcha')
# d=('salomcha','sdf',456)
#
# print(d.count(456))

# nums=[1,2,3,4,5]
# for num in nums:
#     print('salom',num)

#range - (start=0,end,step=1)

# for i in range(10+1):
#     print(i)

# for i in range(1,10+1):# start va end argumenti
#     print(i)

# for i in range(1,10+1,3):# start,end va step argumenti
#     print(i)

# for i in range(20,5,-1):
#     print(i)

# nums=[]
# for i in range(1,int(input('Enter number: '))+1):
#     nums.append(i)
# print(nums)
# print(sum(nums))

# square=[]
# for i in range(1,10):
#     square.append(i**2)
# print(square)

#Ro'yxatlar generatsiyasi

# [amal for o'zgaruvchi in 'interatsiyaga bo'ysunuvchi obyekt']
# a=[i**2 for i in range(1,10+1)]
# print(a)
#
#import random
# a=[random.randint(-10,10) for i in range(5)]
# print(a)
#
# import random
# b=[random.randint(1,10) for i in 'salomcha']
# print(b)

# a=[i for i in range(1,10)if i%2==0]
# print(a)

# nums=[1,21,13,4,55,89,3,9]
# nums_gt=[i for i in nums if i >= 5]
# nums_lt=[i for i in nums if i < 5]
# print(nums)
# print(nums_gt)
# print(nums_lt)

# nums=[1,2,3,4,5,6,7,8,9]
# print(sum(nums))
# print(max(nums))
# print(min(nums))

#Start,end,step->metodi
#print(list1[default_start=0:default_end=len(list1):default_step=1])
#
# list1=[1,2,3,'hello',4,5,'time',8,9,'ball',14,13,'smalle']

#Startdan index nechigachadir
# print(list1[0:3])
# print(list1[:3])

#Start nechidandir index nechidirgacha
# print(list1[3:len(list1)])
# print(list1[3:12+1])
# print(list1[3:])

# print(list1)
# print(list1[2:10:2])

#Turini ajratish ya'ni str va int tiplariga ajratish
# list1=[1,2,3,'hello',4,5,'time',8,9,'ball',14,13,'smalle','title']
# list1_of_strings=[i for i in list1 if type(i) is str]
# list1_of_integers=[i for i in list1 if type(i) is int]
# print(list1_of_integers)
# print(list1_of_strings)

#Nusxalash
# list1=[1,2,3,'hello',4,5,'time',8,9,'ball',14,13,'smalle']
# list2=list1.copy()
# print(list1)
# print(list2)

#Break va continue->metodi
# list1=[1,2,3,'hello',4,5,'time',8,9,'ball',14,13,'smalle','title']
#
# for i in list1:
#     if i == 'title':
#         print('Break!')
#         break
#     elif type(i) == int:
#         print('No')
#         continue

# iterator=0
#
# while iterator<10:
#     print('Yes', iterator)
#     iterator +=1


#add,delete,search,stop,clear,view->metodlari

# fruits = ['banana', 'orange', 'strawberry']
#
# while True:
#     user_text = input('<UNK>')
#     if user_text == 'stop':
#         print('Goodbye')
#         break
#
#     command,product_name= user_text.split(' ')# add apple['add','apple']
#     if command =='add':
#         fruits.append(product_name)
#         print(f"Added {product_name} to the list",fruits)
#     elif command =='delete':
#         fruits.remove(product_name)
#         print(f"Removed {product_name}",fruits)