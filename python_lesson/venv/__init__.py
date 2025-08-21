import matplotlib
import matplotlib.pyplot as plt
import numpy as np

# matplotlib kutubxonasidagi qaysi backend dan foydalanishni ko'rsatadi
# matplotlib.use('TkAgg')

# get_backend()-matplotlib kutubxonasini qaysi backend dan foydalanayotganini taqdim qiladi
# print(matplotlib.get_backend())

# x=np.array([1,1,5,5,1])
# y=np.array([1,5,5,1,1])

# y = np.arange(0, 5, 1)
# x = np.array([a * a for a in y])
#
# y2 = [0, 1, 2, 3, 4]
# x2 = [i + 1 for i in y2]

# plot metodi 2D grafigini chizib beradi
# plt.plot(x,y,':')
# plt.plot(x2,y2,'--')

# Rang berish turlari:
# RGB=(0,1,0) orqali ham rang berish mumkin -- 4-argument berish mumkin
# Codlar orqali - #code- 16lik sanoq sistemasi
# line = plt.plot(x, y, 'g--h', x2, y2, 'r:v',markerfacecolor='b', markersize=10)
# print(line)

# setp()-nomlangan argument
# plt.setp(line,marker='o',markerfacecolor='red',markersize=10)
# plt.setp(line,linestyle='--',linewidth=5)

# grid 'setka'hosil qiladi
# plt.grid(True)
# show() metodi xosil qilingan massivni ko'rsatib beradi
# plt.show()

x = np.arange(-2 * np.pi, 2 * np.pi, 0.1)
y = np.cos(x)
plt.plot(x, y)
plt.grid()
plt.show()

# fill_between()-metodi
plt.fill_between(x, y,where=(y<0), facecolor='blue', alpha=0.5)
plt.fill_between(x, y,where=(y>0), facecolor='red', alpha=0.5)
