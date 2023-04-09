website = 'http://www.SadıkTuran.com'
course = "Phyton Kursu: Baştan Sona Phyton Programlama Rehberiniz (40 saat)"

#1 - ' Hello World ' dizisindeki baştaki ve sondaki boşluklareı silin.
result = ' Hello World '.strip()      #lstrip soldaki karakteri siler. rstrip sağdaki karakteri siler.

#2 - 'http://www.SadıkTuran.com' ifadesindeki SadıkTuran haricindeki tüm karakterleri silin.
result = website.strip('pth:/.wcom')

#3 - 'course' karakter dizisindeki tüm karakterleri küçük yapın.
result = course.lower()

#4 - 'website' karakteri içinde kaç tane 'a' vardır.
result = website.count('a',0,15)      # 0 ile 10 arasında arar.

#5 - 'website' www ile başlayıp com ile bitiyor mu?
result = website.startswith('www')      # hangi karakterle başladığını kontrol ediyor.
result = website.endswith('om')         # hangi karakterle bittiğini kontrol ediyor.

#6 - website içinde .com var mı?
# result = website.find('.com',5,15)      # istenilen karakteri index numarasına göre soldan bulur.
# result = course.rfind('Phyton')       # istenilen karakteri index numarasına göre sağdan bulur.
# result = course.index('com')          #karakteri index e göre yazar.
# result = course.rindex('com')         #karakteri sağdan index e göre yazar.

#7 - course nin içindekiler alfabetik mi?
result = course.isalpha()        # alafabetik olup olmadığını kontrol eder.
result = course.isdigit()
result = '123'.isdigit()         

#8 - 'coontents' ifadesini 50 satıra yerleştirip aralara yıldız yerleştir.
result = 'contents'.center(50, '*')
result = 'contents'.ljust(50, '*')         # kelimeyi sola alır ve diğer taraflara * koyar.
result = 'contents'.rjust(50, '*')         # kelimeyi sağa alır ve diğer taraflara * koyar.

#9 - 'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
result = course.replace(' ', '-',3)       # boşluk yerine 3 tane '-' at. 

# 10 - 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin.
result = 'Hello World'.replace('World','There')

# 11 - 'Course' karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(' ')

print(result)
