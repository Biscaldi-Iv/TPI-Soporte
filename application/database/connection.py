from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABESE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
