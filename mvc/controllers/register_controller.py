from  flask import request, url_for, Blueprint, session, render_template

register_page= Blueprint('register', __name__, template_folder='templates')

@register_page.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        pass
    else:
        return render_template('sign_up/signUp.html')