from  flask import request, url_for, Blueprint, session, render_template, redirect
from entities.models import Users
from bussiness.usuarios_logic import UserLogic
from typing import Dict

global_scope= Blueprint('home', __name__, template_folder='templates')

@global_scope.route('/home', methods=['POST', 'GET'])
def home():
    """if session.get('user_id')==None:
        return  redirect('http://127.0.0.1:5000/')"""
    user_logic = UserLogic()
    if request.method == 'POST':
        error = None
        username = request.form['floatingInput']
        contraseña = request.form['floatingPassword']

        user = user_logic.login(username, contraseña)

        if type(user) == Users:
            session.clear()
            session['user']=user.username
            session['auth']=1
            context={'user':user}
            return render_template('home/home.html',**context)

        if user is None:
            error = "Username incorrecto"
        elif user is False:
            error = "Contraseña incorrecta"
        context = {'error': error, }
        return login(context)
    else:
        context={'user':user_logic.get(session.get('user'))}
        """Falta chequear si esta logueado"""
        return render_template('home/home.html',**context)

@global_scope.route('/', methods=['POST', 'GET'])
def login(contex:Dict=None):
    try:
        if session['user'] is not None and session['auth']==1:
            return redirect('/home')
    except:
        if type(contex)==dict:
            return render_template('log_in/logIn.html', **contex)
        return render_template('log_in/logIn.html')

@global_scope.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        pass
    else:
        return render_template('sign_up/signUp.html')

