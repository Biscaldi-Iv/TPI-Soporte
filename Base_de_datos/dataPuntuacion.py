""" manejo de la tabla puntuacion de la base de datos"""
import pymysql
from .connection import DataBase
from entities.models import Score
from typing import List

class PuntuacionData(DataBase):
    def GetOne(self,idPuntuacion)->Score:
        self.open()
        try:
            self.cursor.execute("select idpuntuacion,score, fechaPuntuacion,tiempoPuntuacion,username from puntuacion where idpuntuacion=%s",(idPuntuacion,))
            return Score(*self.cursor.fetchone().values())
        except:
            print(f"No se pudo recuperar la puntuacion {idPuntuacion=}")
            self.connection.rollback()
            raise Exception(f"No se pudo recuperar la puntuacion {idPuntuacion=}")
        finally:
            self.cursor.close()
            self.close()

# =====================================================================================================================#
    def GetAll(self)->List[Score]:
        self.open()
        listaPuntuaciones=list()
        try:
            self.cursor.execute("select * from puntuacion",)
            for pun in self.cursor.fetchall():
                p=Score(*pun.values())
                listaPuntuaciones.append(p)
            return listaPuntuaciones

        except:
            print("Error al recuperar puntuaciones")
            self.connection.rollback()
            raise Exception("Error al recuperar puntuaciones")
        finally:
            self.cursor.close()
            self.close()

# =====================================================================================================================#
    def register(self, puntuacion: Score) -> bool:
        """returns if stored in bd"""
        insertcmd = "insert into puntuacion(score, fechapuntuacion, tiempopuntuacion, username) values (%s, %s, %s, %s)"
        self.open()
        try:
            self.cursor.execute(insertcmd, puntuacion.lst())
            self.connection.commit()
            return True
        except Exception as e:
            self.connection.rollback()
            return False
        finally:
            self.cursor.close()
            self.close()

#=====================================================================================================================#
    def myTop(self, username):
        listapuntuaciones = list()
        self.open()
        try:
            self.cursor.execute(
                "select idpuntuacion, score, fechapuntuacion, tiempopuntuacion, username from puntuacion where username= %s limit 10", username)
            for pun in self.cursor.fetchall():
                p = Score(*pun.values())
                listapuntuaciones.append(p)
            return listapuntuaciones
        except Exception as e:
            raise Exception(f"No fue posible recuperar las puntuaciones del jugador {username}")
        finally:
            self.cursor.close()
            self.close()

#=====================================================================================================================#
    def top10(self):
        listapuntuaciones=list()
        self.open()
        try:
            self.cursor.execute("select idpuntuacion, score, fechapuntuacion, tiempopuntuacion, username from puntuacion limit 10")
            for pun in self.cursor.fetchall():
                p=Score(*pun.values())
                listapuntuaciones.append(p)
            return listapuntuaciones
        except Exception as e:
            raise Exception("No fue posible recuperar las puntuaciones")
        finally:
            self.cursor.close()
            self.close()





"""p=PuntuacionData()
print(p.GetOne(idPuntuacion=1)) #NO TENGO NADA EN LA BASE DE DATOS TODAVIA ASI QUE VA A DAR ERROR
print("-----------")
print(p.GetAll())"""


