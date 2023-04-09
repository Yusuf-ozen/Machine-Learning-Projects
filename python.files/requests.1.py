import requests
import json



result = requests.get("https://jsonplaceholder.typicode.com/todos")

result = json.loads(result.text)



for i in result:
    if(i["userId"] == 7):

        print(i["title"])      # her gelen i bilgisinin title nı alır.



print(result[0]["title"])
print(result[0])

print(type(result))

