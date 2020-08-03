from controllers.Token import *
from controllers.MiCuenta import *
from flask import Flask, request

app = Flask(__name__)


@app.route('/getToken')
def getToken():
    return Token.getToken()


@app.route('/micuenta')
def getMicuenta():
    return MiCuenta.getEstadoCuenta()


@app.route('/portafolio/arg')
def getPortafolioArg():
    return MiCuenta.getPortafolio('argentina')


@app.route('/portafolio/usa')
def getPortafolioUsa():
    return MiCuenta.getPortafolio('estados_Unidos')


if __name__ == '__main__':
    app.run(port=8282, debug=True)
