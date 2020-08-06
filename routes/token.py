from app import app
from controllers.Token import *


@app.route('/getToken')
def getToken():
    try:
        return Token.getToken()
    except:
        abort(404, description="An error occurred")
