from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Users():
    def __init__(self, id: int, nickname: str, password: str, fullname: str, email: str, register: datetime = datetime.utcnow) -> None:
        self.id = id
        self.nickname = nickname
        self.set_password(password)
        self.fullname = fullname
        self.email = email
        self.time_regist = register

    def __repr__(self):
        return f"Users({self.id},{self.nickname},{self.password},{self.fullname},{self.email, self.time_regist})"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


"""
    @staticmethod
    def get_by_id(id):
        return Users.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Users.query.filter_by(email=email).first()
"""
