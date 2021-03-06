from flask import Flask, session, request, g, redirect
from flask.helpers import url_for
from flask.templating import render_template
from controllers.routes import global_scope
from flask_babel import Babel, gettext as _, lazy_gettext
from bussiness.preguntas_logic import PreguntasLogic

app = Flask(__name__)

app.secret_key = 'www123456www'
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_TRANSLATION_DIRECTORIES'] = '/home/usuario/Documentos/Soporte 2021/TPI-Soporte/translations'
babel = Babel(app)


@babel.localeselector
def get_locale():
    request_lc = request.args.get('lc')
    if not request_lc:
        if not 'lang_code' in g:
            # use default
            g.lang_code = 'en'
            request_lc = 'en'
        else:
            if g.lang_code == 'es':
                request_lc = 'es'
            elif g.lang_code == 'de':
                request_lc = 'de'
            elif g.lang_code == 'it':
                request_lc = 'it'
            else:
                request_lc = 'en'

    else:
        # set g.lang_code to the requested language
        if request_lc == 'de_DE':
            g.lang_code = 'de'
        elif request_lc == 'es_ES':
            g.lang_code = 'es'
        elif request_lc == 'it_IT':
            g.lang_code = 'it'
        else:
            request_lc = 'en_US'
            g.lang_code = 'en'
        # sys.exit()
    session['lc'] = request_lc
    return request_lc


@app.before_request
def session_control():  # control de sesion -->ver
    session.permanent = True


@app.route('/', methods=['POST', 'GET'])
def redireccion():
    langcode=get_locale()
    if type(langcode) is None or len(langcode)<2:
        langcode='en'
    return redirect(url_for('justintime.home'))
    #return redirect('/'+langcode+'/home')


app.register_blueprint(global_scope, url_prefix='/<lang_code>')

# agregar optional en nav var para evitar que alla botones que no corresponden

if __name__ == '__main__':
    app.run(debug=True)
    """pregs=PreguntasLogic()
    pr,resp,inc=pregs.getRandomQuestion(4)
    print(pr)
    print(resp)
    for i in inc:
        print(i)
"""
