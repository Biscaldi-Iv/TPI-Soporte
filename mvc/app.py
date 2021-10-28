#from entities.models import Users
from logging import error
from flask import Flask, request, url_for, render_template, session
from markupsafe import escape  # sirve para evitar inyecciones
from controllers.routes import global_scope

#from entities.models import  Users
#from  bussiness.usuarios_logic import UserLogic

from werkzeug.utils import redirect



app = Flask(__name__)

app.secret_key = 'www123456www'



@app.before_request
def session_control():  # control de sesion -->ver
    session.permanent = True


app.register_blueprint(global_scope)

#agregar optional en nav var para evitar que alla botones que no corresponden

if __name__ == '__main__':
    app.run(debug=True)
