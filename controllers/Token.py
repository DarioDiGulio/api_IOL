import requests
from flask import Response
from util.constants import GRANT_TYPE, URL_TOKEN
from util.private_constants import USER_A, USER_B, USER_C, PASS_A, PASS_B, PASS_C


class Token(object):

    @staticmethod
    def get_token():
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'username': USER_C,
            'password': PASS_C,
            'grant_type': GRANT_TYPE
        }
        res = requests.post(URL_TOKEN, headers=headers, data=body)

        return res.json()['access_token']

    @staticmethod
    def check_token(user, password):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'username': user,
            'password': password,
            'grant_type': GRANT_TYPE
        }
        res = requests.post(URL_TOKEN, headers=headers, data=body)
        print(res.json()['access_token'])
        return res.json()['acces_token']
