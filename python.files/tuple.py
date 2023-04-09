list = [1, 2, 3]

tuple = (1, "iki", 3)    # parantez kullanmasan da olur.

# print(type(list))
# print(type(tuple))

# print(list[2])
# print(list[2])

# print(len(list))
# print(len(tuple))

list = ["Ali", "Veli"]
tuple = ["Ayşe", "Damla", "Ayşe", "Ayşe"]
names = ["Demet", "Emel", "Doğa"] + tuple


list[0] = "Ahmet"
tuple[0] = "Fatma" 

print(tuple.count("Ayşe"))
print(tuple.index("Ayşe"))

# print(list)
# print(tuple)


print(names)

tuple.clear()
print(tuple)
