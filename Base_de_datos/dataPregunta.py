# aqui guardaremos el manejo de la tabla preguntas de la base de datos

from .connection import DataBase
from entities.models import Question
from typing import List, Optional

#from .dataPuntuacion import PuntuacionData


class PreguntaData(DataBase):
    def __init__(self):
        super().__init__()
#=====================================================================================================================#
    def GetOne(self, idPregunta) -> Optional[Question]:
        """:return: idPregunta-->Exists|| None-->Not found"""
        self.open()
        try:
            self.cursor.execute(
                "select * from pregunta where idpregunta=%s", idPregunta)
            q = Question(*self.cursor.fetchone().values())
            return q
        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
            return None

        finally:
            self.cursor.close()
            self.close()

#=====================================================================================================================#
    def GetAll(self) -> List[Question]:
        self.open()
        listaPreguntas = list()
        try:
            self.cursor.execute("select * from pregunta",)
            for preg in self.cursor.fetchall():
                p = Question(*preg.values())
                listaPreguntas.append(p)
            return listaPreguntas

        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

#=====================================================================================================================#
#=====================================================================================================================#


"""
tf=TipoFamosoData()
print(tf.GetOne(idTipoFamoso=1))
print("-----------")
print("-----------")
p=PreguntaData()
print(p.GetOne(idPregunta=1))
print("-----------")
print("-----------")
print(p.getPreguntaXTipoF(tf.GetOne(idTipoFamoso=1)))
print("-----------")
print("-----------")
print(p.GetAll())
"""
