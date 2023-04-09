
'''


def my_decorate(func):
    def wrapper(name):
        print("fonksiyondan önceki islemler ")
        func(name)
        print("fonksiyondan sonraki islemler ")
    return wrapper




@my_decorate        # bu fonksiyonu my_decorate e atar.

def sayHello(name):
    print("Hello", name)






# def sayGreeting():
#     print("Greeting")



# sayHello = my_decorate(sayHello)
sayHello("Yusuf")

# sayGreeting = my_decorate(sayGreeting)         # bu sekilde sayGreeting veya sayHello yu my_decorate in icinde cagirabilirsin.
# sayGreeting()


'''



import math
import time



def calculate_time(func):
    def inner(*args, **kwargs):
        
        start = time.time()           # fonksiyonun ne kadar surede calistigina bakar.
        time.sleep(1)                # 1 saniye bekler ve sonra isleme devam eder.


        func(*args, **kwargs)  
    
        finish = time.time()

        print("Fonksiyon " + func.__name__ + " " + str(finish - start) + " saniye surdu.")


    return inner


@calculate_time
def usAlma(a, b):

                    
    print(math.pow(a, b))
    


@calculate_time
def faktoriyel(num):

    print(math.factorial(num))


@calculate_time
def toplam(a, b):
    print(a + b)


@calculate_time
def carpim(a, b):
    print(a * b)




usAlma(99, 99)
faktoriyel(5)
toplam(35, 9887)
carpim(234, 675)




