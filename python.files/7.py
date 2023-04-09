# Yaşı Girilen Kişinin Ehliyet Alıp Alamayacağını Gösteren Python Örneği

date = int(input("Enter Date of birth :  "))

age = 2020 - date 

if (age > 18):
    print("you can have license \o/")

else:
    print(f"You should wait {18 - age} year")