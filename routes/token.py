from app import app
from controllers.Token import *
from flask import request, abort
from flask_cors import CORS, cross_origin


@app.route('/getToken')
@cross_origin()
def getToken():
    try:
        return Token.getToken()
    except:
        abort(404, description="An error occurred")

@app.route('/checkToken/<user>/<password>')
@cross_origin()
def checkToken(user, password):
    try:
        return Token.checkToken(user, password)
    except:
        abort(404, description="An error occurred")
