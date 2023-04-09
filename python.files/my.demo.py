# 100'e kadar 3 ün katı olan sayıları yazdır.
"""

x = int(input("Enter a number :  "))


for i in range(1,x):
    if (i % 3 == 0):
        print(i)

"""

# 1000 ' e kadarki sayilardan 7 'ye tam bölünen 5 ' tam bölünmeyen sayıları yazdırın.

"""

y = int(input("Enter a number :  "))

for i in range(1,y):
    if (i % 7 == 0) and (i % 5 != 0):
        print(i)

"""

"""

y = int(input("Enter a number :  "))

for i in range(0,y,7):
    if (i % 5 != 0):
        print(i)

"""


# 1,1000 arsındaki asal sayıları bulan kodu yazınız.

x = int(input("Enter a number :  "))

for prime in range(2,x):
    if (x > 1):

        for i in range(2,x - 1):
            if (prime % i == 0):
                break

        else:
            print(x
            )


