import re

from ..models.models import Users
from ..models.exceptions import PasswordNotConfirmed, UserNotValid


def validate_user(usr: Users, pas2: str) -> None:
    if not __email_is_valid(usr.email):
        raise UserNotValid(f"The email address: {usr.email} is not valid")

    if None in (usr.nickname, usr.fullname, usr.email):
        raise UserNotValid("The user has no first name, last name or email")

    if not __password_is_confirmed(usr.password, pas2):
        raise PasswordNotConfirmed("The password was never confirmed")

    if not __is_valid_len_pasword(usr.password):
        raise PasswordNotConfirmed(
            "The lengh of the pass was too large or not enough")


def format_name(usr: Users) -> Users:
    user_dict = usr._asdict()
    user_dict["fullname"] = usr.fullname.capitalize()

    return Users(**user_dict)


def __email_is_valid(email: str) -> bool:
    if not isinstance(email, str):
        return False

    regex = r'^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'

    return bool(re.search(regex, email))


def __is_valid_len_pasword(pass: str) -> bool:
    if 8 < len(pass) < 16:
        return False


def __password_is_confirmed(pwd1: str, pwd2: str) -> bool:
    if pwd1 != pwd2:
        return False
