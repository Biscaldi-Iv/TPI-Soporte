from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from run import db
from web.app import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50), nullable=False)
    pasword = db.Column(db.String(16), nullable=False)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    time_regist = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"User: {self.nickname}"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):
        if not self.id:
            db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_by_id(id):
        return Users.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Users.query.filter_by(email=email).first()
