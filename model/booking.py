from service.dataService import bookingsDB
from datetime import date

class Booking:
    def __init__(self, user, film, date=date.today()):
        self._user = user
        self._film = film
        self._date = date

    @property
    def user(self) :
        return self._user
    @user.setter
    def user(self, value) :
        self._user = value

    @property
    def film(self) :
        return self._film
    @film.setter
    def film(self, value) :
        self._film = value

    @property
    def date(self) :
        return self._date
    @date.setter
    def date(self, value) :
        self._date = value