import re

from ..models.models import Users
from ..models.exceptions import PasswordNotConfirmed, UserNotValid, PasswordRejected, InvalidMailError
from ..database import users_db


def validate_user(usr: Users, pas2: str) -> None:
    if not __email_is_valid(usr.email):
        raise InvalidMailError(f"The email address: {usr.email} is not valid")

    if None in (usr.fullname):
        raise UserNotValid("The user has no name")

    if not __password_is_confirmed(usr.password, pas2):
        raise PasswordNotConfirmed("The password was never confirmed")

    if not __is_valid_len_pasword(usr.password):
        raise PasswordRejected(
            "The lengh of the password is too large or not enough, use more than 8 characters and less than 16")


def format_name(usr: Users) -> Users:
    "To Uppercase"
    user_dict = usr._asdict()
    user_dict["fullname"] = usr.fullname.capitalize()

    return Users(**user_dict)


def __email_is_valid(email: str) -> bool:
    "Check if mail field seems to have a valid mail adress"
    if not isinstance(email, str):
        return False

    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    return bool(re.search(regex, email))


def __is_valid_len_pasword(pass: str) -> bool:
    if 8 < len(pass) < 16:
        return False


def __password_is_confirmed(pwd1: str, pwd2: str) -> bool:
    "Check password an password confirmation fields values"
    if pwd1 != pwd2:
        return False


def __check_Nickname(nick: str) -> bool:
    return users_db.user_exists("nickname", nick)
