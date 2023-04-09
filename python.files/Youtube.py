'''

insanlar = [
     {

    'ilk_isim' : 'Yusuf',
    'soy_isim' : 'Ozen',
    'Yas' : '20',
    'Ders' : 'Python'

}

,

{
    'ilk_isim' : 'Yusuf',
    'soy_isim' : 'Ozen',
    'Yas' : '20',
    'Ders' : 'Python'

}



]
# print(type(insanlar))

# print(insanlar["ilk_isim"])            # Bu sekilde ulaşılır
# print(insanlar.get("ilk_isim"))        # Bu sekilde de ulaşılır

# del(insanlar['Yas'])

# print(insanlar)

print(insanlar )




'''




# def toplam(sayi1, sayi2):




#     return (sayi1 + sayi2)

# x = toplam(34, 43)

# print(x)


# x = 30

# if x > 20:
#     print('x 20 den buyuktur')

# elif (x ==20):
#     print('x 20 dir')

# else:
#     print('x 20 den kucuktur')



"""

x = 20

if (x == 20) or (x < 20):
    print('x 20 ye esit veya kucuktur')

elif x >20 and x < 25:
    print('x 20 ile 25 arasındadır.')


"""




# sayilar = [1, 2, 3]

# aradigim_sayi = 3

# if aradigim_sayi in sayilar:
#     print('aradiğim sayi vardır.')


# print(aradigim_sayi in sayilar)         >>>>   True cevabı verir.







# meyveler = ['kavun', 'karpuz', 'elma']



# for x in meyveler:

#     print(x)

#     if x == 'karpuz':
#         print('oooooooo')


'''


meyveler = ['kavun', 'karpuz', 'elma']



for x in meyveler:
    print(x)
    
    if x == 'karpuz':
        break


'''



# count = 3

# while count != 0:
#     print(count)
#     count -= 1




class Kullanici:


    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas


    def selamla(self):
        print(f'oo hosgeldniz benim adım {self.isim}')


"""

kullanici1 = Kullanici('Yusuf', 20)



print(kullanici1.isim)

kullanici1.selamla()          # bu sekilde selamla fonksiyonu calisir.

kullanici2 = Kullanici('Ali', 25)

print(kullanici2.isim)

kullanici2.selamla()

"""


class Musteri(Kullanici):

    def __init__(self, isim, yas):
        self.isim = isim
        self.yas = yas
        self.bakiye = 0
        # super().__init__(isim, yas)       # super kullanarak selfsiz yapabilirsin.


    def bakiyemi_sorgula(self):

        return self.bakiye


    def bakiye_arttır(self):
        self.bakiye += 10

    def bakiye_cek(self):
        self.bakiye -= 5



muster1 = Musteri('Ahmet', 39)

print(muster1.bakiyemi_sorgula())

muster1.bakiye_arttır()

print(muster1.bakiyemi_sorgula())

muster1.bakiye_cek()

print(muster1.bakiyemi_sorgula())

print(muster1.yas)












