class User:
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @property
    def name(self) :
        return self._name
    @name.setter
    def name(self, value) :
        self._name = value

    @property
    def password(self) :
        return self._password
    @password.setter
    def password(self, value) :
        self._password = value