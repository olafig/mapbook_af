users:list=[
    {'name':'Ola','posts':1,'city':'Warszawa'},
    {'name':'Dominik','posts':3,'city':'Poznań'},
    {'name':'Szymon z wąsem','posts':5,'city':'Toruń'},
    {'name':'Szymon','posts':7,'city':'Białogard'},
    {'name':'Patryk','posts':9,'city':'Łódź'},
    {'name':'Patrycja','posts':11,'city':'Mińsk'},
    {'name':'Ola','posts':13,'city':'Radom'},
    {'name':'Julia','posts':15,'city':'Zamość'},
    {'name':'Karolina','posts':17,'city':'Mława'},
    {'name':'Amelia','posts':19,'city':'Toruń'},

]
#TODO please update user list

print(f'Witaj {users[0]['name'] }!!')
for user in users[1:]:
    print(f'twój znajomy  {user['name']}, z miasta {user['city']} opublikował {user['posts']} postów')
# for idx,_ in enumerate(users[1:]):
#     print(f'twój znajomy {users[idx]}, opublikował {postow[idx]} postów')
