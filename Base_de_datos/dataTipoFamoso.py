# aqui guardaremos todas las tablas de la base de datos
import pymysql
from .connection import DataBase
from entities.models import KindOfUser

class TipoUsuarioData(DataBase):
    def GetOne(self,idTipoFamoso)->KindOfUser:
        self.open()
        try:
            self.cursor.execute("select idtipofamoso,detalle from tipofamoso where idtipofamoso=%s",(idTipoFamoso,))
            return KindOfUser(*self.cursor.fetchone().values())
        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def GetAll(self)->list[KindOfUser]:
        self.open()
        listaTipoFamosos=list()
        try:
            self.cursor.execute("select * from tipofamoso",)
            for tf in self.cursor.fetchall():
                t=KindOfUser(*tf.values())
                listaTipoFamosos.append(u)
            return listaTipoFamosos

        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

u=UsuarioData()
print(u.GetOne(idTipoFamoso="2"))
print("-----------")
print(u.GetAll())


