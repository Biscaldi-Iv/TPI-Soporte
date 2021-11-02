from flask import Flask, session, request, g, redirect
from controllers.routes import global_scope
from flask_babel import Babel, gettext as _

app = Flask(__name__)

app.secret_key = 'www123456www'
app.config['BABEL_DEFAULT_LOCALE']='en'
app.config['BABEL_TRANSLATION_DIRECTORIES']='/home/usuario/Documentos/Soporte 2021/TPI-Soporte/translations'
babel=Babel(app)

@babel.localeselector
def get_locale():
    request_lc = request.args.get('lc')
    if not request_lc:
        if not 'lang_code' in g:
            # use default
            g.lang_code = 'en'
            request_lc = 'en_US'
        else:
            if g.lang_code == 'es':
                request_lc = 'es_ES'
            elif g.lang_code == 'de':
                request_lc = 'de_DE'
            elif g.lang_code=='it':
                request_lc='it_IT'
            else:
                request_lc = 'en_US'

    else:
        # set g.lang_code to the requested language
        if request_lc == 'de_DE':
            g.lang_code = 'de'
        elif request_lc == 'es_ES':
            g.lang_code = 'es'
        elif request_lc=='it_IT':
            g.lang_code='it'
        else:
            request_lc = 'en_US'
            g.lang_code = 'en'
        # sys.exit()
    session['lc'] = request_lc
    return request_lc

@app.before_request
def session_control():  # control de sesion -->ver
    session.permanent = True


app.register_blueprint(global_scope, url_prefix='/<lang_code>')

#agregar optional en nav var para evitar que alla botones que no corresponden

if __name__ == '__main__':
    app.run(debug=True)
