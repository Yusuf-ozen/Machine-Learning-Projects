# # x = int(input('sayı giriniz : '))

# # if x > 5:
# #     raise Exception('x 5 den buyuk olamaz.')          # "raise"  ifadesi exceptionda bir şey yazdırıken kullanılır.




# def check_password(psw):
#     import re                  

#     if(len(psw) < 8):
#         raise Exception('8 haneli şifre giriniz.')


#     elif not re.search("[a-z]", psw):    # Burada eğer küçük harf bulamazsa diye çalışır.
#         raise Exception('Parola küçük harf içermelidir.')


#     elif not re.search("[A-Z]", psw):    # Burada eğer büyük harf bulamazsa diye çalışır.
#         raise Exception('Parola büyük harf içermelidir.')


#     elif not re.search("[0-9]", psw):    
#         raise Exception('Parola rakam içermelidir.')


#     elif not re.search("[_@$]", psw):   
#         raise Exception('Parola alpha numeric karakter içermelidir.')


#     elif re.search("/s", psw):              # boşluk karakterini ifade ettik.
#         raise Exception('Parola boşluk içermemelidir.')


#     else:
#         print('geçerli parola')


# password = '12345678aA@'


# try:
#     check_password(password)

# except Exception as ex:
#     print(ex)

# else:
#     print('Geçerli parola')

# finally:
#     print('validation tamamlandı.')



class Person:
    def __init__(self, name, age):
        if(len(name) > 10):
            raise Exception('name alanı fazla karakter içeriyor')

        else:
            self.name = name


p = Person('aliiiiiiiii',1989)

