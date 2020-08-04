from controllers.Token import *
from controllers.MiCuenta import *
from controllers.Titulos import *
from util.constants import COUNTRIES
from flask import Flask, request

app = Flask(__name__)


@app.route('/getToken')
def getToken():
    return Token.getToken()


@app.route('/micuenta')
def getMicuenta():
    return MiCuenta.getEstadoCuenta()

@untested
@app.route('/portafolio/<pais>')
def getPortafolioArg(pais='argentina'):
    if pais in COUNTRIES:
        return MiCuenta.getPortafolio(str(pais))
    else:
        abort(404, description="Params not found")

@untested
@app.route('/titulos')
def getTitulos():
    titulos = Titulos()
    return titulos.getTitulos()

@untested
@app.route('/cotizaciones/<pais>')
def getCotizaciones(pais='argentina'):
    if pais in COUNTRIES:
        titulos = Titulos()
        return titulos.getCotizaciones(pais)
    else:
        abort(404, description="Params not found")


if __name__ == '__main__':
    app.run(port=8282, debug=True)
