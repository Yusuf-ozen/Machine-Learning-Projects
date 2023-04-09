website = 'http://www.SadıkTuran.com'
course = "Phyton Kursu: Baştan Sona Phyton Programlama Rehberiniz (40 saat)"

#1 - 'Course' karakter dizisinde kaç karakter bulunur ?

result = len(course)

#2 - 'website' içinden www karakterlerini alın.
result = website[7:10]

#3 - 'website' içinden com karakterlerini alın.
result = website[22:25]

#4 - 'Course' içinden ilk 15 ve son 15 karakterini alın.

result = course[:15]
result = course[-15:]

#5 - 'Course' karakterleri tersten yazdırın. 

result = course[::-1]        #butun karakterleri yazar ve -1 yazıldığında tersten yazar.



name, surname, age, job = 'Bora', 'Yılmaz', 32, 'Mühendis'

#6 - Yukarıda verilenlere göre asagidakileri yazdırın.
#  Benim adım Bora Yılmaz, yaşım 32 ve Mesleğim mühendis

print(f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}",)

#7 - 'Hello World ' ifadesindeki W yerine w yazdırın.

s = 'Hello World'

result = s[6]
s = s[0:6] + 'w' + s[-4:]
print(s)
s.replace('W','w')    #Burada başta  yazılanla ikinci yazılan yer değişir.

#8 - 'abc' ifadesini yan yana 3 defa yazdırın.

result = 'abc' * 3

print(result)