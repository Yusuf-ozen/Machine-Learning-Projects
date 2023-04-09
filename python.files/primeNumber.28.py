# Girilen bir sayının asal olup olmadığını kontrol eden kod yazınız.

"""

x = int(input("Enter a number :  "))

if (x > 1):
    for i in range(2,x):
       
        if (x % i) == 0:
            print(f"{x} is a not prime number")
            break

        else:
            print(f"{x} is  a prime number")
          

else:
    print(f"{x} is not prime number.")
 

 """



number = int(input("Enter a number :  "))
prime = True


if (number == 1):
     print("Number is not prime!")  # ayrıca prime = False yazabiliriz.


for i in range(2,number):
    if (number % i == 0):
        print("number is not a prime!")
        prime = False                            # prime değeri false olduğu için break yapılır.
        break


if prime:                                # True  yani false'un tersi olduğu için programı çalıştırır. 
    print("Number is prime")