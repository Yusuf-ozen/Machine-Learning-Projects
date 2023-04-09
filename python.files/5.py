# Girilen Sayının Tek mi Çift mi Olduğunu Bulan Python Örneği.

x = int(input("Enter a number :  "))


while (x > 0):
    if (x % 2 == 0):
        print(F"{x} is a even")
        break
    else:
        print(f"{x} is odd")
        break