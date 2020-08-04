import requests
from util.constants import USER, PASS, GRANT_TYPE, URL_TOKEN


class Token(object):

    @staticmethod
    def getToken():
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        body = {
            'username': USER,
            'password': PASS,
            'grant_type': GRANT_TYPE
        }
        response = requests.post(
            f'{URL_TOKEN}', headers=headers, data=body)
        return response.json()['access_token']
