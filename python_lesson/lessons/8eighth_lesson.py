import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#matplotlib kutubxonasidagi qaysi backend dan foydalanishni ko'rsatadi
# matplotlib.use('TkAgg')
# plt.show()

#get_backend()-matplotlib kutubxonasini qaysi backend dan foydalanayotganini taqdim qiladi
# print(matplotlib.get_backend())

#grid->"setka" hosil qiladi
# plt.grid(True)
# show()->bu metod hosil bo'lgan massivni ko'rsatib beradi
# plt.show()

#Kvadrat hosil bo'ladi
# x=np.array([1,1,5,5,1])
# y=np.array([1,5,5,1,1])
#
#Chiziqlar
# y=np.arange(0,5,1)
# x=np.array([a*a for a in y])
#
# y2=[0,1,2,3,4]
# x2=[i+1 for i in y2]
# plt.plot(x, y,y2,x2)
#
# line=plt.plot(x,y,'g-o',y2,x2,'r-H',markerfacecolor='g',markersize=12)
# print(line)
# plt.grid()
# plt.show()

#plot metodi bizga 2D grafik chizib beradi
#Chiziqqa rang berish turlari
#1.RGB=(0,0,0),4-argument->ko'rinish darajasi
#2.#000CC ikkilik sanoq sistemasi
#3.color=''-> bu faqat hammasini bo'yaydi


#cos(x) oraliqni np kutubxonasi orqali 2D ko'rinishini yasash va bo'yash
# x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
# y = np.cos(x)
# plt.plot(x, y)
# plt.grid()
# plt.show()
#
# # fill_between()->metodi oraliqni bo'yaydi.
# plt.fill_between(x, y,where=(y<0), facecolor='blue', alpha=0.5)
# plt.fill_between(x, y,where=(y>0), facecolor='red', alpha=0.5)
#
# plt.rcParams['font.size'] = 1