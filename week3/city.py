import requests
from pprint import pprint


class YandexWheatherForecast:

    def __init__(self, api_key):
        self._api_key = api_key

    def get(self, lat, lon):
        url = f'http://api.weather.yandex.ru/v1/informers?lat={lat}&lon={lon}&lang=en_US'
        data = requests.get(
            url, headers={'X-Yandex-API-Key': self._api_key}).json()
        return data


class CityInfo:

    def __init__(self, city, wheather_forecast=None):
        self.city = city
        self._wheather_forecast = wheather_forecast or YandexWheatherForecast('API_KEY')

    def weather_forecast(self):
        return self._wheather_forecast.get(0, 0)


def _main():
    city_info = CityInfo('Moscow')
    forecast = city_info.weather_forecast()
    pprint(forecast)


if __name__ == '__main__':
    _main()
