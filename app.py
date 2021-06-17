from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker, relationship
"""
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


class Users(db.Model):
    nickname = db.Column(db.String(50), primary_key=True)
    pasword = db.Column(db.String(16), nullable=False)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    time_regist = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "User: nick={} name={} time={}".format(self.nickname, self.fullname, self.time_regist)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nkn = request.form['Nick']
        # sin verificar contra
        ps = request.form['Password']
        fn = request.form['full']
        em = request.form['mail']
        new_user: Users = Users(
            nickname=nkn, pasword=ps, fullname=fn, email=em)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return new_user

    else:
        usuarios = Users.query.all()
        return render_template('index.html', usuarios=usuarios)


if __name__ == "__main__":
    app.run(debug=True)

# video guia: https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=554s
