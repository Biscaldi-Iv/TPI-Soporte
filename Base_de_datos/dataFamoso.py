# aqui guardaremos el manejo de la tabla famoso de la base de datos
import pymysql
from .connection import DataBase
from entities.models import Famous,KindOfFamous

class FamosoData(DataBase):
    def GetOne(self,idFamoso)->Famous:
        self.open()
        try:
            self.cursor.execute("select idfamoso,nombrecompleto,altura,fechanacimiento,foto,idtipofamoso from famoso where idfamoso=%s",(idFamoso,))
            return Famous(*self.cursor.fetchone().values())
        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def GetAll(self)->list[Famous]:
        self.open()
        listaFamosos=list()
        try:
            self.cursor.execute("select * from famoso",)
            for fam in self.cursor.fetchall():
                f=Famous(*fam.values())
                listaFamosos.append(f)
            return listaFamosos

        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def getFamosoXTipoF(self, tipoFamoso: KindOfFamous) -> list[Famous]:
        self.open()
        listaFamosos = list()
        try:
            self.cursor.execute("select * from famoso where idtipofamoso=%s", tipoFamoso.idTipoFamoso)
            for fam in self.cursor.fetchall():
                f=Famous(*fam.values())
                listaFamosos.append(f)
            return listaFamosos

        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()


f=FamosoData()
print(f.GetOne(idFamoso=1)) #NO TENGO NADA EN LA BASE DE DATOS TODAVIA ASI QUE VA A DAR ERROR
print("-----------")
print(f.GetAll())


