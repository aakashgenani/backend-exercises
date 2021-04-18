# Main weather class
class Weather:
    def __init__(self, name: str):
        self._name = name

    def get_name(self):
        return self._name


class Sunny(Weather):
    def __init__(self):
        super(Sunny, self).__init__('Sunny')


class Cloudy(Weather):
    def __init__(self):
        super(Cloudy, self).__init__('Cloudy')


class Rain(Weather):
    def __init__(self):
        super(Rain, self).__init__('Rain')
