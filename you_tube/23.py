#Shfirlash
import random
import string

chars = string.ascii_letters + string.digits + string.punctuation
chars=list(chars)
key=chars.copy()
random.shuffle(key)

print(f'cahrs: {chars}')
print(f'key: {key}')
# #ENCRYPT
a_text =input('enter text:')
b_text =""
for char in a_text:
    index = key.index(char)
    b_text += chars[index]
print(a_text)
print(b_text)

import random
import string

a=string.digits+string.ascii_letters
a=list(a)
b=a.copy()
random.shuffle(b)
# print(b)
# print(a)
text=input("enter text:")
sd=""

for i in text:
    index=b.index(i)
    sd+=a[index]
print(sd)