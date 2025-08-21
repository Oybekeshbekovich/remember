#Datetime
import datetime

date = datetime.date(2025, 1, 3)
today = datetime.date.today()

time = datetime.time(10, 45, 13)
now = datetime.datetime.now()

now = now.strftime("%H:%M:%S %d/%m/%Y")

target_datetime = datetime.datetime(2025, 1, 3, 10, 45, 13)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print('Target date has passed')
else:
    print('Target date has not passed')
