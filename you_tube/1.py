#Timer
import time

my_time = int(input(">>>"))
for x in range(my_time, 0, -1):
    days=int(x/86400)
    hours=int(x/3600)%24
    minutes = int(x / 60) % 60
    seconds = x % 60
    print(f'{days}:{hours:02}:{minutes:02}:{seconds:02}')
    time.sleep(1)

print("TIME UP!")
