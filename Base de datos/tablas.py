# aqui guardaremos todas las tablas de la base de datos
import pymysql
from connection import DataBase

class Users():
    def __init__(self, username: str, nombre: str, apellido: str, password: str, email: str) -> None:
        self.username = username
        self.nombre = nombre
        self.apellido = apellido
        self.password = password
        self.email = email

    def __repr__(self):
        return f"Users({self.username},{self.nombre},{self.apellido},{self.password},{self.email})"

class UsuarioData(DataBase):
    def GetOne(self,username):
        self.cursor.execute("select username,nombre,apellido,password,email from usuario where username=%s",(username,))
        return self.cursor.fetchone()

    def GetAll(self):
        self.cursor.execute("select * from usuario",)
        return self.cursor.fetchall()




usuario=UsuarioData()
print(usuario.GetOne("pepito"))
u=Users(*usuario.GetOne("pepito").values())
print(u)