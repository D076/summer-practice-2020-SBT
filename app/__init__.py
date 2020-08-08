import os
import signal
import sys
from flask import Flask
from .database import db
from app.api.tokenManager import TokenManager
from app.gatewayconnector import GatewayConnector

token_manager = TokenManager()
gateway_connector = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    if not 'db' in sys.argv:
        apis = [
            {
                'path': '/auth',
                'api_version': 'v1'
            },
            {
                'path': '/user/{login}/{password}/{name}',
                'api_version': 'v1'
            },
            {
                'path': '/index',
                'api_version': 'v1'
            }
        ]

        gateway_connector = GatewayConnector('127.0.0.1', 1123, '127.0.0.1', 'Auth service', '0.1.1alpha', apis)

        try:
            gateway_connector.publish()
            print('[GATEWAY CONNECTOR] Published')
            gateway_connector.ready()
            print('[GATEWAY CONNECTOR] Ready')
            gateway_connector.start()
            print('[GATEWAY CONNECTOR] Thread started')
        except ConnectionError:
            print('Gateway connection error')

        token_manager.start()

    if app.debug == True:
        try:
            from flask_debugtoolbar import DebugToolbarExtension
            toolbar = DebugToolbarExtension(app)
        except:
            pass

    import app.api.views as api

    app.register_blueprint(api.module)
    
    return app
