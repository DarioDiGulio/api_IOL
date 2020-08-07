import requests
from flask import Response
from util.constants import GRANT_TYPE, URL_TOKEN
from util.private_constants import USER_A, USER_B, PASS_A, PASS_B

class Token(object):

    @staticmethod
    def getToken():
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'username': USER_A,
            'password': PASS_A,
            'grant_type': GRANT_TYPE
        }
        res = requests.post(URL_TOKEN, headers=headers, data=body)
        
        return res.json()['access_token']

    @staticmethod
    def checkToken(user, password):
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