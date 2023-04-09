# inheritance (kalıtım): miras alma

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Cat(Animal), Dog(Animal)


class Person():


    def __init__(self, fname, lname):            # def initi kullanmak için başta self ya da başka bir şey kullanman gerekir. 
        self.firstName = fname
        self.lastName = lname
        print("Person Created")



    def who_am_I(self):
        print('I am a person')



    def eat(self):
        print('I am eating now')


class Student(Person):
    def __init__(self, fname, lname, number):           # self in yanına sadece name leri belirtmemiz yeterlidir.
        Person.__init__(self, fname, lname)                   # bu yazdığımız student 'ı çalıştırırken Student taki Person özelliklerinin de kaybolmamasını sağlıyor.
        self.studentNumber = number
        print("Student Created")


    # override                            # persondaki who fonksiyonunu ezip kendi who fonksiyonumuzu oluşturduk.
    def who_am_I(self):
        print('I am a student')


    def sayHello(self):
        print('Hello I am a student')



class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname,lname)                     # super metodu kullandığımızda self'e gerek kalmıyor. self.x = y  örnek olarak.
        self.branch = branch



    def who_am_I(self):
        print(f'I am a {self.branch} teacher')





p1 = Person('Yusuf', 'Özen')
s1 = Student('Ali', 'Turan', 12345)
t1 = Teacher('Serkan', 'Kral', 'Math')

print(p1.firstName + ' ' + p1.lastName)           # first ve last name 'i çağırmak için bu ifadeyi kullanman gerekiyor.
print(s1.firstName + ' ' + s1.lastName + ' No : ' + str(s1.studentNumber))           # first ve last name 'i çağırmak için bu ifadeyi kullanman gerekiyor.


p1.who_am_I()                          # hangi fonksiyonu çağıracaksan onu noktayla yaz.
s1.who_am_I()
t1.who_am_I()

p1.eat()                       # Bu şekilde 'eat' fonksiyonunu çağırıyoruz.
s1.eat()

s1.sayHello()





