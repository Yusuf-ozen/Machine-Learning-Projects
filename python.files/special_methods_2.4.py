list = [1, 2, 3]
# my_string = 'Yusuf Ozen'

# print(len(list))
# print(len(my_string))
# print(type(list))
# print(type(my_string))




class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print('Movie objesi oluşturuldu.')


    def __str__(self):
        return f'{self.title} by {self.director}'


    def __len__(self):
        return self.duration


    def __del__(self):
        print('Movie Deleted')


m = Movie('film adı', 'yönetmen adı', 120)

# print(str(list))          # Burada str yazmasan da olur.
# print(str(m))        

# print(len(list))
# print(len(m))


del m


print(m)
