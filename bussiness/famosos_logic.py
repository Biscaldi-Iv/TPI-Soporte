from Base_de_datos.dataFamoso import FamosoData
from entities.models import Famous,KindOfFamous
from typing import List
import random


class UserLogic:
    def __init__(self):
        self.datasource = FamosoData()

    def all(self, tipoFamoso: KindOfFamous) -> List[Famous]:
        listaFamosos = self.datasource.getFamosoXTipoF(tipoFamoso)
        return listaFamosos

    def getRandomFamous(self, tipoFamosos: KindOfFamous) -> [Famous]:
        listaFamosos = self.all(tipoFamosos)
        fam= random.choice(listaFamosos)
        return fam
