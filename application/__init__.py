from application.databese.user_db import set_data_base
from flask import Flask, render_template, url_for, request
from werkzeug.utils import redirect
import databese.user_db as user_db
from databese.user_db import set_data_base, set_data_base.Users


app = Flask(__name__)
set_data_base(app)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        nkn = request.form['Nick']
        # sin verificar contra
        ps = request.form['Password']
        fn = request.form['full']
        em = request.form['mail']
        new_user: Users = Users(
            nickname=nkn, pasword=ps, fullname=fn, email=em)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')
        except:
            return new_user

    else:
        usuarios = Users.query.all()
        return render_template('index.html', usuarios=usuarios)


if __name__ == "__main__":
    app.run(debug=True)

# video guia: https://www.youtube.com/watch?v=Z1RJmh_OqeA&t=554s
