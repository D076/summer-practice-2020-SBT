import os
import configparser
import sys
import json
from flask import Flask
from .database import db
from app.api.tokenManager import TokenManager
from app.gatewayconnector import GatewayConnector

token_manager = TokenManager()
gateway_connector = None

addr_white_list = list()

def create_app():
    app = Flask(__name__)

    config_path = './application.cfg'
    api_versions_path = 'app/api/api_versions.json'

    if not os.path.exists(config_path):
        raise FileNotFoundError('There is no application.properties in root directory')

    if not os.path.exists(api_versions_path):
        raise FileNotFoundError('There is no api_versions.json in app/api')

    config = configparser.ConfigParser()
    config.read(config_path)

    # Application configuration
    app.config['DEBUG'] = True if config['AuthService']['DEBUG'] == 'True' else False
    app.config['DEVELOPMENT'] = True if config['AuthService']['DEVELOPMENT'] == 'True' else False
    app.config['CSRF_ENABLED'] = True if config['AuthService']['CSRF_ENABLED'] == 'True' else False
    app.config['SECRET_KEY'] = config['AuthService']['SECRET_KEY']
    app.config['SQLALCHEMY_DATABASE_URI'] = config['AuthService']['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    service_ip = None
    service_port = None

    # Args parse
    if '-h' in sys.argv:
        service_ip = sys.argv[sys.argv.index('-h') + 1]
    else:
        service_ip = '127.0.0.1'

    if '-p' in sys.argv:
        service_port = int(sys.argv[sys.argv.index('-p') + 1])
    else:
        service_port = 5000

    # Database initialization
    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    if not 'db' in sys.argv:
        with open(api_versions_path, 'r') as f:
            apis = json.load(f)

        gateway_service_ip = config['Gateway']['HOST']
        gateway_service_port = config['Gateway']['PORT']

        # Initializing gateway connection
        gateway_connector = GatewayConnector(
            gateway_service_ip,
            gateway_service_port,
            service_ip,
            service_port,
            'Auth service',
            '0.1.1alpha',
            apis)

        print('#' * 50)
        print('GATEWAY CONNECTOR'.center(50))
        print('#' * 50)
        try:
            gateway_connector.publish()
            print('1) Published')

            gateway_connector.ready()
            print('2) Ready')

            gateway_connector.start()
            print('3) Thread started')

            addr_white_list.append(gateway_service_ip)
        except ConnectionError as ce:
            print(ce)
        except RuntimeError as re:
            print(re)

        print('#' * 50)

        token_manager.start()

    import app.api.views as api

    app.register_blueprint(api.module)
    
    return app
