from Base_de_datos.dataFamoso import FamosoData
from entities.models import Famous
import random


class FamousLogic:
    def __init__(self):
        self.datasource = FamosoData()

    def getRandomFamous(self) -> [Famous]:
        idfam = random.randint(1,1508)
        fam = self.datasource.GetOne(idfam)
        return fam

f = FamousLogic()
print(f.getRandomFamous())
