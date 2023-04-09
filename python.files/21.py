# Python ile bir liste içinde 5’in katları olan sayıları listeleme.


x = [12, 25, 45, 33, 69, 70, 110, 205]
sayac = 0

for y in x:
    if (y % 5 == 0):
        sayac += 1
        print(y)



print(f'{sayac} tane 5 e bölünen sayı vardır.')



