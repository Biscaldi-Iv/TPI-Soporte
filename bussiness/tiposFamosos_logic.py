from Base_de_datos.dataTipoFamoso import TipoFamosoData
from entities.models import KindOfFamous
from typing import List


class KindOfFamousLogic:
    def __init__(self):
        self.datasource = TipoFamosoData()

    def all(self) -> List[KindOfFamous]:
        listaTipos = self.datasource.GetAll()
        return listaTipos