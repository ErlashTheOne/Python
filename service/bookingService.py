from model.booking import Booking
from service.dataService import bookingsDB
from service.filmService import rent_film
import os

def rent(user):
    film = rent_film()
    booking = Booking(user, film)
    create_boking(booking)
    os.system('cls')
    print(f"you have rented {film} movie")

def show_bookings(user):
    os.system('cls')
    userBookings = list(filter(lambda booking: booking.user == user, bookingsDB))

    if(len(userBookings) > 0):
        for booking in userBookings:
            print(f"{booking.film} {booking.date}")
    else: 
        print("There are no bookings yet")

    print("\n")

def create_boking(booking):
    bookingsDB.append(booking)