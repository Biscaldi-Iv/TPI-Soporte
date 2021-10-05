from  flask import request, url_for, Blueprint, session, render_template, redirect
from entities.models import Users
from bussiness.usuarios_logic import UserLogic

home_page= Blueprint('home', __name__, template_folder='templates')

@home_page.route('/home', methods=['POST', 'GET'])
def home():
    """if session.get('user_id')==None:
        return  redirect('http://127.0.0.1:5000/')"""
    ul=UserLogic()
    user=ul.login(request.form.get('floatingInput'),request.form.get('floatingPassword'))
    if user is not None:
        return render_template('home/home.html')
    return  redirect(url_for('login.login'))