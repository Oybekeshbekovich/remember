#Random
import random

#Random bitta raqam tanlash
low=1
high=10
number=random.randint(low,high)
print(number)

#Sintaksis ro'yxatni randomi
options=('jazz','rock','pop')
option=random.choice(options)
print(option)

#Listdagilarni randomi
cards=['1','2','3','4','5','6','7','osh','jiz','A']
random.shuffle(cards)
print(cards)