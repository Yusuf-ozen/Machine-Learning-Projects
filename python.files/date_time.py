from datetime import datetime
from datetime import timedelta
# from datetime import date
# from datetime import time


# import datetime




simdi = (datetime.now())     # su anki tarhi verir. 
# simdi = datetime.today()     # bugunku tarihi verir.

# result = dir(datetime.time)
# result = dir(datetime.date)

result = simdi.year
result1 = simdi.month
result2 = simdi.day
result3 = simdi.hour
result = datetime.ctime(simdi)       # Tarih hakkında bilgi verir.
result = datetime.strftime(simdi, '%Y')
result = datetime.strftime(simdi, '%X')
result = datetime.strftime(simdi, '%d')
result = datetime.strftime(simdi, '%A')
result = datetime.strftime(simdi, '%B')
result = datetime.strftime(simdi, '%Y %B %A')



t = '15 April 2019 hour 10:12:30'
dt = datetime.strptime(t, '%d %B %Y hour %H:%M:%S')

birthday = datetime(1983, 6, 14)


result = datetime.timestamp(birthday)   # saniye cinsinden cevirir.
result = datetime.fromtimestamp(result)    # datetime cevirir.
result = simdi - birthday        # time delta

# result = result.days
# result = result.seconds
result = result.microseconds


# result = simdi + timedelta(days = 10)          # su anki gune 10 ekler.
# result = simdi + timedelta(days = 15, seconds = 10)


print(birthday)
print(result)

# t = '21 Nisan 2021'

# gun, ay, yil = t.split()
# print(gun)
# print(ay)
# print(yil)




# print(result)
# print(result1)
# print(result2)
# print(result3)


print(dt)









