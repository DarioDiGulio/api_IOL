from controllers.Token import *
from controllers.MiCuenta import *
from controllers.Titulos import *
from util.constants import COUNTRIES
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/getToken')
def getToken():
    return Token.getToken()


@app.route('/micuenta')
def getMicuenta():
    return MiCuenta.getEstadoCuenta()


@app.route('/portafolio/<pais>')
def getPortafolioArg(pais='argentina'):
    if pais in COUNTRIES:
        return MiCuenta.getPortafolio(str(pais))
    else:
        abort(400, description="Params not found")


@app.route('/titulos')
def getTitulos():
    return Titulos().getTitulos()


@app.route('/cotizaciones/<pais>')
def getCotizaciones(pais='argentina'):
    return Titulos().getCotizaciones(str(pais))


if __name__ == '__main__':
    app.run(port=8282, debug=True)
