# x = 5
# y = 10
# z = 20

# x, y, z = 5, 10, 20
# print(x, y, z)

# x, y = y, x

# x = x + 5
# x += 5
# x -= 2
# x *= 4
# x /= 3
# x %= 7
# x //= 2
# y **= 4

# print(x, y, z)



values = 1, 2, 3, 4

print(values)

print(type(values))

x, y, *z = values     # z ye kalanları atar.

print(x, y, z[1])