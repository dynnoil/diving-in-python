from datetime import date


class Human:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Human {}'.format(self.name)

    def _say(self, text):
        print(text)

    def say_name(self):
        self._say(f'Hello, I am {self.name}')

    def say_how_old(self):
        self._say(f'I am {self.age} years old')


class Planet:

    def __init__(self, name, population=None):
        self.name = name
        self.population = population or []

    def add_human(self, human):
        self.population.append(human)


mars = Planet('Mars')
bob = Human('Bob')
mars.add_human(bob)

print(mars.population)


oleg = Human('Oleg', 20)
oleg.say_name()
oleg.say_how_old()


def extract_desc(user_string):
    return 'some event'


def extract_date(user_string):
    return date(2019, 6, 14)


class Event:

    def __init__(self, desc, user_date):
        self.desc = desc
        self.user_date = user_date

    def __str__(self):
        return f'Event "{self.desc}" at {self.user_date}'

    @classmethod
    def from_string(cls, user_input):
        desc = extract_desc(user_input)
        user_date = extract_date(user_input)
        return cls(desc, user_date)


event = Event.from_string('some event')
event.from_string('dsfsdf')
print(event)

assert dict.fromkeys('12') == {'1': None, '2': None}


class Person:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    @staticmethod
    def is_age_valid(age):
        return 0 < age < 150


assert Person.is_age_valid(151) == False

vlad = Person('Vlad')
assert not vlad.is_age_valid(200)


class Robot:

    def __init__(self, power, robot_class=None):
        self._power = power
        self._robot_class = robot_class

    power = property()

    @power.setter
    def power(self, value):
        if value < 0:
            self._power = 0
        else:
            self._power = value

    @power.getter
    def power(self):
        return self._power

    @power.deleter
    def power(self):
        del self._power

    @property
    def robot_class(self):
        return self._robot_class


wall_e = Robot(100)
wall_e.power = -100
assert wall_e.power == 0

del wall_e.power

try:
    wall_e.power
except AttributeError as error:
    print(error)

d = {wall_e: 'Robot'}
assert d[wall_e] == 'Robot'
