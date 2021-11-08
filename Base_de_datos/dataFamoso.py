# aqui guardaremos el manejo de la tabla famoso de la base de datos
from typing import List
from .connection import DataBase
from entities.models import Famous


class FamosoData(DataBase):
    def GetOne(self, idFamoso) -> Famous:
        self.open()
        try:
            self.cursor.execute("SELECT * FROM famosos where id=%s", (idFamoso,))
            return Famous(*self.cursor.fetchone().values())
        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def GetAll(self) -> List[Famous]:
        self.open()
        listaFamosos = list()
        try:
            self.cursor.execute("select * from famosos", )
            for fam in self.cursor.fetchall():
                f = Famous(*fam.values())
                listaFamosos.append(f)
            return listaFamosos

        except:
            print("excepcion ocurrida bro")
            self.connection.rollback()
        finally:
            self.cursor.close()
            self.close()

    def GetPaises(self):
            self.open()
            listaPaises = []
            try:
                self.cursor.execute("SELECT distinct nacionalidad FROM famosos where nacionalidad not "
                                    "like '%-%' and nacionalidad not like '%,%'", )
                for row in self.cursor.fetchall():
                    r = row.values()
                    listaPaises.append(r)
                return listaPaises
            except:
                print("excepcion ocurrida bro")
                self.connection.rollback()
            finally:
                self.cursor.close()
                self.close()

    def getAleatorio(self, not0:str):
        self.open()
        try:
            self.cursor.execute("SELECT * FROM just_in_time.famosos where "+not0+" !=0 order by rand() LIMIT 1")
            return Famous(*self.cursor.fetchone().values())
        except:
            print("Error al recuperar famoso")
        finally:
            self.cursor.close()
            self.close()

