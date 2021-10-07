from  flask import request, url_for, Blueprint, session, render_template, redirect
from entities.models import Users
from bussiness.usuarios_logic import UserLogic
from typing import Dict


global_scope= Blueprint('justintime', __name__, template_folder='templates')

@global_scope.route('/home', methods=['POST', 'GET'])
def home():
    """if session.get('user_id')==None:
        return  redirect('http://127.0.0.1:5000/')"""
    user_logic=UserLogic()
    if session['user'] is not None:
        context={'user':user_logic.get(session.get('user'))}
        """Falta chequear si esta logueado"""
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
            context = {'user': user}
            return redirect('/home')

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
                return redirect('/home')
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
        context=dict()
        user_logic=UserLogic()
        newuser=Users(request.form['username'], request.form['name'],
                  request.form['lastname'], request.form['password'],
                  request.form['email'])

        if user_logic.get(newuser.username) is None:
            """registra"""
            #paso 1- chequear si las contraseñas coinciden
            if newuser.check_password(request.form['passconfirm']):
                user_logic.register(newuser)
                print("usuario registrado")
                session['user']=newuser.username
                session['auth']=1
                return redirect('/home')
            else:
                """no coinciden las contras"""
                context.update({'error':'Las contraseñas deben coincidir',
                                'lastdata':newuser})
        else:
            """usuario ya registrado"""
            context.update({'error': 'Nombre de Usuario ya registrado',
                            'lastdata': newuser})
        """tendra el dict con el error surgido y recupera los datos para el form"""
        return render_template('register/register.html', **context)



    else:
        """method=get"""
        u=Users('','','','','')
        context={'error':'', 'lastdata':u}
        return render_template('register/register.html',**context)

@global_scope.route('/logout', methods=['POST','GET'])
def logout():
    session['user']=None
    session['auth']=0
    return redirect('/')

