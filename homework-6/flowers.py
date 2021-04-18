from abc import ABC
import random


# Main flower class
class Flower(ABC):
    def __init__(self, flower_type: str, height: float, hydration: float):
        self._type = flower_type
        self._height = height
        self._hydration = hydration

    # Public methods - Getters
    def get_type(self):
        return self._type

    def get_height(self):
        return self._height

    def get_hydration(self):
        return self._hydration


class Red(Flower):
    def __init__(self):
        super(Red, self).__init__('Red', round(random.uniform(4, 6), 1), round(random.uniform(30, 60), 1))

    # Setters
    def set_hydration(self, weather):
        if weather.get_name() == 'Rain':
            self._hydration = min(self._hydration * 1.1, 100)
        elif weather.get_name() == 'Cloudy':
            self._hydration = min(self._hydration * 0.98, 100)
        elif weather.get_name() == 'Sunny':
            self._hydration = min(self._hydration * 0.95, 100)

    def set_height(self, weather):
        if self.get_hydration() > 85 or self.get_hydration() < 20:
            self._height = max(self._height - 0.5, 0)
        elif weather.get_name() == 'Sunny':
            self._height = min(self._height + 1, 10)

    # Conditional check
    def is_dead(self):
        if self._height < 2.5:
            return True
        else:
            return False


class Yellow(Flower):
    def __init__(self):
        super(Yellow, self).__init__('Yellow', round(random.uniform(6, 9), 1), round(random.uniform(20, 35), 1))

    # Setters
    def set_hydration(self, weather):
        if weather.get_name() == 'Rain':
            self._hydration = min(self._hydration * 1.2, 100)
        elif weather.get_name() == 'Cloudy' or weather.get_name() == 'Sunny':
            self._hydration = min(self._hydration * 0.95, 100)

    def set_height(self, weather):
        if 40 > self.get_hydration() > 10:
            self._height = min(self._height + 1.5, 20)
        else:
            self._height = max(self._height - 1, 0)

    # Conditional check
    def is_dead(self):
        if self._height < 4:
            return True
        else:
            return False


class Blue(Flower):
    def __init__(self):
        super(Blue, self).__init__('Blue', round(random.uniform(6, 7.5), 1), round(random.uniform(40, 70), 1))

    # Setters
    def set_hydration(self, weather):
        if weather.get_name() == 'Rain':
            self._hydration = min(self._hydration * 1.1, 100)
        elif weather.get_name() == 'Sunny':
            self._hydration = min(self._hydration * 0.95, 100)

    def set_height(self, weather):
        if weather.get_name() == 'Sunny':
            self._height = max(self._height - 1, 0)
        elif weather.get_name() == 'Rain':
            self._height = min(self._height + 0.5, 12)
        elif self._hydration > 35 and weather.get_name() == 'Cloudy':
            self._height = min(self._height + 0.5, 12)

    # Conditional check
    def is_dead(self):
        if self._height < 1 or self._hydration < 15:
            return True
        else:
            return False
