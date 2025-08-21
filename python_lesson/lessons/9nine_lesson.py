# Funksiyalash dasturi

# nums=[1,2,3,4,5,6,7,8,9]
# # print(nums)
# nums1=[]
# for i in nums:
#     nums1.append(i)
# print(nums1)

#===================================================================
# map-> map(nima qilish kerakligi,nima bilan ishlash?(Ro'yxat))->map obyekt

# nums2=map(int,nums)
# print(nums2)

# print('list', nums1,nums1.__sizeof__())
# print('map', list(nums2),nums2.__sizeof__())

# def num1(number):
#     return number*2
# list1=[i for i in range(1,11)]
# list2=list(map(num1,list1))
#
# # print(list1)
# # print(list2)
#
#
# def add_hello(elem):
#     return str(elem)+ ' salomcha'
#
# list3=list(map(add_hello,list1))
# # print(list3)

# =============================================================

# Listdagi str va int larni ajratish va qo'shimcha qo'shish
# a=[1,2,3,'salom','world',7,9,15,'time','teach']
#
# def sorted_a(elem):
#     if type(elem) is int:
#         return elem + 10
#     elif type(elem) is str:
#         return elem + " python"
# list4=list(map(sorted_a,a))
# print(list4)

# ============================================
# filter
# list1=[1,2,3,4,5]
# def even(number):
#     return number % 2 == 0
#
# list5=list(filter(even,list1))
# print(list5)

# ==========================================
# a=[1,2,3,'salom','world',7,9,15,'time','teach']
# def getStr(element):
#     return type(element) is str
# def getNum(element):
#     return type(element) is int
#
# list6=list(filter(getStr,a))
# list7=list(filter(getNum,a))
# print(list6)
# print(list7)

# ===================================
# lambda funksiyalari - 1qatorli

# Lambada <object>:<Nima qilish kerakligi?>
#
# nums=['1','2','3','4','5','6','7','8','9']
# list8=list(map(lambda element:int(element),nums))
# print(list8)

# a = [1, 2, 3, 'salom', 'world', 7, 9, 15, 'time', 'teach']
# list9 = list(map(lambda element: str(element) + " salom",a))
# # print(list9)
#
# list10 = [i for i in range(10)]
# list11 = [i for i in range(25,35)]
#
# print(f"{list10}\n{list11}")
#
# list12=list(map(lambda x,y:x+y,list10,list11))
# print(f"{list12}")


