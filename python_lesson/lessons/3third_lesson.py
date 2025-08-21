#List- ro'yxatlar

# myList = [1,2,3,"oybek",[7,8,9,"Abbos"]]
#
# print(myList)
# print(len(myList))
# print(myList[0])
# print(myList[1])
# print(myList[2])
# print(myList[3])
# print(myList[4])
# print(myList[5])
# print(myList[6])- out of range

# print(myList.index(3))
#
# fruits = ["apple", "banana", "cherry",'melon','watermelon']

#metod append-> ro'yxatga qo'shish

# fruits.append("pear")
# fruits.append("cherry")
#
# print(fruits)

#metod insert->ro'yxatning istalgan joyiga qo'sha oladi indexga qarab

# fruits.insert(0,"pizza")
# print(fruits)

#del metodi->index ga qarab o'chiradi
#del fruits[3]- o'chiradi
#print(fruits)

#metod remove->belgilangan elementni o'chiradi
# print(fruits)
# fruits.remove("apple")
#
# print(fruits)

#pop metod->tanlangan elementni o'chiradi
# item_index=fruits.index('banana')
# deleted_fruit = fruits.pop(item_index)
# print(f"Your deleted fruit is: {deleted_fruit}")
# print(fruits)

#sort- tartiblash metodi
# nums = [7,8,2,3,4,6,8]
# print(nums)
#
# nums.sort()
# print(nums)
# nums.sort(reverse=True)
# print(nums)

# list1=['Ab','ab','bc','Bc','zd','Ye']
# print(sorted(list1))
#
#
# list1=['Ab','ab','bc','Bc','zd','Ye']
# print(list1)
# list1.sort()
# print(list1)

# nums=[4,6,7,3,5,8]
# nums_sorted=sorted(nums)
# nums_sorted.append("AAA")
# print(nums_sorted)

#Foydalanuvchi element kiritadi va u ro'yxat oxiriga qo'shiladi
# fruits = ["apple", "banana", "cherry", 'melon', 'watermelon']
# user_element=input("<UNK>")
# fruits.append(user_element)
# print(fruits)
#Foydalanuvchi kiritgan element ro'yxatning ichida bo'lsa "YES" qaytaradi aks holda "NO"
# fruits = ["apple", "banana", "cherry", 'melon', 'watermelon']
# user_element=input("<UNK>")
# if user_element in fruits:
#     print("Yes")
# else:
#     print("No")

#Foydalanuvchi kiritgan element ro'yxatning ichida bo'lmasa "YES" qaytaradi aks holda "NO"
# fruits = ["apple", "banana", "cherry", 'melon', 'watermelon']
# user_element=input("<UNK>")
# if user_element not in fruits:
#     print("Yes")
# else:
#     print("No")

#Foydalanuvchi kiritgan element ro'yxatning ichida bo'lsa uni o'chiradi aks holda ro'yxat oxiriga qo'shib qo'yadi
# fruits = ["apple", "banana", "cherry", 'melon', 'watermelon']
# user_element=input("<UNK>")
# if user_element in fruits:
#     fruits.remove(user_element)
#     print(f'fruits removed: {fruits}')
#     print(fruits)
# else:
#     fruits.append(user_element)
#     print(f'fruits added: {fruits}')
#     print(fruits)

#sikl-for->ro'yxatning ichidagi int va strlarni ajratib beradi
# list1=[1,2,'time',5,6,'hello',8,9,'done',6]
# list_of_integers=[]
# list_of_strings=[]
#
# for element in list1:
#     if type(element) is int: #elementning tipini aniqlaydi
#         list_of_integers.append(element)
#     else:
#         list_of_strings.append(element)
# print(list1)
# print(list_of_integers)
# print(list_of_strings)

# str1='hello world'
# for character in str1:
#     print(character) #Har bitta harfni tagma-tag yozib beradi
# new_list=str1.split(' ') # SPLIT - satrdan ro'yxat hosil qilish
# print(new_list)

# str1='hello world'
#
# new_list=str1.split(' ')
# print(new_list)

# new_list2=['hello', 'world']
# new_str=' '.join(new_list2) # Ro'yxatdan satr hosil qiladi
# print(new_str)

#list - element tipini o'zgartirish
# str1='hello world'
# new_list=['h','e','l','l','o']
# new_list1 = list(str1)
# print(new_list1)
