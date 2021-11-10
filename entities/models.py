from datetime import datetime
from typing import Tuple,List,Any
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import  datetime


class Users():
    def __init__(self, username: str, nombre: str, apellido: str, password: str, email: str) -> None:
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        if "pbkdf2" in password:
            self.password=password
        else:
            self.set_password(password)
        self.email = email

    def lst(self) -> Tuple:
        """returns ('username', 'password', 'nombre', 'apellido', 'mail')"""
        return self.username, self.password, self.nombre, self.apellido, self.email

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

class Famous():
    def __init__(self, idFamoso: int, altura: float, fechaNacimiento: datetime, fortuna: float, img:str, nacionalidad: str,
        nombreCompleto: str, peso: float) -> None:
        self.idFamoso = idFamoso
        self.altura = altura
        self.fechaNacimiento = fechaNacimiento if fechaNacimiento!=0 else datetime.today()
        self.fortuna = fortuna
        self.imagen=img
        self.nacionalidad = nacionalidad
        self.nombreCompleto = nombreCompleto
        self.peso = peso


    def __repr__(self):
        return f"Famous({self.idFamoso},{self.altura},{self.fechaNacimiento},{self.fortuna},{self.nacionalidad}," \
               f"{self.nombreCompleto}, {self.peso} )"


class Score():
    def __init__(self, idPuntuacion=0, score: int=0, fechaPuntuacion: datetime=datetime.today(), username: str=''):
        self.idPuntuacion = idPuntuacion
        self.score = score
        self.fechaPuntuacion = fechaPuntuacion
        self.username = username


    def __repr__(self):
        return f"Score({self.idPuntuacion},{self.score},{self.fechaPuntuacion},{self.username})"

    def lst(self) -> List[Any]:
        """returns ('score', 'fechapuntuacion', 'username')"""
        return [self.score, self.fechaPuntuacion, self.username]


class Question():
    def __init__(self, idPregunta: int, descripcion: str) -> None:
        self.idPregunta = idPregunta
        self.descripcion = descripcion

    def __repr__(self):
        return f"Question({self.idPregunta},{self.descripcion})"

    def lst(self) -> Tuple:
        """returns ('idpregunta', 'descripcion')"""
        return self.idPregunta, self.descripcion
