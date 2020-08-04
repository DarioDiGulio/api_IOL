import requests
from controllers.Token import *
from util.constants import URL_API


class Titulos(object):

    def __init__(self):
        self.headers = {'Authorization': f'Bearer {Token.getToken()}'}

    def getTitulos(self):
        response = requests.get(f'{URL_API}/Titulos/FCI', headers=self.headers)
        return json.loads(response.text)

    def getCotizaciones(self, pais):
        response = requests.get(f'{URL_API}/{pais}/Titulos/Cotizacion/Instrumentos', headers=self.headers)
        return json.loads(response.text)
