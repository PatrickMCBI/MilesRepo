from flask import Flask
#from config import HOST
from flask_cors import CORS

from flask_sqlalchemy import get_debug_queries

# from version import *
from routes.usersroute import usersapi



app = Flask(__name__)
api_version = '/api/v1.0'
CORS(app)
"""
Blueprint is structuring the api's
"""
# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app

app.register_blueprint(usersapi, url_prefix=api_version)


if __name__ == '__main__':
    #app.debug = True
    #app.run(host=HOST['HOST'], port=HOST['PORT'])

    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    
    try:
       PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
       PORT = 5555
    1
    app.debug = True
    app.run(HOST, PORT)
