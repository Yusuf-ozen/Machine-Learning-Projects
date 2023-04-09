# Kullanıcın girdiği iki sayı arasındaki sayıların toplamını gösteren Python Örneği.


ilk = int(input("ilk sayi :  "))
son = int(input("son sayi :  "))
top = 0

for num in range(ilk, son + 1):
    top += num

print('Toplam :  ', top)