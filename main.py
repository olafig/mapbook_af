from os import remove

from mapbook.users import users
from mapbook.crud import hello, read_users, add_user,remove_user, update_user

def main():
    hello(users[0]['name'])
    while True:
        print('======MENU======')
        print('0. wyjście z programu')
        print('1. dodaj znajomego')
        print('2. wczytaj znajomych')
        print('3. aktualizuj znajomego')
        print('4. usuń znajomego')
        print('5. generuj mapę z lokalizacją znajomego')
        print('6. generuj mapę z lokalizacją wszystkich znajomych')

        menu_option: str = input('Użytkowniku wybierz opcję menu: ')
        print(f'użytkownik wybrał {menu_option}')
        if menu_option == '0':
            break
        if menu_option == '1':
            add_user(users)
        if menu_option == '2':
            read_users(users)
        if menu_option == '3':
            update_user(users)
        if menu_option == '4':
            remove_user(users)
        if menu_option == '5':
            pass
        if menu_option == '6':
            pass

if __name__ == '__main__':
    main()


