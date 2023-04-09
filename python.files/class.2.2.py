# class


class Person:                  # class'tan sonra genellikle büyük harfle başlanır.
    # pass


    # class attributes

    address = 'no information'


    # constructors method

    def __init__(self, name, year):          # self bilgiler için kullanılır.


    # object attributes


        self.name = name
        self.year = year
        # print('init metodu çalıştı.')

    # instance methods

    def intro(self):
        print("Hello There :) I am " + self.name)


    def calculatAge(self):
        return 2020 - self.year


# object, instance

p1 = Person('Yusuf', 1999)
p2 = Person('ahmet', 2000)


p1.intro()
p2.intro()

print(f"ad : {p1.name}  yas : {p1.calculatAge()}")
print(f"ad : {p2.name}  yas : {p2.calculatAge()}")


# # updating

# p1.name = 'yusuf'          # p1 name 'i yusuf olarak değiştirir.
# p2.address = 'istanbul'    # p2 address ' i istanbul olarak değiştirir.


# # accessing object atributes

# print(f"name : {p1.name}  yas = {2020 - p1.year}  address : {p1.address}")
# print(f"name : {p2.name}  yas = {2020 - p2.year}  address : {p2.address}")


# print(p1)
# print(p2)


# print(type(p1))
# print(type(p2))

# print(p1 == p2)               # burada false yazdırır çünkü adresler farklıdır.







class Circle:
    # Class object attribute
    pi = 3.14


    def __init__(self, yaricap = 1):
        self.yaricap = yaricap


    # Methods
    def cevreHesapla(self):
        return 2 * self.pi * self.yaricap                  # Burada ve alttakinde pi 'yi self olarak yazılmalıdır yoksa pi tanımlanmamış olur.


    
    def alanHesapla(self):
        return self.pi * self.yaricap * self.yaricap          # ayrıca (self.yaricap ** 2)  yazabilirsin.




c1 = Circle()      # Bir şey yazmazsan yarıçap = 1 olur.
c2 = Circle(5)     # Yarıçap = 5 yaptık.



print(f"Cevre1 :  {c1.cevreHesapla()}  Alan1 : {c1.alanHesapla()}")
print(f"Cevre2  :  {c2.cevreHesapla()}   Alan2 : {c2.alanHesapla()}")
