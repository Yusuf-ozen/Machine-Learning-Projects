def sayHello(name = "user"):                  # def komutu fomksiyon oluşturmaya yarar.
   
   
    # print("Hello " + name)

    return "Hello " + name

msg = sayHello("yusuf")          # Bu şekilde fonksiyonu çağırıyoruz.

# sayHello("ozen")  

# sayHello()        # Burada name ' e atadığımız user'ı yazdırır.


print(msg)





def Total(number1, number2):
    return number1 + number2


result = Total(10, 20)
result = Total(15, 25)

print(result)




def yasHesapla(dogumBilgisi):
    return 2020 - dogumBilgisi


ageYusuf = yasHesapla(2000)
ageTuran = yasHesapla(1992)


print(ageTuran)
print(ageYusuf)





def emkliligeKacYilKaldi(dogumBilgisi, isim):

    """
    DOCSTRING: Doğum yılınıza göre emekliliğinize kaç yıl kaldı.
    INPUT: Doğum Yılı
    OUTOUT: Hesaplanan Yıl Bilgisi

    """
    yas = yasHesapla(dogumBilgisi)

    emeklilik = 65 - yas

    if (emeklilik > 0):
        print(f"emekliliğinize {emeklilik} yıl kaldı. ")

    else:
        print("Emeklilik vaktiniz gelmiştir.")


emkliligeKacYilKaldi(1983, "ali")
emkliligeKacYilKaldi(1943, "ahmet")





print(help(emkliligeKacYilKaldi))               # Yazdiğin açiklamaları gosterir.


list = [1, 2, 3]
print(help(list.append))   # bununla ilgili bilgi verir.



