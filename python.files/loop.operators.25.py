# ***range***



# for item in range(50,150,10):         # range'in içine ne yazdıysan o kadar ya da o aralıkta yazdırır.
#     print(item)                       # range ' in 2. virgulden sonraki artış miktarını gösterir.


# print(list(range(50,150,20)))        # Bu sayıları listeye çeviriyoruz.





# ***enumerate***

"""

index = 0

greeting = "Hello There"

for letter in greeting:
    print(f"index : {index}   letter : {letter}")
    index += 1

"""


greeting = "Hello There"

for item in enumerate(greeting):             # enumerate index adreslerini yazdırır.

 print(item)
 


# ***zip***

list1 = [1, 2, 3, 4, 5]


list2 = ["a", "b", "c", "d", "e"]
 

list3 = [100, 200, 300, 400, 500]

print(list(zip(list1, list2,list3)))            # zip listeleri eşleştirir. 

for item in zip(list1, list2,list3):        # oluşan listeleri alt alta yazdırır.
    print(item)


for a,b,c in zip(list1, list2,list3):        # sadece ilk listedeki elemanları yazdırır.,
    print(a)

