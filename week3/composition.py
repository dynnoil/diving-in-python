import json


class PetExport:
    def export(self, dog):
        raise NotImplementedError


class ExportJson(PetExport):
    def export(self, dog):
        return json.dumps({
            "name": dog.name,
            "breed": dog.breed
        })


class ExportXml(PetExport):
    def export(self, dog):
        return """
        <?xml version="1.0" encoding="utf-8"?>
        <dog>
            <name>{0}</name>
            <breed>{1}</breed>
        </dog>
        """.format(dog.name, dog.breed)


class Pet:
    def __init__(self, name):
        self.name = name


class Dog(Pet):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed


class ExDog(Dog):
    def __init__(self, name, breed=None, exporter=None):
        super(ExDog, self).__init__(name, breed)
        self._exporter = exporter or ExportJson()
        if not isinstance(self._exporter, PetExport):
            raise ValueError("bad exporter", self._exporter)

    def export(self):
        return self._exporter.export(self)


sharik = ExDog('Sharik', 'Dvornayga', exporter=ExportXml())
print(sharik.export())

tuzik = ExDog('Tuzik', 'Mops')
print(tuzik.export())
