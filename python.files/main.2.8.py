import mod                # mod.py adlı dosyamızda yazdığımız kodları burada modul olarak kullanıyoruz

# result = help(mod)          # Burada modulumuz hakkında bilgi alabiliriz.

result = help(mod.func)       # Burada func gibi özel bilgi alabiliriz..

result = (mod.number)          # Burada number'ı ekranda çalıştırabiliriz.

result = mod.numbers            # Numbers 'ı çalıştırabiliriz.

result = mod.person["name"]       # persondaki name'i çalıştıraniliriz.

result = mod.func(10)                  # Func çalışır.



p = mod.Person()
p.speak()                # classdaki obje üzerinden speak'i çağırıyoruz.







print(result)

