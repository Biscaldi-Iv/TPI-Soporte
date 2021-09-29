# aqui guardaremos el manejo de la tabla famoso de la base de datos
import pymysql
from .connection import DataBase
from entities.models import Score

class PuntuacionData(DataBase):
    def GetOne(self,idPuntuacion)->Score:
        self.open()
        try:
            self.cursor.execute("select idpuntuacion,score, fechaPuntuacion,tiempoPuntuacion,username from puntuacion where idpuntuacion=%s",(idPuntuacion,))
            return Score(*self.cursor.fetchone().values())
        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def GetAll(self)->list[Score]:
        self.open()
        listaPuntuaciones=list()
        try:
            self.cursor.execute("select * from puntuacion",)
            for pun in self.cursor.fetchall():
                p=Score(*pun.values())
                listaPuntuaciones.append(p)
            return listaPuntuaciones

        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

p=PuntuacionData()
print(p.GetOne(idPuntuacion=1)) #NO TENGO NADA EN LA BASE DE DATOS TODAVIA ASI QUE VA A DAR ERROR
print("-----------")
print(p.GetAll())


