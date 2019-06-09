
class FileReader:

    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename) as file:
                return file.read()
        except IOError as error:
            print(error)
            return ''
