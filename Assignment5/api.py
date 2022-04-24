from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

class Crypto:
    def get_top_20(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start':'1',
            'limit':'20',
            'convert':'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '1f1ebb94-7047-4fbc-839f-28783b871f58',
        }
        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data['data']

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)


    def get_top_1(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start':'1',
            'limit':'1',
            'convert':'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '1f1ebb94-7047-4fbc-839f-28783b871f58',
        }
        session = Session()
        session.headers.update(headers)

        try:
            response = session.get(url, params=parameters)
            data = json.loads(response.text)
            return data['data']

        except (ConnectionError, Timeout, TooManyRedirects) as e:
            print(e)
