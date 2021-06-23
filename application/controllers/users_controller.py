from typing import List

from database import users_db
from ..models.models import Users
from ..helpers import helper


def create(user_: Users, pwdConf: str):
    user_ = helper.format_name(user_)
    helper.validate_user(user_, pwdConf)
    return users_db.create(user_)
