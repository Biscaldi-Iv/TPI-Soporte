#from entities.models import Users
from logging import error
from flask import Flask, request, url_for, render_template, session
from markupsafe import escape  # sirve para evitar inyecciones
from  controllers.login_controller import login_page
from  controllers.register_controller import register_page
from  controllers.home_controller import home_page

#from entities.models import  Users
#from  bussiness.usuarios_logic import UserLogic

from werkzeug.utils import redirect


app = Flask(__name__)

app.secret_key = 'www123456www'


@app.before_request
def session_control():  # control de sesion -->ver
    session.permanent = True


app.register_blueprint(login_page)

app.register_blueprint(register_page)

app.register_blueprint(home_page)

if __name__ == '__main__':
    app.run(debug=True)
