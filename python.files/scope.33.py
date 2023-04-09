# global scope

x = 'global x'

def function():
    # local scope
    # x = 'local x'
    print(x)

function()
print(x)




#################################

# global
name = 'cınar'


def changeName(newName):
    global name
    # local
    name = newName
    print(name)

changeName('ada')

print(name)



###########################



name = 'global string'

def greeting():
    # name = 'cınar'


    def hello():
       # name = 'ada'
        print('hello '+ name)



    hello()

greeting()



#########################



x = 50

def test():
    global x                       # dışarıda yazdırdığın x bilgisini içeride kullanmak istersen "global" ifadesi kullanılır
    print(f'x : {x}')

    x = 100
    print(f'change x to {x}')

test()

print(x)





