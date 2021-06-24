from flask import jsonify, Response, Blueprint
from ..models.exceptions import PasswordNotConfirmed, PasswordRejected, UsedMail, UserNotFound, UserNotValid, NicknameExists, InvalidMailError

errors_scope = Blueprint("errors", __name__)


def __generate_error_response(error: Exception) -> Response:
    message = {
        "ErrorType": type(error).__name__,
        "Message": str(error)
    }
    return jsonify(message)


@errors_scope.app_errorhandler(UserNotFound)
def handle_user_not_found(error: UserNotFound) -> Response:
    response = __generate_error_response(error)
    response.status_code = 404
    return response


@errors_scope.app_errorhandler(NicknameExists)
@errors_scope.app_errorhandler(UsedMail)
def handle_other_user_exceptions(error: Exception) -> Response:
    response = __generate_error_response(error)
    response.status_code = 409
    return response


@errors_scope.app_errorhandler(404)
def handle_not_found(error) -> Response:
    response = __generate_error_response(error)
    response.status_code = 404
    return response
