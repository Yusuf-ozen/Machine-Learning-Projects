def cube():
    # result = []

    for i in range(5):

        # result.append(i**3)
        yield i ** 3


    # return result


generator = cube()

iterator = iter(generator)





print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
























