liste = ["1", "2", "5a", "10b", "abc", "10", "50"]


# liste elemanları içindeki sayısal değerleri bulunuz.




# for x in liste:
#     try:

#         result = int(x)
#         print(result)

#     except ValueError:
#         continue
      





# 2 - Kullanıcı q değerini girmedikçe aldığınız her inputun sayı olduğundan emin olunuz.
# Aksi halde hata mesajı verin.




# while True:
#     sayi = input('sayi : ')
#     if sayi == 'q':
#         break



#     try:
#         result = float(sayi)
#         print('girdiğiniz sayı : ', sayi)

#     except ValueError:
#         print('gecersiz sayı')
#         continue





# 3 -  girilen parola için türkçe karakter hatası veriniz.







# def check_password(parola):


#     turkce_karakterler = 'şçğüöıİ'

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError('hatalı karakter')

#         else:
#             pass
         
#     print('geçerli parola')


# parola = input('Parola : ')

# try:
#     check_password(parola)

# except TypeError as err:
#     print(err)






# 4 - Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verin.



def faktoriyel(x):
    x = int(x)


    if (x < 0):
        raise ValueError('0 dan büyük sayı giriniz.')



    result = 1


    for i in range(1, x + 1):
        result *= i
    return result


for x in [5, 10, 20, -3, '10a']:
    try:
        y = faktoriyel(x)

    except ValueError as err:
        print(err)
        continue


    print(y)











