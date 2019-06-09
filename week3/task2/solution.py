import os.path
import csv
import re


def cw2us(x):
    return re.sub(r'(?<=[a-z])[A-Z]|(?<!^)[A-Z](?=[a-z])',
                  r"_\g<0>", x).lower()


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    @property
    def car_type(self):
        return cw2us(self.__class__.__name__)

    def get_photo_file_ext(self):
        _, ext = os.path.splitext(self.photo_file_name)
        return ext


class Car(CarBase):

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count

    @classmethod
    def parse(cls, raw_data):
        try:
            brand = raw_data['brand']
            photo_file_name = raw_data['photo_file_name']
            carrying = raw_data['carrying']
            passenger_seats_count = raw_data['passenger_seats_count']
        except KeyError as err:
            raise ValueError(
                'one or more of required arguments are missed', raw_data) from err
        else:
            return cls(brand, photo_file_name, float(carrying), int(passenger_seats_count))


class Truck(CarBase):

    def __init__(self, brand, photo_file_name, carrying, body_whl=None):
        super().__init__(brand, photo_file_name, carrying)
        self.body_length, self.body_width, self.body_height = Truck.split_body_wl(
            body_whl or '')

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height

    @classmethod
    def parse(cls, raw_data):
        try:
            brand = raw_data['brand']
            photo_file_name = raw_data['photo_file_name']
            carrying = raw_data['carrying']
        except KeyError as err:
            raise ValueError(
                'one or more of required arguments are missed', raw_data) from err
        else:
            try:
                body_whl = raw_data['body_whl']
            except KeyError:
                body_whl = None

            return cls(brand, photo_file_name, float(carrying), body_whl)

    @staticmethod
    def split_body_wl(body_wl: str):
        if not body_wl:
            return [0.0] * 3
        return [float(param) for param in body_wl.split('x')]


class SpecMachine(CarBase):

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

    @classmethod
    def parse(cls, raw_data):
        try:
            brand = raw_data['brand']
            photo_file_name = raw_data['photo_file_name']
            carrying = raw_data['carrying']
            extra = raw_data['extra']
        except KeyError as err:
            raise ValueError(
                'one or more of required arguments are missed', raw_data) from err
        else:
            return cls(brand, photo_file_name, float(carrying), extra)


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.DictReader(csv_fd, delimiter=';')

        for row in reader:
            if not 'car_type' in row:
                continue
            if row['car_type'] == 'car':
                try:
                    car = Car.parse(row)
                except ValueError as err:
                    print('Error while parsing: ', err)
                else:
                    car_list.append(car)
            elif row['car_type'] == 'truck':
                try:
                    truck = Truck.parse(row)
                except ValueError as err:
                    print('Error while parsing: ', err)
                else:
                    car_list.append(truck)
            elif row['car_type'] == 'spec_machine':
                try:
                    spec_machine = SpecMachine.parse(row)
                except ValueError as err:
                    print('Error while parsing: ', err)
                else:
                    car_list.append(spec_machine)

    return car_list

