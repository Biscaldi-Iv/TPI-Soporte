from Base_de_datos.dataFamoso import FamosoData
from entities.models import Famous
import random


class FamousLogic:
    def __init__(self):
        self.datasource = FamosoData()

    def getRandomFamous(self, not0) -> [Famous]:
        fam = self.datasource.getAleatorio(not0)
        return fam

f = FamousLogic()
print(f.getRandomFamous())
