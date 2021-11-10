import datetime

from flask import request, url_for, Blueprint, session, render_template, redirect, json, g
import requests
from entities.models import Users,Score
from bussiness.usuarios_logic import UserLogic
from bussiness.puntuacion_logic import PuntuacionLogic
from typing import Dict
from keys import secret_key, public_key
from flask_babel import gettext as _
from bussiness.preguntas_logic import PreguntasLogic
import random


global_scope= Blueprint('justintime', __name__, template_folder='templates')

@global_scope.url_defaults
def add_language_code(endpoint, values):
    values.setdefault('lang_code', g.lang_code)

@global_scope.url_value_preprocessor
def pull_lang_code(endpoint, values):

    url_lang_code_items_values = ['en','es','de','it']
    url_lang_code_default_item_value = 'es'

    g.lang_code = url_lang_code_default_item_value
    if values:
        if 'lang_code' in values:
            if values['lang_code'] in url_lang_code_items_values:
                g.lang_code = values.pop('lang_code', None)
            else:
                pass

def is_human(captcha_response):
    """ Validating recaptcha response from google server
        Returns True captcha test passed for submitted form else returns False.
    """
    secret = secret_key
    payload = {'response':captcha_response, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']

@global_scope.before_request
def SessionCheck():
    _, endp=request.endpoint.split('.')
    if endp!='questions':
        if 'nivel' in session.keys():
            session.pop('nivel')
    if endp!='login' and endp!='register' and endp!='logout':
        try:
            lastinteraction = session['lastinteraction'].replace(tzinfo=None)
            sincelast = (datetime.datetime.now() - lastinteraction).seconds/60
            #hay 10 minutos de sesion maximo hasta pedir login nuevamente
            if session['user'] is None or session['auth'] != 1 or sincelast > 10:
                return redirect('/logout')
        except:
            return redirect('/logout')
        # se renueva la sesion
        lastinteraction = datetime.datetime.now()
        session['lastinteraction'] = lastinteraction
    if 'lang' not in session.keys():
        session['lang']='en'

@global_scope.route('/home', methods=['POST', 'GET'])
def home():
    """if session.get('user_id')==None:
        return  redirect('http://127.0.0.1:5000/')"""
    user_logic=UserLogic()
    if session['user'] is not None:
        context={'user':user_logic.get(session.get('user'))}

        return render_template('home/home.html',**context)
    else:
        return redirect('/')

@global_scope.route('/', methods=['POST', 'GET'])
def login(contex:Dict=None):
    user_logic = UserLogic()
    if request.method == 'POST':
        error = None
        username = request.form['floatingInput']
        contraseña = request.form['floatingPassword']

        user = user_logic.login(username, contraseña)

        if type(user) == Users:
            session.clear()
            session['user'] = user.username
            session['auth'] = 1
            session['lastinteraction']=datetime.datetime.now()
            return redirect(url_for('justintime.home'))

        if user is None:
            error = "Username incorrecto"
            print(error)
        elif user is False:
            error = "Contraseña incorrecta"
            print(error)
        context = {'error': error, }
        return render_template('log_in/logIn.html', **context)
    else:
        try:
            if session['user'] is not None and session['auth']==1:
                return redirect(url_for('justintime.home'))
        except:
            if type(contex)==dict:
                print(dict)
                return render_template('log_in/logIn.html', **contex)
        print("no dict")
        return render_template('log_in/logIn.html')

@global_scope.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        """la unica forma de llegar a register con POST es registrando una cuenta-
        esta pagina registrara la cuenta y enviara a home"""
        context={'captcha':public_key}
        user_logic=UserLogic()
        newuser=Users(request.form['username'], request.form['name'],
                  request.form['lastname'], request.form['password'],
                  request.form['email'])
        captcha_response = request.form['g-recaptcha-response']
        if user_logic.get(newuser.username) is None:
            """registra"""
            #paso 1- chequear si las contraseñas coinciden
            if newuser.check_password(request.form['passconfirm']):
                if is_human(captcha_response):
                    user_logic.register(newuser)
                    session['user']=newuser.username
                    session['auth']=1
                    return redirect('/home')
                else:
                    context.update({'error':'No paso recaptcha', 'lastdata':newuser})
                    return render_template('register/register.html', **context)
            else:
                """no coinciden las contras"""
                context.update({'error':'Las contraseñas deben coincidir',
                                'lastdata':newuser})
        else:
            """usuario ya registrado"""
            context.update({'error': 'Nombre de Usuario ya registrado',
                            'lastdata': newuser,})
        """tendra el dict con el error surgido y recupera los datos para el form"""
        return render_template('register/register.html', **context)



    else:
        """method=get"""
        u=Users('','','','','')
        context={'error':'', 'lastdata':u, 'captcha':public_key}
        return render_template('register/register.html',**context)

@global_scope.route('/logout', methods=['POST','GET'])
def logout():
    session['user']=None
    session['auth']=0
    return redirect(url_for('justintime.login'))

@global_scope.route('/rules', methods=['POST', 'GET'])
def rules():
    return render_template('play/rules.html')

@global_scope.route('/questions', methods=['POST','GET'])
def questions():
    if request.method=='POST':
        if 'nivel' not in session.keys():
            session['nivel']=0
            session['puntuacion']=0
        
        if session['nivel']!=0 and request.form['formrespuesta']=='false':
            pl=PuntuacionLogic()
            s=Score(username=session['user'],score=session['puntuacion'])
            pl.register(s)
            contexto = {"username": session['user'], "puntuacion": session['puntuacion']}
            session.pop("puntuacion")
            session.pop("nivel")
            return render_template('play/results.html',**contexto)
        if 'dificultad' in session.keys():
            suma_puntos(session['dificultad'],session['nivel'])
        nivel=session['nivel']+1
        session['nivel']=nivel
        #cambiar despues la cantidad de veces de cada nivel
        if nivel<=10:
            session['dificultad']='facil'
            p = PreguntasLogic()
            pregunta, correcta, incorrecta, imagen = p.getRandomQuestion(4)
            contexto = {"pregunta": pregunta, "correcta": correcta, "incorrecta": incorrecta, "imagen": imagen}
            return render_template('play/easyQ.html', **contexto)
        elif nivel<=20:
            session['dificultad']='media'
            p = PreguntasLogic()
            pregunta, correcta, incorrecta, imagen = p.getRandomQuestion(8)
            contexto = {"pregunta": pregunta, "correcta": correcta, "incorrecta": incorrecta, "imagen": imagen }
            return render_template('play/middQ.html', **contexto)
        elif nivel>20:
            session['dificultad']='dificil'
            p = PreguntasLogic()
            pregunta, correcta, incorrecta, imagen = p.getRandomQuestion(8)
            contexto = {"pregunta": pregunta, "correcta": correcta, "incorrecta": incorrecta, "imagen": imagen }
            return render_template('play/hardQ.html', **contexto)
    else:
        #"arreglar **"
        return 'Estas haciendo trampa'





@global_scope.route('/menuTools', methods=['POST', 'GET'])
def menu_tools():
    return render_template('tools/menuTools.html')


def suma_puntos(dificultad: str, nivel: int):
     if dificultad == "facil" and nivel>0:
         session [ "puntuacion" ] += 10
     elif dificultad == "media":
         session [ "puntuacion" ] += 20
     elif dificultad == "dificil" :
         session [ "puntuacion" ] += 30

