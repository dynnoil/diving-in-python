
num = 10
assert isinstance(num, int)


class Human:
    pass


class Robot:
    """Empty"""


print(Robot)
print(dir(Robot))


class Planet:
    """This class describes planet"""

    count = 0

    def __new__(cls, *args, **kwargs):
        False and print('__new__ called')
        obj = super().__new__(cls)
        return obj

    # magic method
    def __init__(self, name, population=None):
        False and print('__init__ called')
        self.name = name
        self.population = population or []
        Planet.count += 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return 'Platet {}'.format(self.name)


planet = Planet('Mercury')
print(planet)

planet.name = 'Earth'
del planet.name

try:
    print(planet.name)
except AttributeError as e:
    planet.name = 'Earth'


solar_system = []
planet_names = [
    'Mercury', 'Venus', 'Earth', 'Mars',
    'Jupiter', 'Saturn', 'Uranus', 'Neptune'
]

for name in planet_names:
    planet = Planet(name)
    solar_system.append(planet)

print(solar_system)

print('Planet object dict: {}'.format(planet.__dict__))
print('Planet class dict: {}'.format(Planet.__dict__))
