# aqui guardaremos el manejo de la tabla usuario de la base de datos
import pymysql
from connection import DataBase
from entities.models import Users


class UsuarioData(DataBase):
    def GetOne(self, username) -> Users:
        self.open()
        try:
            self.cursor.execute(
                "select username,nombre,apellido,password,email from usuario where username=%s", (username,))
            return Users(*self.cursor.fetchone().values())
        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def GetAll(self) -> list[Users]:
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


u = UsuarioData()
print(u.GetOne(username="blitz"))
print("-----------")
print(u.GetAll())
