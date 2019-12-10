from .exceptions import Unauthorized, NotAllowed, NotFound, InvalidUsage


def register_error_handlers(app):
    # Handle request errors
    common_payload = {
        '_meta': {
            'service_name': app.config['SERVICE_NAME']
        }
    }

    @app.errorhandler(401)
    def unauthorized(error):
        return Unauthorized(
            message="Bad username or password",
            payload=common_payload
        ).to_response()

    @app.errorhandler(404)
    def not_found(error):
        return NotFound(
            message="Resource was not found",
            payload=common_payload
        ).to_response()

    @app.errorhandler(405)
    def not_allowed(error):
        return NotAllowed(
            message="Method was not allowed",
            payload=common_payload
        ).to_response()

    @app.errorhandler(InvalidUsage)
    def invalid_usage(error: InvalidUsage):
        return error.to_response()
