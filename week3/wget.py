import sys
import requests

if __name__ == '__main__':

    url = sys.argv[1]

    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
    except requests.Timeout:
        print('timeout')
    except requests.HTTPError as err:
        code = err.response.status_code
        print('error, url {0}, code {1}'.format(url, code))
    except requests.RequestException:
        print('get error, url ', url)
    else:
        print(response.content)
