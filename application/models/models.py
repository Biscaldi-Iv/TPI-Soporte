#from flask_sqlalchemy import SQLAlchemy
from typing import NamedTuple, Optional
from datetime import datetime

#db = SQLAlchemy(app)
"""
class Users(db.Model):
    nickname = db.Column(db.String(50), primary_key=True)
    pasword = db.Column(db.String(16), nullable=False)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    time_regist = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "User: nick={} name={} time={}".format(self.nickname, self.fullname, self.time_regist)
        """


class Users(NamedTuple):
    nickname: Optional[int] = None
    pasword: Optional[str] = None
    fullname: Optional[str] = None
    email: Optional[str] = None
    time_regist: Optional[datetime] = None

    def __repr__(self):
        return "User: nick={} name={} time={}".format(self.nickname, self.fullname, self.time_regist)
