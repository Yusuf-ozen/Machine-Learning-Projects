# Identity Operators : is

"""
# x = y = [1, 2, 3]

# z = [1, 2, 3]

# print(x == y)
# print(x == z)


# print(x is y)       # aynı adreslerin olması gerekir.
# print(x is z)       # x ve z aynı adreste olmadıkları için false. 

"""



# x = [1, 2, 3]
# y = [2, 4]

# del x[2]
# y[1] = 1
# y.reverse()         # listeyi ters çevirir.

# print(x == y)        # değerlerdeki eşitliğe bakar ama 'is' adrese bakar. Yani aynı adrese tanımlamadık.
# print(x is y)
# print(x is not y)       # 'is' operatorunun tersidir.






# Membership Operator : in

x = ["apple", "banana"]
print("banana" in x)                  # 'in' istenilen bilginin içerde olup olmadığını kontrol eder.

name = "Yusuf"
print("u" in name)                 # 'u' harfinin verilenin içinde olup olmadığını kontrol eder.
print("u" not in name)             # içinde olmadığını kontrol ediyor.
