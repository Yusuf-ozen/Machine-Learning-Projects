# Bankamatik Uygulaması

hesap_A = {

    'ad' : 'sadık',
    'hesapNo' : '123456',
    'bakiye' : 3000,
    'ekHesap' : 2000
}



hesap_B = {

    'ad' : 'Ali',
    'hesapNo' : '23456',
    'bakiye' : 2000,
    'ekHesap' :1000
}

para = int(input("Kac para cekmek istersiniz :  "))

def paraCek(hesap, miktar):
    print(f"Merhaba {hesap['ad']}")


    if (hesap['bakiye'] >= miktar):
        hesap['bakiye'] -= miktar
        print('Paranızı alabilirsiniz.')

    else:
        toplam = hesap['bakiye'] + hesap['ekHesap']



        if (toplam >= miktar):
            ekHesapKullanımı = input("Bakiyeniz yetersiz ek bakiyenizi kullanmak istiyor musunuz?(e/h) :  ")

            if (ekHesapKullanımı == 'e'):
             
                ekHesapKullanılacakMiktar = miktar - hesap['bakiye']
                hesap['bakiye'] = 0
                hesap['ekHesap'] -= ekHesapKullanılacakMiktar

                print('Paranızı alabilirsiniz')

            else:
                print(f"{hesap['hesapNo']} nolu hesabınızdan {hesap['bakiye']} TL bulunmaktadır.")


        else:
            print('Yetersiz bakiye')




def bakiyeSorgula(hesap):
    print(f"{hesap['hesapNo']} nolu hesabınızda {hesap['bakiye']} TL bulunmaktadır. Ekhesap limitimiz ise {hesap['ekHesap']} TL dir.")





paraCek(hesap_A, para)

bakiyeSorgula(hesap_A)

print('***********************************')

paraCek(hesap_A, para)
bakiyeSorgula(hesap_A)






















