from flask import Flask, request, abort

app = Flask(__name__)

from routes.micuenta import *
from routes.token import *
from routes.titulos import *

if __name__ == '__main__':
    app.run(port=8282, debug=True)
