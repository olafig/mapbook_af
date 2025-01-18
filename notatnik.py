

users: list = [
    {'name': 'Dominik', 'posts': 1, 'city': 'Poznań'},
    {'name': 'Julia', 'posts': 1, 'city': 'Zamość'},
    {'name': 'Patryk', 'posts': 1, 'city': 'Łódź'},
    {'name': 'Patrycja', 'posts': 1, 'city': 'Zielona_Góra'},
]

class User:
    def __init__(self,imie,nazwisko,posts,lokalizacja):
        self.name = imie
        self.nazwisko = nazwisko
        self.posts = posts
        self.lokalizacja = lokalizacja


user_Marek=User('Marek','aaa', '23', 'aaa')


print(user_Marek.name)
