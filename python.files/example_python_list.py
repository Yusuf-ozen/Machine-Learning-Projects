#1 - 'Bmv, Mercedes, Opel, Mazda' elemanlrına sahip bir liste oluşturunuz.
cars = ['Bmv', 'Mercedes', 'Opel', 'Mazda']
print(cars)


#2 - Liste kaç elemanlıdır?

result = len(cars)


#3 - Listenin ilk ve son elemanı nedir?

result = cars[0]
result = cars[3]
result = cars[-1]
result = cars[-4]

#4 - Mazda değerini Toyota ile değiştirin.

# cars[-1] = "Toyota"
# result = cars[-1]
# result = cars

#5 - Mercedes listenin bir elemanı mıdır?

result = "Mercedes" in cars         # Bu elemanın içinde olup olmadığını kontrol eder.

#6 - Listenin -2 indeksindeki değer nedir?

result = cars[-2]

#7 - Listenin ilk 3 elemanını alın.

result = cars[0:3]
result = cars[:3]
result = cars[-2:]

#8 - Listenin son iki elemanı yerine 'Toyota' ve 'Renault' değerlerini ekleyin.

cars[-2:] = ["Toyota", "Renault"]
result = cars

#9 - Listenin üzerine 'Audi' ve "Nissan" değerlerini ekleyin.

result = cars + ["Audi", "Nissan"]


#10 - Listenin son elemanını silin.

# del cars[-1]
# result = cars

#11 - Listenin elemanlarını tersten yazdırın.

result = cars[::-1]

#12 - Aşağıdaki verileri bir liste içinde saklayınız.

    # studentA = Yiğit Bilgi 2010, (70, 60, 70)
    # studentB = Sena Turan 1999, (80, 80, 70)
    # studentC = Ahmet Turan 1998, (80, 70, 90)


studentA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
studentB = ["Sena", "Turan", 1999, [80, 80, 70]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

#13 - Liste elemanlarını ekrana yazdırın.


result = studentA[1]
result = studentB[3][1]

result = f"{studentA[0]} {studentA[1]} {2021 - studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2]) / 3}."

print(result)