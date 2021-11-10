""" manejo de la tabla puntuacion de la base de datos"""
import pymysql
from .connection import DataBase
from entities.models import Score
from typing import List

class PuntuacionData(DataBase):

    def register(self, puntuacion: Score) -> bool:
        """returns if stored in bd"""
        if puntuacion.score==0:
            return True
        insertcmd = "insert into puntuacion(score, fechapuntuacion, username) values (%s, %s, %s)"
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
                "select idpuntuacion, score, fechapuntuacion, username from puntuacion where username= %s order by score desc limit 10", username)
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
            self.cursor.execute("select idpuntuacion, score, fechapuntuacion, username from puntuacion order by score desc limit 10")
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


