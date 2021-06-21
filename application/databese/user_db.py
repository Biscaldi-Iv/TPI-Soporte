from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


def set_data_base(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    db = SQLAlchemy(app)
