from controllers.Titulos import *
from flask import Flask, request, abort
from util.constants import COUNTRIES, MARKETS, SYMBOLS
from app import app


@app.route('/titulos')
def get_titulos():
    try:
        return Titulos().get_titulos()
    except:
        abort(404, description="An error occurred")


@app.route('/cotizaciones/<pais>')
def get_cotizaciones(pais='argentina'):
    try:
        if pais in COUNTRIES:
            return Titulos().get_cotizaciones(str(pais))
        else:
            abort(400, description="Params not found")
    except:
        abort(404, description="An error occurred")


@app.route('/seriehistorica/<mercado>/<simbolo>/<desde>/<hasta>')
@app.route('/seriehistorica/<mercado>/<simbolo>')
@app.route('/seriehistorica')
def get_serie_historica(mercado='bcBA', simbolo='ALUA', desde='2010-01-01', hasta='2020-01-01'):
    try:
        if mercado in MARKETS and simbolo in SYMBOLS:
            return Titulos().get_serie_historica(mercado, simbolo, desde, hasta)
        else:
            abort(400, description="Params not found")
    except:
        abort(404, description="An error occurred")
