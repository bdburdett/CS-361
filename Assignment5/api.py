from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import socket
import requests


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


    def get_external_ip(self):
        """
        Users likely using DHCP and local private address could cause issues for the location request.
        This function will return a user's externally facing public ip assigned in DHCP.
        """
        #API for external ip lookup: https://www.ipify.org/
        return requests.get('https://api.ipify.org').text


    def get_ip_loc(self):
        HOST = '127.0.0.2'                                      #Adjust as necessary; match with ip_locator_serv
        PORT = 18777                                            #Adjust as necessary; match with ip_locator_serv

        #Setup socket to connect to local server
        user_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #Use get_external_ip to get the user's current DHCP; if not using DHCP should still work as expected
        ip_request = self.get_external_ip()

        try:
            user_socket.connect((HOST, PORT))
            user_socket.sendall(ip_request.encode())
            ip_location = user_socket.recv(1024).decode()

            return ip_location

        except Exception as e:
            print("Cannot connect to the server:", e)