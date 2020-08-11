import requests
import json
from json import dumps
from util.constants import URL_API
from controllers.Token import *
from flask import Flask, make_response


class MiCuenta(object):

    def __init__(self):
        self.headers = {'Authorization': f'Bearer {Token.get_token()}'}

    def get_estado_cuenta(self):

        response = requests.get(
            f'{URL_API}/estadocuenta', headers=self.headers)
        return json.loads(response.text)

    def get_portafolio(self, pais):

        response = requests.get(
            f'{URL_API}/portafolio/{pais}', headers=self.headers)
        return json.loads(response.text)

    def get_operaciones(self, state, country):

        response = requests.get(
            f'{URL_API}/operaciones?filtro.estado={state}&filtro.pais={country}', headers=self.headers)
        return make_response(dumps(response.json()))
