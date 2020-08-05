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


@app.route('/titulos/<titulo>')
def getTitulos(titulo=0):
    if int(titulo) < 14:
        titulos = Titulos().getTitulos(int(titulo))
    else: 
        abort(400, description="Params not found")
    return titulos


@app.route('/cotizaciones/<pais>/<titulo>')
def getCotizaciones(pais='argentina', titulo=0):
    if pais in COUNTRIES and int(titulo) < 5:
        return Titulos().getCotizaciones(str(pais),int(titulo))
    else:
        abort(400, description="Params not found")


if __name__ == '__main__':
    app.run(port=8282, debug=True)
