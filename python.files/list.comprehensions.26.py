for x in range(10):
    print(x)



number = [x for x in range(10)]       # aralıktaki sayıları liste şeklinde yazdırır.

print(number)



for x in range(10):
    print(x ** 2)           # Aralıktaki sayıların karesini yazdırır.


number = [x ** 2 for x in range(10)]        # Aralıktaki sayıların karesini listeler.

print(number)      



number = [x ** 2 for x in range(10) if x % 3 == 0]       # sadece 3'e bölünenlerin karesini alır.
print(number)

#########

myString = "Hello"
myList = []



for letter in myString:
    myList.append(letter)

print(myList)



myList = [letter for letter in myString]   # myString dekileri  letter'a atıp my list'de yazdırır.
print(myList)

###########


years = [2001, 1987, 1956, 1888,2010]

for year in years:
    print(2020 - year)


ages = [2020 - year for year in years]
print(ages)



results = [x if x % 2 == 0 else "TEK" for x in range(1,10)]

print(results)


total = [y*y  for y in range(50,200,10)]  # sağ tarafa önce for ' u normal şekilde yaz sonra sola istediğin şekilde yaz.
print(total)




result = []

for x in range(3):                 # iç içe 2 döngü olduğu için ilk for'un herbir karakterine alttakinin 3 karakteri yazdırılır.
    for y in range(3):
        result.append((x,y))

print(result)


result = [(x,y,z) for x in range(3)  for y in range(3) for z in range(3)]
print(result)


