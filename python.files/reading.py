# try:

#     file = open('newfile.txt','r')       # r yazmasak da r olarak çalışır
#     print(file)


# except FileNotFoundError:
#     print('dosya okuma hatası')

# finally:
#     print('dosya kapandı')
#     file.close()



file = open('newfile.txt','r', encoding='utf-8')

# # for döngüsü

# for i in file:
#     print(i, end='')          # buradaki end boşlukları siler.




# *****************read() fonksiyonu

# content1 = file.read()

# print('içerik 1')
# print(content1)


# content2 = file.read()


# print('içerik 2')
# print(content2)




# content = file.read(5)
# content = file.read(3)
# print(content)




# *****************readline() fonksiyonu


# content = file.readline()         # readline fonksiyonu sadece bir satır okur.
# print(content)





# *****************readline() fonksiyonu

liste = file.readlines()         # herbir bilgiyi liste elemanı olarak alır.
print(liste)

print(liste[0])
print(liste[1])



file.close()








