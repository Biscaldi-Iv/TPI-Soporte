# aqui guardaremos el manejo de la tabla tipofamoso de la base de datos
import pymysql
<<<<<<< HEAD
from connection import DataBase
from entities.models import KindOfUser

class TipoUsuarioData(DataBase):
    def GetOne(self,idTipoFamoso:int)->KindOfUser:
=======
from .connection import DataBase
from entities.models import KindOfFamous

class TipoFamosoData(DataBase):
    def GetOne(self,idTipoFamoso)->KindOfFamous:
>>>>>>> 981ac298c73e41cb72e52544ff75ee65ab1e5b65
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

<<<<<<< HEAD
u=TipoUsuarioData()
=======
u=TipoFamosoData()
>>>>>>> 981ac298c73e41cb72e52544ff75ee65ab1e5b65
print(u.GetOne(idTipoFamoso=2))
print("-----------")
print(u.GetAll())


