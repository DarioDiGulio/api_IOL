from controllers.Token import *
from controllers.MiCuenta import *
from controllers.Titulos import *
from util.constants import COUNTRIES
from flask import Flask, request, abort

app = Flask(__name__)


@app.route('/getToken')
def getToken():
    try:
        return Token.getToken()
    except:
        abort(404, description="An error occurred")


@app.route('/micuenta')
def getMicuenta():
    try:
        return MiCuenta.getEstadoCuenta()
    except:
        abort(404, description="An error occurred")


@app.route('/portafolio/<pais>')
def getPortafolioArg(pais='argentina'):
    try:
        if pais in COUNTRIES:
            return MiCuenta.getPortafolio(str(pais))
        else:
            abort(400, description="Params not found")
    except:
        abort(404, description="An error occurred")


@app.route('/titulos')
def getTitulos():
    try:
        return Titulos().getTitulos()
    except:
        abort(404, description="An error occurred")


@app.route('/cotizaciones/<pais>')
def getCotizaciones(pais='argentina'):
    try:
        return Titulos().getCotizaciones(str(pais))
    except:
        abort(404, description="An error occurred")


if __name__ == '__main__':
    app.run(port=8282, debug=True)
