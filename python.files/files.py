
# 'w' : (write)  yazma modu
# ** dosyayı konumda oluştururlar.
# ** dosya içeriğni siler ve yeniden ekleme yapar.





# file = open('newfile.txt','w')            # open dosyayı açar. 'w' ilgili konumda dosya oluşturur. 'r' ise okuma içindir.

# file.close                     # 'close' actığın dosyayı kapatır.


# file = open("C:/Users/90531/Desktop/new_file.text", "w")        # masaüstüne kaydetmek için yapılır.

# print(file)


# file = open('newfile.txt','w',encoding='utf-8')    # encoding türkçe karakterleri yazmayı sağlar.

# # file.write('Yusuf Özen')                # oluşturulan dosyanın içine istediğn şeyleri yazabilirsin.

# # file.close()




# 'a' : (append) ekleme modu. Dosya konumda yoksa oluşturur.

# file = open('newfile.txt','a',encoding='utf-8')   # append tekrar ekler her çalıştırdığımızda.
# file.write('\npython')
# file.close()





# 'x' : (create) oluşturma modu. Dosya zaten varsa hata verir.

file = open('newfiles.txt','x',encoding='utf-8')  



