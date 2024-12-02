


def hello(user:str)->None:
    print(f'Witaj {user}!!')

def read_users(users:list)->None:
        for user in users[1:]:
            print(f'twój znajomy  {user['name']}, z miasta {user['city']} opublikował {user['posts']} postów')


def add_user(userlist:list)->None:
    new_name:str=input('proszę podać imię nowego znajomego')
    new_post:int=int(input('podaj liczbę postów'))
    new_city:str=input('podaj nazwę miasta')
    new_user: dict = {'name': new_name, 'posts': new_post, 'city': new_city}
    userlist.append(new_user)