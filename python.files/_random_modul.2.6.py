import random


# result = dir(random)

# result = help(random)


result = random.random()         # Burada 0.0 ve 1.0 arasında bir sayı tutar.

result = random.random() * 100   # Seçilen sayının 100 katını yazdırır.

result = random.uniform(1,10)     # 1 ile 10 arasındaki sayılardan rastgele secer.

result = int(random.uniform(1,10))      # 1 ile 10 arasındaki tam sayıları rastgele secer.

result = random.randint(10,100)        # 10 ile 100 arasında rastgele bir tamsayı seçer.


names = ['ali', 'ahmet', 'yağmur', 'ayşe']

greeting = 'Hello bro'

result = names[random.randint(0,len(names) - 1)]      # rastgele bir indexdeki ismi seç.

result = random.choices(names)        # rastgele bir ismi secer.

result = random.choice(greeting)      # Greeting'deki rastgele bir karakteri secer(bosluk dahil)


liste = list(range(10))
random.shuffle(liste)           # 1 den 10 a kadar rastgele bir liste oluşturur.


result = liste



liste = range(100)
result = random.sample(liste, 3)        # listeden istediğn kadar elemanı almanı sağlar.

result = random.sample(names, 2)


result = random.sample(greeting, 2)


print(result)




