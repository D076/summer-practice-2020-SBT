import os
import signal
import sys
from flask import Flask
from .database import db
from app.api.tokenManager import TokenManager

token_manager = TokenManager()


def create_app():
    app = Flask(__name__)
    app.config.from_object(os.environ['APP_SETTINGS'])
    app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app)
    with app.test_request_context():
        db.create_all()

    if not 'db' in sys.argv:
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
