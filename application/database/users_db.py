"Functions to CRUD an user, table-> users"
from application.models.models import Users
from typing import List, Tuple

from connection import _fetch_all, _fetch_lastrow_id, _fetch_none, _fetch_one
from ..models.exceptions import NicknameExists, UsedMail
from ..models.models import Users


def create_user(user_: Users):
    if user_exists("email", user_.email):
        raise UsedMail(f"Email:{user_.email} is already registered")
    if user_exists("nickname", user_.nickname):
        raise NicknameExists(
            f"Nickname:{user_.nickname} is already registered")

    query = """INSERT INTO users VALUES (:nickname, :password,
                                            :fullname, :email, :time_regist)"""

    user_dict = user_._asdict()

    id_ = _fetch_lastrow_id(query, user_dict)

    user_dict["id"] = id_
    return Users(**user_dict)


def user_exists(field: str, value: str) -> bool:
    "field: field to check, value:value inserted by web user"
    query = f"SELECT id, nickname, email FROM users WHERE {field}=?"
    parameters = [value]
    record = _fetch_one(query, parameters)

    return bool(record)


def create_table():
    query = "DROP TABLE IF EXISTS users"
    _fetch_none(query)

    fields = """(id integer primary_key=True, nickname text, password text, fullname text,
                     email text, time_regist text)"""
    query = f"CREATE TABLE IF NOT EXISTS users {fields}"

    _fetch_none(query)


def list_all() -> List[Users]:
    query = "SELECT * FROM users"
    records = _fetch_all(query)
