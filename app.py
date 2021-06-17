from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
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
        return "User: {} {} {}".format(self.nickname, self.fullname, self.time_regist)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        pass
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

# video guia: https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=554s
