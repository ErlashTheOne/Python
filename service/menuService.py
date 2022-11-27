
from service.userService import login, register
from service.filmService import show_available
from service.bookingService import rent, show_bookings
import os

def select_from_menu_between_range(start, finish, menu):
    menu_range = range(start, finish + 1)
    user_num = -1

    while( user_num not in menu_range ):
        print(menu)

        try: 
            user_num = int(input())

        except:
            print("Only numbers from abobe are valid")
            user_num = -1

        if( user_num not in menu_range ):
            print("Only numbers from abobe are valid")
        
    return user_num

def print_start_menu():
    os.system('cls')
    menu = """
    1 - Login
    2 - Register
    3 - Exit"""
    return select_from_menu_between_range(1, 3, menu)  

def print_user_menu():
    menu = "1 - Show available films\n2 - Rent a film\n3 - Your bookings\n4 - Log out"
    return select_from_menu_between_range(1, 4, menu)

def start_menu():
    global user
    exit = False

    print("Welcome!")

    while (not exit):
        user_start_selecction = (print_start_menu())

        match user_start_selecction:
            case 1:
                user = login()
            case 2:
                user = register()
            case 3:
                exit = True
            case _:
                print("Something go wrong")

        if(not exit):
            os.system('cls')
            exit_user = False
            while(not  exit_user):
                user_user_selecction = (print_user_menu())

                match user_user_selecction:
                    case 1:
                        show_available()
                    case 2:
                        rent(user)
                    case 3:
                        show_bookings(user)
                    case 4:
                        exit_user = True
                    case _:
                        print("Something go wrong")
            
    os.system('cls')
    print("See you soon")