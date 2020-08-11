from app import app
from controllers.Token import *
from flask import abort
from flask_cors import cross_origin


@app.route('/get_token')
@cross_origin()
def get_token():
    try:
        return Token.get_token()
    except:
        abort(404, description="An error occurred")


@app.route('/check_token/<user>/<password>')
@cross_origin()
def check_token(user, password):
    try:
        return Token.check_token(user, password)
    except:
        abort(404, description="An error occurred")
