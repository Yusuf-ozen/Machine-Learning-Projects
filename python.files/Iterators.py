# # liste = [1, 2, 3, 4, 


# iterator = iter(liste)

# print(iterator)


# print(next(iterator))         # next sıra sıra elemanları getirtir.
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))



# iterator = iter(liste)

# # while Tru
# #     tr
# #         element = next(iterato
# #         print(elemen

# #     except StopIteratio
# #         bre



class myNumbers:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop


    def __iter__(self):
        return self


    def __next__(self):
        if self.start <= self.stop:
            x = self.start
            self.start += 1
            return x

        else:
            raise StopIteration



list = myNumbers(10, 20)



myiter = iter(list)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


while True:
    try:
        element = next(myiter)
        print(element)

    except StopIteration:
        break




# for x in list:
#     print(x)



