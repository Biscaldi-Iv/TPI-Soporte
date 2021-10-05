from  flask import request, url_for, Blueprint, session, render_template

login_page=Blueprint('login', __name__, template_folder='templates')

@login_page.route('/', methods=['POST', 'GET'])
def login():

    if request.method == 'POST':
        error = None
        usuario = request.form['floatingInput']
        contraseña = request.form['floatingPassword']
        # if harcodeado
        if usuario == 'ivan123':
            if contraseña == 'IV100100':
                session.clear()
                session['user_id'] = usuario
                return f'hola {usuario}'
            else:
                error = 'Clave incorrecta'
        else:
            error = 'Nombre incorrecto'
        context = {'error': error, }
        return render_template('log_in/logIn.html', **context)

    else:
        return render_template('log_in/logIn.html')
