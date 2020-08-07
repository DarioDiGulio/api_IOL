from controllers.MiCuenta import *
from flask import Flask, request, abort
from util.constants import COUNTRIES
from app import app
from flask_cors import CORS, cross_origin


@app.route('/micuenta')
@cross_origin()
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
