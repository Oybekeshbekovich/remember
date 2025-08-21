# Mantiqiy amallar "Taqqoslash operatorlari"
#False yoki True qaytaradigan misollar
# print(3<1)
# print(3<=2)
# print(3<4)
# print(2==2)
# print(2!=2)

# print('a'>'b')
# print('c'>'C')
# print("a" == "a")

#Bu metod harflarni asci ajdvaldagi qiymatini chiqarib beradi.

# print(ord("B"))
# print(ord("a"))

#ikkilik sanoq sistemasidagi qiymatini chiqatib beradi
# a=bin(5)
# b=bin(10)
# print(a,b)

# hex->16
# oct->8
# bin->2
# ord->asci

#16 lik sanoq sistemasi
#print(hex(16))
#8 lik sanoq sistemasi
#print(oct(8))
#sonning darajasiga oshiradi
# print(pow(3,5))
#Round metodi sonni yaxlitlab beradi
# print(round(3.65))

# a= reversed("Oybek")
# print(a)

# Shart operatorlari

# username ="oybek"
# password = "Oybek_07"
# a=input("User name kiriting: ")
# if a==username:
#    print("Welcome " + username + "!")
# b=input("Password kiriting: ")
# if b==password:
#    print("It is true")
# print("Siz saytga muafaqqiyatli kirdingiz!!!")

#x=int(input("<UNK>"))
#y=int(input("<UNK>"))
#if x==y:
 #   print("True")
#else:
 #   print("False")

# a=int(input("Yoshingizni kiriting: "))
# if a <= 18:
#    print("o'quvchi")
# elif a<=25:
#   print("talaba")
# else:
#   print("ishchi")


#Mantiqiy operatorlar
# or - yoki
# and- va
# not- yo'q, bo'lmasa


# a=int(input("Yoshingizni kiriting: "))
# if a > 0 and a<=18:
#    print("o'quvchi")
# elif 18<a<=25:
#   print("talaba")
# else:
#   print("ishchi")


# user_name =input('<UNK>')
# password = input('<<PASSWORD>>')

#foynadalnuvchlar
# user_name -"oybek" ;password - 123456
# user_name-"ixtiyor";password - 757575

#adimnstratorlar
# user_name -"abbos" ;password - qwerty
# user_name-"asil";password - zxcvbn

# if (user_name == 'oybek' and password == "123456") or (user_name == 'ixtiyor' and password == "757575"):
#     print('Xush kelibsiz', user_name+"!")
# elif(user_name == 'abbos' and password == "qwerty") or (user_name == 'asil' and password == "zxcvbn"):
#     print('Welcome', user_name+"!")
# else:
#     print('Error')

# a=input("<UNK>")
# b=input("Surename: ")
# if (a.lower() == "oybek" or a.lower() == "jamshid") and b.lower() == "rakhmonberdiyev":
#     print("Welcome!")


# a=input("Name: ")
# if a:
#     print(f"Hello {a} ")
# else:
#     print(f"It is not your name!  {a}")