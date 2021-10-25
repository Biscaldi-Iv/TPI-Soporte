from Base_de_datos.dataPregunta import PreguntaData
from entities.models import Question, KindOfFamous, Famous
from typing import List
import famosos_logic,tiposFamosos_logic
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

    def devolverPregunta(self):
        #creo lista de todos los tipos de famosos
        listaTipoFamosos=tiposFamosos_logic.KindOfFamousLogic.all()

        #elijo aleatoriamente un tipo de famoso
        tipoFamoso = random.choice(listaTipoFamosos)

        #selecciono una pregunta para ese tipo de famoso
        preg = self.getRandomQuestion(tipoFamoso)

        #selecciono tambien un famoso acorde a ese tipo de famoso
        fam = famosos_logic.FamousLogic.getRandomFamous(tipoFamoso)

        #devuelvo la pregunta armada con el famoso y la pregunta seleccionada
        return self.armarPregunta(preg,fam)






