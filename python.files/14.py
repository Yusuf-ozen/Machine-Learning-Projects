# Girilen Sayının Asal Sayı mı Değil mi olduğunu bulan Python Örneği
"""

x = int(input('enter a number :  '))



if (x <= 1):
    print(f'{x} is not prime')


else:

    for i in range(2,x):
        if (x % i == 0):
            print(f'{x} is not prime')
            break

        else:
            print(f'{x} is prime')
            break

"""




y = int(input('Enter a number : '))
counter = 0

for j in range(2,y):
    if (y % j == 0):
        counter += 1

if (counter != 0):
    print('not prime')

else:
    print('prime!')






