# Value-Types  =>  string, number        Burada yaptığın değişiklik öbürünü etkilemez.

x = 5
y = 25

x = y

y = 10

# print(x)
# print(y)

#references - Types  => list      Burada yaptığın değişiklik öbürünü de etkiler.

a = ["Apple", "Banana"]
b = ["Apple", "Banana"]

a = b

b[0] = "Orange"

print(a, b)
