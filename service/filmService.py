from service.dataService import filmsDB
import os

def show_films(filmList = filmsDB, select = False):
    os.system('cls')
    for i, film in enumerate(filmList):
        print(f"{f'{i + 1} -' if select else ''}{film.name}")
    print("\n")

def available_films():
    return list(filter(lambda film: film.status, filmsDB))

def show_available():
    show_films(available_films())

def select_film(film_list):
    exit = False
    select_num = -1
    while(not exit):
        print("Choose a film to rent:")
        show_films(film_list, True)
       
        try: 
            select_num = int(input())
            
        except: 
            print("It must be a number")
            select_num = -1

        if( 0 < select_num and select_num <= len(film_list)):
            exit = True
    selected_film = film_list[select_num - 1].name
    return selected_film

def select_available():
    return select_film(available_films())

def rent_film():
    selected_film = select_available()
    change_status(selected_film)
    return selected_film

def change_status(name):
    for film in filmsDB:
        if(film.name == name):
            film.status = not film.status