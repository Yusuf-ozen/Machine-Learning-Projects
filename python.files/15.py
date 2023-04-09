# 1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan ve sonucu ekranda gösteren Python Örneği

x = int(input('Enter a number :  '))

tek_toplam = 0

cift_toplam = 0


for i in range(1, x + 1):
    if (i % 2 == 0):
        cift_toplam += i


    else:
        tek_toplam += i



print('Teklerin toplamı : ',tek_toplam)
print('Çiftlerin toplamı : ',cift_toplam)


