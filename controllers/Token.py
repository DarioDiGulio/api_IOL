import requests
from util.constants import GRANT_TYPE, URL_TOKEN
from util.private_constants import USER, PASS


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
        response = requests.post(URL_TOKEN, headers=headers, data=body)
        return response.json()['access_token']
