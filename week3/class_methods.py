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
print(event)

assert dict.fromkeys('12') == {'1': None, '2': None}
