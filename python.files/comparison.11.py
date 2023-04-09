# username , password  =>  database

# "SadıkTuran" , "123456"

a, b, c, d = 5, 5, 10, 4

result = (a == b)           #true     eğer a b'ye eşitse
result = (a == c)           #false
result = (a !=b)             # a b' ye eşit değil ise true
result = (a > b)             # a b'den büyükse true
result = (a <= b)            # a b'den küçük veya eşitse true
result = (True == 1)         # True 1'e eşit olduğu için sonuç True.
result = (False == 0)        # False 0'a eşit olduğu için sonuç True.
result = True + False + 40   # Sonuç eşittir 41.



password = "123456"
username = "SadıkTuran"

x = input("Please enter password : ")
y = input("Please enter username : ")

result = (x == password)
res = (y == username)

print(result)
print(res)
