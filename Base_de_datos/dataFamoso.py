# aqui guardaremos el manejo de la tabla famoso de la base de datos
from typing import List
from .connection import DataBase
from entities.models import Famous
from dateutil import parser


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
                    r = list(row.values()).pop()
                    listaPaises.append(r)
                return listaPaises
            except:
                print("FamososData- Error al recuperar países")
                self.connection.rollback()
            finally:
                self.cursor.close()
                self.close()

    def getAleatorio(self, not0:str):
        self.open()
        try:
            query="""SELECT famosos.ID,famosos.altura, famosos.fnac, famosos.fortuna, famosos.img_name, famosos.nacionalidad, famosos.nombre, famosos.peso FROM just_in_time.famosos where """+not0+" !=0 order by rand() LIMIT 1"
            self.cursor.execute(query)
            f=[*self.cursor.fetchone().values()]
            try:
                fnac=parser.parse(f[2])
            except:
                fnac=0
            fam=Famous(f[0],f[1], fnac, f[3], f[4], f[5], f[6], f[7])
            return fam
        except:
            print("Error al recuperar famoso")
        finally:
            self.cursor.close()
            self.close()

