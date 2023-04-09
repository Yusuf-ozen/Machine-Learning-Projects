def changeName(n):
    n = "yusuf"



name = "yiğit"

changeName(name)
print(name)




def change(n):
    n = [1, 2, 3, 4]


list = ["y", "u", "s", "u", "f"]

change(list)

print(list)






def change(n):
    n[0] = "elma"    # listenin 0. elemanına elmayı atar.


list = ["armut", "kiraz"]

change(list)

print(list)






# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara", "izmir"]

# n = sehirler[:]   # slicing

# n[0] = "istanbul"

# print(sehirler)
# print(n)




def add(a, b, c = 0):        # sıfıra eşitlediğimizde hem 2 hem de üç tanesiyle toplama işlemi yapabiliriz.
    return sum((a, b, c))


print(add(10, 20, 30))





# def add(*params):            # bir sürü sayı için işlem yapılacaksa * ifadesi kullanılabilir.
#     print(params)

#     return sum(params)


# print(add(10, 40, 50, 100))





# def add(*params):
#     sum = 0
    

#     for n in params:
#         sum += n

#     return sum


# print(add(123, 345, 456, 124))

"""

def displayUser(**args):                                      # dictionary listesi olarak ** kullanılır.
    for key, value in args.items():
        print("{} is {}".format(key,value) )



displayUser = (name= "Çınar", age = 2, city = "istanbul")                                                   # !!!!!!  Hata var ama bulamadım. !!!!!!
displayUser = (name = "Ada", age = 12, city = "izmir", phone = "14242536")
displayUser = (name = "Turan", age = 22, city = "Muş", phone = "72636788", mail = "turan@gmail")

"""



def myFunction(a, b, *args, **kwargs):

    print(a)
    print(b)
    print(args)
    print(kwargs)


myFunction(10, 20, 30, 40, 50, key1 = "value1", key2 = "value2")

