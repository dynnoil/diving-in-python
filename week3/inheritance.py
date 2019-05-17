import json


class Pet:

    def __init__(self, name):
        self.name = name


class Dog(Pet):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def say(self):
        return f'Woof! I am {self.name} of {self.breed}'


polly = Dog('Polly', 'Doberman')
assert polly.say() == 'Woof! I am Polly of Doberman'

assert isinstance(polly, object)
assert isinstance(polly, Pet)
assert isinstance(polly, Dog)


class ExportJSON:
    def to_json(self):
        return json.dumps({
            "name": self.name,
            "breed": self.breed
        })


class ExtDog(Dog, ExportJSON):

    def __init__(self, name, breed=None):
        super().__init__(name, breed)


class WoolenDog(Dog, ExportJSON):

    def __init__(self, name, breed=None):
        super(Dog, self).__init__(name)
        self.breed = 'Woolen dog of {0}'.format(breed)


dog = ExtDog('Belka', breed='Strelka')
print(dog.to_json())

woolen = WoolenDog('Жучка', 'Такса')
print(woolen.breed)
