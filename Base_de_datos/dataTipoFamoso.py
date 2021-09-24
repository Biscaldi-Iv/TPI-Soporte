# aqui guardaremos el manejo de la tabla tipofamoso de la base de datos
import pymysql
from .connection import DataBase
from entities.models import KindOfFamous

class TipoFamosoData(DataBase):
    def GetOne(self,idTipoFamoso)->KindOfFamous:
        self.open()
        try:
            self.cursor.execute("select idtipofamoso,detalle from tipofamoso where idtipofamoso=%s",(idTipoFamoso,))
            return KindOfFamous(*self.cursor.fetchone().values())
        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def GetAll(self)->list[KindOfFamous]:
        self.open()
        listaTipoFamosos=list()
        try:
            self.cursor.execute("select * from tipofamoso",)
            for tf in self.cursor.fetchall():
                t=KindOfFamous(*tf.values())
                listaTipoFamosos.append(t)
            return listaTipoFamosos

        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

u=TipoFamosoData()
print(u.GetOne(idTipoFamoso=2))
print("-----------")
print(u.GetAll())


