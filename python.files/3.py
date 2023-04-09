# Girilen Vize ve Final Notu Ortalaması Hesaplayan Python Örneği 
# Ve 3 yazılının ortalamasını hesaplayan kod

vize1 = input("Vize1 :  ")
vize2 = input("Vize2 :  ")
final = input("final :  ")

yazili1 = float(input("1.yazılı :  "))
yazili2 = float(input("2.yazılı :  "))
yazili3 = float(input("3.yazılı :  "))






Grade = ((float(vize1) + float(vize2)) * 0.3) + (float(final) * 0.4)

ortalama = (yazili1 + yazili2 + yazili3) / 3

print(f"Vize ortalaması :  {Grade}  ve  yazılı ortalaması : {ortalama} ")