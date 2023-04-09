x = 7
hak = 5
devam = "e"

result = 5 < x < 10

# and

result = (x > 5) and (x < 10)            # "and" kullanılırsa her iki şartı sağlamalı   

# true, true => true
# true, false => false

result = (hak > 0) and (devam == "e")

# or

result = (x > 0) or (x % 2 == 0)     # "or" iki şarttan birini sağlarsa true yazdırır.

# true, false => true



# not

result = not(x > 0)   # tam ters.





print(result)

a = int(input("Enter a number :  "))

sum = ((a > 5) and (a < 10)) and (a % 2 == 0)

print(sum)







