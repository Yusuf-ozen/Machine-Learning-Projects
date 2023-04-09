# 1 den Kullanıcının Girdiği Sayıya Kadar Sayıları Listeleyen Python

x = int(input("Enter a number : "))

for i in range(1,x):
    print(i)


i = [ i for i in range(1,x)]   # yan yana yazdırır.

print(i)