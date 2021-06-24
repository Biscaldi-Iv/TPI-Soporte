class PasswordNotConfirmed(Exception):
    "Password and confirmation fields does not match"
    pass


class PasswordRejected(Exception):
    "Password must have between 8 and 16 characters"
    pass


class NicknameExists(Exception):
    "Nickname already in use"
    pass


class UsedMail(Exception):
    "Mail already registered"
    pass


class InvalidMailError(Exception):
    "Not valid mail"
    pass


class UserNotFound(Exception):
    "User name or mail not registred"
    pass


class UserNotValid(Exception):
    "User has no name"
    pass
