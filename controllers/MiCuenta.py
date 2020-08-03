import requests
import json
from util.constants import URL_API
from controllers.Token import *


class MiCuenta(object):

    @staticmethod
    def getEstadoCuenta():
        headers = {
            'Authorization': f'Bearer {Token.getToken()}'
        }

        response = requests.get(
            f'{URL_API}/estadocuenta', headers=headers)
        return json.loads(response.text)

    @staticmethod
    def getPortafolio(pais):
        headers = {
            'Authorization': f'Bearer {Token.getToken()}'
        }

        response = requests.get(
            f'{URL_API}/portafolio/{pais}', headers=headers)
        return json.loads(response.text)

    @staticmethod
    def getOperacion(number):
        headers = {
            'Authorization': f'Bearer {Token.getToken()}'
        }

        response = requests.get(
            f'{URL_API}/operaciones/{number}', headers=headers)
        return json.loads(response.text)
