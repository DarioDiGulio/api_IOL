from controllers.MiCuenta import *
from flask import abort
from util.constants import COUNTRIES, STATE
from app import app
from flask_cors import cross_origin


@app.route('/micuenta')
@cross_origin()
def get_micuenta():
    try:
        return MiCuenta().get_estado_cuenta()
    except:
        abort(404, description="An error occurred")


@app.route('/portafolio/<pais>')
@cross_origin()
def get_portafolio_arg(pais='argentina'):
    try:
        if pais in COUNTRIES:
            return MiCuenta().get_portafolio(str(pais))
        else:
            abort(400, description="Params not found")
    except:
        abort(404, description="An error occurred")


@app.route('/operaciones/<state>/<country>')
@cross_origin()
def getOperaciones(state, country):
    try:
        if state in STATE and country in COUNTRIES:
            return MiCuenta().get_operaciones(str(state), str(country))
        else:
            abort(400, description="Params not found")
    except:
        abort(404, description='An error ocurred')
