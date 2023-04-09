# 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Python Örneği



for x in range(1,100):
    if (x % 3 == 0) or (x % 5 == 0):
        print(x)