userName = "Yusuf"
password = "123"

a = input("Please enter your username :  ")
b = input("Please enter your password :  ")

# isLoggedin =(userName == a) and (password == b)


# isLoggedin = True


if  (userName == a) :                       # if den sonra gelen satırda tab tuşuna basman lazım. Ve iki nokta şart.
    # you can write 'if 2 == 2'   or 'if True'.
    if (password == b):
        print("Welcome")

    else:
        print("Wrong password")
else:
        print("Wrong username")