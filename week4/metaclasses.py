from abc import ABCMeta, abstractmethod


class Clazz:
    pass


obj = Clazz()

print(type(obj))
print(type(Clazz))
print(type(type))

assert not issubclass(Clazz, type)


class Meta(type):
    def __init__(cls, name, bases, attrs):
        print('Initializing - {}'.format(name))

        if not hasattr(cls, 'registry'):
            cls.registry = {}
        else:
            cls.registry[name.lower()] = cls

        super().__init__(name, bases, attrs)


class Base(metaclass=Meta):
    pass


class A(Base):
    pass


class B(Base):
    pass


print(Base.registry)


class Sender(metaclass=ABCMeta):

    @abstractmethod
    def send(self):
        """Do something"""


class Child(Sender):

    def send(self):
        pass


Child()


class PythonWay:

    def send(self):
        raise NotImplementedError
