#MULTITHREADING->bir vaqtning o'zida bir nechta vazifalarni bajara oladi
import threading
import time

def walking_dog(first,last):
    time.sleep(8)
    print(f'You finish walking{first} {last}')
def take_out_trash():
    time.sleep(2)
    print(f'You take out trash')
def get_mail():
    time.sleep(4)
    print(f'You get a mail')

chore1=threading.Thread(target=walking_dog, args=("Scooby","Doo"))
chore1.start()
#chore1.join()
chore2=threading.Thread(target=take_out_trash)
chore2.start()
#chore2.join()
chore3=threading.Thread(target=get_mail)
chore3.start()
#chore3.join()
print("All chores are complete!")