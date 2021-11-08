# aqui guardaremos el manejo de la tabla usuario de la base de datos
import pymysql
from .connection import DataBase
from entities.models import Users
from typing import List, Optional


class UsuarioData(DataBase):
    def __init__(self):
        super().__init__()
#=====================================================================================================================#
    def GetOne(self, username) -> Optional[Users]:
        """:return: User-->Exists|| None-->Not found"""
        self.open()
        try:
            self.cursor.execute(
                "select * from usuario where username=%s", username)
            u = Users(*self.cursor.fetchone().values())
            return u
        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
            return None

        finally:
            self.cursor.close()
            self.close()

#=====================================================================================================================#
    def GetAll(self) -> List[Users]:
        self.open()
        listaUsuarios = list()
        try:
            self.cursor.execute("select * from usuario",)
            for usu in self.cursor.fetchall():
                u = Users(*usu.values())
                listaUsuarios.append(u)
            return listaUsuarios

        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

#=====================================================================================================================#
    def register(self, usuario: Users) -> bool:
        """returns if stored in bd"""
        insertcmd = "insert into usuario(username, password, nombre, apellido, email) values (%s, %s, %s, %s, %s)"
        self.open()
        try:
            self.cursor.execute(insertcmd, usuario.lst())
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.cursor.close()
            self.close()

#=====================================================================================================================#
    def update(self, user: Users) -> bool:
        """:returns: if saved changes"""
        updt = "update usuario set password= %s, nombre= %s, apellido= %s, email= %s where username= %s"
        params = (user.password, user.nombre,
                  user.apellido, user.email, user.username)
        self.open()
        try:
            self.cursor.execute(updt, params)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False
        finally:
            self.cursor.close()
            self.connection.close()
