# 1'den 100'e kadar

# x = 0


# while x < 100:       # Burada while ' ın 100 ' e kadar çalışmasını istiyoruz.
#     if x % 2==0:      # Çift sayıları yazdırır.
#         print(f"cift sayi : {x}")
#     else:
#         print(f"tek sayi : {x}")
#     x = x + 1        # Burada x ' in değerini sürekli arttırıyoruz.

# print("Bitti!")




name = ""                      # False
while not name.strip:    #boşluk karakterini siler.     # Her zaman girmemizi sağlar ismini. True demek not name.
    name = input("Enter name : ")       # eğer ismini girmezsen sürekli sormaya devam eder.


print(f"Hello, {name}")
