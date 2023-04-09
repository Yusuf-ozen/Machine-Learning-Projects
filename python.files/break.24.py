# name = "Sadık Turan"

# for letter in name:


#     # if (letter == "a"):        # "a" harfini gördüğü an programı bitirir.
#     #     break



#     if (letter == "ı"):        # "ı" harfini gördüğü zaman devam eder bu yüzden "ı" yı yazmaz.
#         continue

#     print(letter)



# x = 0

# while x < 5:
#     if (x == 2):        # x 2'ye geldiğinde programı durdurur
#         break
#     print(x)
#     x += 1





# x = 0

# while x < 5:
#     x += 1
#     if (x == 2):        # x 2'ye geldiğinde programı tekrar çalıştırdığı için 2 yi yazmaz.
#         continue
#     print(x)
  


# ornek: 1'den 100'e kadar tek sayıların toplamı kaçtır?

x = 1
result = 0

while x <= 100:
    x += 1

    if x % 2 == 1:
        continue

    result += x
  
print(result)

