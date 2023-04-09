numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]


val = min(numbers)          # minumum sayıyı bulur.
val = max(numbers)          # maximum sayıyı bulur.
val = min(letters)          # alfabetik olarak ilk olanı yazdırır.
val = max(letters)          # alfabetik olarak son olanı yazdırır.

val = numbers[3:6]
val = numbers[:3]

numbers[4] = 40

# numbers.append("49")       #Listeye istediğin şeyleri ekler.
# numbers.append(59)

numbers.insert(3, 78)     #Listeye ekleyeceğin şeyi ilk kısımda index no sunu ikinci kısma ekleyeceğin şeyi yaz.
numbers.insert(-1, 99)

# numbers.pop()             # Listedeki son elemanı siler.
# numbers.pop(2)            # Listedeki index numarası verdiğini siler.
# numbers.pop(-1)   


# numbers.remove(1)        # Listedki yazdığın elemanı siler.

numbers.sort()             # Listedeki elemanları küçükten büyüğe sıralar.  
letters.sort()             # Listedeki elemanları alfabetik olarak sıralar.

numbers.reverse()          # Listedeki elemanları tersine sıralar.
letters.reverse()          # Listedeki elemanları tersine sıralar.




print(numbers)
print(letters)


print(len(numbers))
print(len(letters))


print(numbers.count(10))        # istediğin sayının listede kaç defa olduğunu bulur.
print(letters.count("a"))

numbers.clear()                 # İstediğn listenin elemanlarını temizler.
print(numbers)
