# aqui guardaremos todas las tablas de la base de datos
import pymysql
from connection import DataBase

class UsuarioData(DataBase):
    def GetOne(self,username):
        self.cursor.execute("select username,nombre,apellido from usuario where username=?",(username,))
        return self.cursor.fetchAll()




usuario=UsuarioData()
print(usuario.GetOne("pepito"))