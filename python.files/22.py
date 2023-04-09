# Bir string içerisinde belirlenen bir karakterin olup olmadığını kontrol eden Python programı 

'''

def kontrol(str):              # kontrol fonksiyonu oluşturduk.
  sayac = 0
  for ch in str:              # str fonksiyonundaki kelimeleri ch'ye attık.
    if ch == 'ğ':             # ch'de "ğ" olup olmadığını kontrol ettik.
      sayac = sayac + 1       # 'ğ' varsa sayacı arttırdık.
  
  if sayac == 1:              # sayaç arttıysa 'True' dedik.
    return True
  else:
    return False             # sayaç 0 kaldıysa 'False' dedik.
 


metin=input('Metin : ')



if(kontrol(metin)==True):                           # Eğer kontrol fonksiyonu True derse içinde vardır.
      print('ğ karakteri metin içinde var')


else:
      print('ğ karakteri metin içinde yok')


'''



giriş = input('kelime giriniz : ')
x = input('Hangi harfi kontrol edeceksiniz : ')

def kontrol(kelime):
    sayac = 0

    for word in kelime:
        if (word == x):
            sayac += 1

    if (sayac > 0):
        return True


    else:
        return False


if (kontrol(giriş) == True):
    print(f"içinde {x} harfi vardır.")

else:
    print(f'içinde {x} harfi yoktur!')


 