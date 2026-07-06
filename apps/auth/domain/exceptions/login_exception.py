from apps.shared.domain.exceptions.domain_exception import AppErrorException


class UserIsNotActiveException(AppErrorException):
    default_message = "User is not active"


class UserDoesNotExistException(AppErrorException):
    default_message = "User does not exist"


class InvalidCredentialsException(AppErrorException):
    default_message = "Invalid credentials"
