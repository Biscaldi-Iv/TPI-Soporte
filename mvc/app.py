from flask import Flask, session
from controllers.routes import global_scope
from flask_babel import Babel, gettext as _

app = Flask(__name__)

app.secret_key = 'www123456www'
app.config['BABEL_DEFAULT_LOCALE']='en'
app.config['BABEL_TRANSLATION_DIRECTORIES']='/home/usuario/Documentos/Soporte 2021/TPI-Soporte/translations'
babel=Babel(app)

@babel.localeselector
def get_locale():
    #return session['lang']
    return 'it'

@app.before_request
def session_control():  # control de sesion -->ver
    session.permanent = True

app.register_blueprint(global_scope)

#agregar optional en nav var para evitar que alla botones que no corresponden

if __name__ == '__main__':
    app.run(debug=True)
