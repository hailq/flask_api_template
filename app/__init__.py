import os
from flask import Flask, request

from app.commons.exceptions import NotAllowed, NotFound, InvalidUsage, Unauthorized
from config import Config as DefaultConfig


def create_app(config_name):
    """Create an application instance."""
    app = Flask(__name__)

    # Apply configuration
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_object(DefaultConfig)  # Default settings
    app.config.from_pyfile(cfg)

    # Register blueprints
    from .api_v1 import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix=f"{app.config['BASE_URL']}/api/v1")

    # Hello endpoint
    @app.route('/hello', methods=['GET'])
    def hello():
        return 'Hello, Got It'

    # Handle request events
    @app.before_request
    def handle_before_request():
        # Allow the pre-flight requests to get through
        if request.method == 'OPTIONS':
            return None

    from .commons.error_handlers import register_error_handlers

    register_error_handlers(app)

    return app
