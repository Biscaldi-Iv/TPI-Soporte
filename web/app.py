#from entities.models import Users
from flask import Flask, request, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import redirect

from entities.models import Users

from Base_de_datos.dataTipoFamoso import KindOfUser
from Base_de_datos.dataUsuarios import UsuarioData


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():

    if request.method == 'POST':
        pass
    else:
        parametros={"usuario":None}
        return render_template('logIn.html',**parametros)



@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        pass
    else:
        return render_template('signUp.html')


if __name__ == '__main__':
    app.run(debug=True)
