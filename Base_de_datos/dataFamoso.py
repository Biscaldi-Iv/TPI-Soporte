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

p = FamosoData()
print(p.GetPaises())