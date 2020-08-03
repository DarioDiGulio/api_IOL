import requests
from util.constants import USUARIO, CONTRASÑEA, GRANT_TYPE, URL_TOKEN


class Token(object):

    @staticmethod
    def getToken():
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'username': USUARIO,
            'password': CONTRASÑEA,
            'grant_type': GRANT_TYPE
        }
        response = requests.post(
            f'{URL_TOKEN}', headers=headers, data=body)
        return response.json()['access_token']
