from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Users():
    def __init__(self, username: str, nombre: str, apellido: str, password: str, email: str) -> None:
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.set_password(password)
        self.email = email

    def __repr__(self):
        return f"Users({self.username},{self.nombre},{self.apellido},{self.password},{self.email})"

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

"""
    @staticmethod
    def get_by_id(id):
        return Users.query.get(id)

    @staticmethod
    def get_by_email(email):
        return Users.query.filter_by(email=email).first()
"""

class KindOfFamous():
    def __init__(self, idTipoFamoso: int, detalle: str) -> None:
        self.idTipoFamoso = idTipoFamoso
        self.detallle = detalle

    def __repr__(self):
        return f"KindOfFamous({self.idTipoFamoso},{self.detallle})"


class Famous():
    def __init__(self, idFamoso: int, nombreCompleto: str, altura: float, fechaNacimiento: datetime, foto: str, idTipoFamoso: int) -> None:
        self.idFamoso = idFamoso
        self.nombreCompleto = nombreCompleto
        self.altura = altura
        self.fechaNacimiento = fechaNacimiento
        self.foto = foto
        self.idTipoFamoso = idTipoFamoso

    def __repr__(self):
        return f"Users({self.idFamoso},{self.nombreCompleto},{self.altura},{self.fechaNacimiento},{self.foto},{self.idTipoFamoso})"


