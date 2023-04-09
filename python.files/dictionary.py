# key - value

# 41 => Kocaeli  49 => Muş

# cities = ["Kocaeli", "Muş"]
# plates = [41, 49]

# print(plates[cities.index("Kocaeli")])    # Burada 41 i Kocaeli' ye atanır.
# print(plates[cities.index("Muş")])        # Burada 49 u Muş' a atanır.

# print(cities[plates.index(49)])           # Burada da tam tersi olur.

# # print(plates["Kocaeli"])   =>  41

# plates = {"Kocaeli" : 41, "Muş" : 49}

# print(plates["Kocaeli"])             # Kocaelinin plakasını bulur.
# print(plates["Muş"])                 # Muş un plakasını bulur.

# plates["Ankara"] = 6                 # Ankara yı 6 olarak alır ve listeye atar.
# plates["Ankara"] = "new value" 


# print(plates)

users = {

    "SadıkTuran" : {
        "Age" : 36,
        "Roles" : ["User"],
        "Mail" : "sadıkturan@gmail.com",
        "Address" : "Kocaeli",
        "Phone" : "5674893843"
    },

    "ÇınarTuran" : {
        "Age" : 2,
        "Roles" : ["Admin", "User"],
        "Mail" : "cınarturan@gmail.com",
        "Address" : "Maraş",
        "Phone" : "2323233843"
    }
}



print(users["SadıkTuran"]["Age"])           # Burada SadıkTuran ın yaş bilgisine ulaşılır. 
print(users["SadıkTuran"]["Mail"]) 
print(users["SadıkTuran"]["Address"]) 
print(users["SadıkTuran"]["Roles"])
print(users["ÇınarTuran"]["Roles"][0])     # Burada Çınarturan ın Roles kısmındaki ilk şeyi yazdırır. 






