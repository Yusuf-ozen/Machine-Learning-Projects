import os
import date_time


# result = dir(os)

# result = os.name




# os.chdir('..')
# os.chdir('..')




# result = os.getcwd()         # bu dosyanın hangi klasorlerde oldugunu gosterir.

# os.chdir('C://')


# os.makedirs('newdirectory/yeniklasor')

# os.mkdir('newdirectory')



# for dosya in os.listdir():           # sadce py uzantılı dosyaları gösterir.
#     if dosya.endswith('.py'):
#         print(dosya)


# result = os.stat('date_time.py')        # bilgi sahibi olmak istediğin dosyayı gösterir.

# result = result.st_size/1024            # dosya boyutunu bayt cinsinden verir.
# result = datetime.date_time fromtimestamp(result.st_ctime)



# os.system("notepad.exe")         # microsofttaki herhangi bir uygulamayı calistirir.

# print(result)




##### path ######  

result = os.path.abspath('OS.py')     # istediğin dosyanın tam konumunu verir.
result = os.path.exists('OS.py')        # yazdigin dosyanin klasorde olup olmadigini kontrol eder.
result = os.path.splitext('OS.py')     # dosyanın uzantisini yazdirir.




print(result)















