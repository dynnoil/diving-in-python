
class Descriptor:

    def __get__(self, obj, obj_type):
        print('get')

    def __set__(self, obj, value):
        print('set')

    def __delete__(self, obj):
        print('delete')


class Clazz:
    attr = Descriptor()


instance = Clazz()
instance.attr
instance.attr = 1
del instance.attr


class ImportantValue:

    def __init__(self, amount=None):
        self.amount = amount or 0

    def __get__(self, obj, obj_type):
        return self.amount

    def __set__(self, obj, value):
        with open('week4/log.txt', 'w') as f:
            f.write(str(value))

        self.amount = value


class Account:
    amount = ImportantValue()


bobs_amount = Account()
bobs_amount.amount = 150

with open('week4/log.txt', 'r') as f:
    result = f.read()
    assert int(result) == 150


class SimpleClazz:

    # method is Descriptor
    def method(self):
        pass


simpleClazz = SimpleClazz()

print(simpleClazz.method)  # bound method
print(SimpleClazz.method)  # unbound method


class MyProperty:
    def __init__(self, getter):
        self.getter = getter

    def __get__(self, obj, obj_type=None):
        if obj is None:
            return self

        return self.getter(obj)


class User:

    def __init__(self, first_name, last_name, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    @property  # property is descriptor
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    @MyProperty
    def name(self):
        sex_lowercased = self.sex.lower()

        if sex_lowercased == 'male':
            return f'Mr. {self.last_name}'

        if sex_lowercased == 'female':
            return f'Ms. {self.last_name}'

        return self.last_name


amy = User('Amy', 'Jones', 'Female')

print(amy.full_name)
print(User.full_name)
print(amy.name)


class FixedAttrClazz:

    __slots__ = ['anakin']

    def __init__(self):
        self.anakin = 'the choosen one'


obj = FixedAttrClazz()

try:
    obj.another_attr = 10
except AttributeError:
    print('Its Ok. Class now has fixed attributes set')
