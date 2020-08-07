from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

from routes.micuenta import *
from routes.token import *
from routes.titulos import *

if __name__ == '__main__':
    app.run(port=8282, debug=True)
