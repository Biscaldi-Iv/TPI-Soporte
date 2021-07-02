#from entities.models import Users
from flask import Flask, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tester.db'
db = SQLAlchemy(app)


@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        pass
    else:
        return render_template('home_ext.html')


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        pass
    else:
        return render_template('register_ext.html')


@app.route('/users_control', methods=['POST', 'GET'])
def usr_control():
    if request.method == 'POST':
        """"
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
        except Exception:
            return Exception
            """
    else:
        usuarios = Users.query.all()
        return render_template('usr_control_ext.html')


if __name__ == '__main__':
    app.run(debug=True)
