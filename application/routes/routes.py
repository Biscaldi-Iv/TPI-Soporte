from flask import Blueprint, render_template

global_scope = Blueprint("views", __name__)
usr_register = Blueprint("views", __name__)

nav = [
    {"name": "Listar", "url": "api/users"}
]


@global_scope.route("/", methods=['GET'])
def home():
    parameters = {"title": "Cuanto es¿?", "description": "Home page"}
    return render_template("home.html", nav=nav, **parameters)
