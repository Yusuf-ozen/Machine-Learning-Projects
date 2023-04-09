import requests
import json


api_url = "http://api.exchangeratesapi.io/v1/latest?access_key=f3cdceaeff7e2033240dc7208107311d&format=1"



bozulan_doviz = input("Bozulan doviz turu : ")

alinan_doviz = input("Alinan doviz turu : ")

miktar = int(input(f"Ne kadar {bozulan_doviz} bozdurma istiyorsunuz : "))

result = requests.get(api_url + bozulan_doviz)
result = json.loads(result.text)


print("1 {0} = {1} {2}".format(bozulan_doviz, result["rates"][alinan_doviz], alinan_doviz))
print("{0} {1} = {2} {3}".format(miktar, bozulan_doviz, miktar * result["rates"][alinan_doviz], alinan_doviz))



# print(result)






