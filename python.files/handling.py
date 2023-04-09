# error handling => hata yönetimi



# try:             # try ilk hata komutudur.


#     x = int(input('x : '))
#     y = int(input('y : '))
#     print(x / y)


# # except ZeroDivisionError:              # 'except' den sonra hangi hata yapılabilecekse o yazılır.
# #     print('y için sıfır girilemez.')   # Burada da hata için bir mesaj yazılır.
# # except ValueError:
# #     print('x ve y için harf kullanılamaz.')




# except (ZeroDivisionError,ValueError) as e:        # as 'e' hangi türden bir hata olduğunu bildiriyor.
#     print('Hatalı yazım')
#     print(e)



#########################################################################################





# try:            

#     x = int(input('x : '))
#     y = int(input('y : '))
#     print(x / y)


# except:       
#     print('Hatalı yazım')          # Hata olduğunu tek yazar.






###################################################################################



# try:            

#     x = int(input('x : '))
#     y = int(input('y : '))
#     print(x / y)


# except:       
#     print('Hatalı yazım')

# else:
#     print('her şey yolunda')





#################################################################################


# while True:                            # Doru şekilde girene kadar sorar.
#     try:            

#         x = int(input('x : '))
#         y = int(input('y : '))
#         print(x / y)


#     except:       
#         print('Hatalı yazım')

#     else:
#         break





###########################################################################





while True:                        
    try:            

        x = int(input('x : '))
        y = int(input('y : '))
        print(x / y)


    except Exception as ex:       
        print('Hatalı yazım', ex)

    else:
        break
    finally:
        print('try except sonlandı.')










