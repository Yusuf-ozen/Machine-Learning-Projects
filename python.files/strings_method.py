message = 'Hello there. My name is Yusuf '

# message = message.upper()    # buradaki upper bütün harfleri büyük yazdırır.
# message = message.lower()    # bütün harfleri küçük yazdırır.
# message = message.title()    #kelimelerin başını büyük harfle yazdırır.
# message = message.capitalize()   #sadece ilk harfi büyük yazdırır.
# message = message.strip()        #ilk ve sondaki boşlukları temizler.
# message = message.split()        #her kelimeyi ayrı ayrı çalıştırır.
# message = message.split('.')   
# message = '   '.join(message)             #split ie ayırdığımız kelimelerin arasına neler geleceğini belirliyor.

# index = message.find('My')       #istediğin kelimenin ilk harfini index no ile bulur.

# print(index)



# isFound = message.startswith('H')      # Eger 'H' ile başlıyorsa true yazdırır.
# isFound = message.endswith('H')          # Eger 'H'  ile bitiyorsa True yazdır.
# print(isFound)

# message = message.replace('My', 'Ben')     # Burada ilk ifadenin yerine ne yazmak istersen onu yazarsın.


message = message.center(100,'*')             # mesajı 100 karakterlik bir diziye sıkıştırır. ikincisi aralara birşey yazdırır.

print(message)
# print(message[0])               # x.dizidekini yazdırır.