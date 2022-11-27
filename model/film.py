class Film:
    def __init__(self, name, status):
        self._name = name
        self._status = status

    @property
    def name(self) :
        return self._name
    @name.setter
    def name(self, value) :
        self._name = value

    @property
    def status(self) :
        return self._status
    @status.setter
    def status(self, value) :
        self._status = value