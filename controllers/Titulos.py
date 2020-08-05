import requests
from controllers.Token import *
from util.constants import URL_API
import json


class Titulos(object):

    def __init__(self):
        self.headers = {'Authorization': f'Bearer {Token.getToken()}'}


    def getTitulos(self, titulo):
        response = requests.get(f'{URL_API}/Titulos/FCI', headers=self.headers)
        return response.json()[titulo]


    def getCotizaciones(self, pais, titulo):
        response = requests.get(f'{URL_API}/{pais}/Titulos/Cotizacion/Instrumentos', headers=self.headers)
        return response.json()[titulo]
