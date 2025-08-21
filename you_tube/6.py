#Listning ichiga yana list solib undagi elementni tanlash
#1-
meal=["osh","manti","jiz"]
fruit=["apple","banana","orange"]
vegetable=["cator","pottato","tomato"]

all_list=[meal,fruit,vegetable]
print(all_list[0][0])

#2-
all_list = [["osh", "manti", "jiz"], ["apple", "banana", "orange"]
    , ["cator", "pottato", "tomato"]]
print(all_list[0][0])

all_list = [["osh", "manti", "jiz"], ["apple", "banana", "orange"]
    , ["cator", "pottato", "tomato"]]
for items in all_list:
    for item in items:
        print(item,end=" ")
    print()
