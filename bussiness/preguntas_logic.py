from Base_de_datos.dataPregunta import PreguntaData
from entities.models import Question, KindOfFamous, Famous
from typing import List
import famosos_logic
import random


class PreguntasLogic:
    def __init__(self):
        self.datasource = PreguntaData()

    def all(self, tipoFamoso: KindOfFamous) -> List[Question]:
        listaPreguntas = self.datasource.getPreguntaXTipoF(tipoFamoso)
        return listaPreguntas

    def getRandomQuestion(self,tipoFamoso: KindOfFamous) -> [Question]:
        listaPreguntas=self.all(tipoFamoso)
        preg= random.choice(listaPreguntas)
        return preg

    def armarPregunta(self, preg: Question, fam:Famous):
        preguntaArmada = preg.descripcion + " " + fam.nombreCompleto + " ?"
        return preguntaArmada

    def devolverPregunta(self, tipoFamoso: KindOfFamous):
        preg = self.getRandomQuestion(tipoFamoso)
        fam = famosos_logic.UserLogic.getRandomFamous(tipoFamoso)
        return self.armarPregunta(preg,fam)






