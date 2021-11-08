from Base_de_datos.dataPregunta import PreguntaData
from Base_de_datos.dataFamoso import FamosoData
from entities.models import Question, Famous
from bussiness import famosos_logic
import operator
from datetime import date,datetime
from typing import List
import random


class PreguntasLogic:
    def __init__(self):
        self.datasource = PreguntaData()

    def getRandomQuestion(self) -> [Question]:
        idpreg= random.randint(1,9)
        preg = self.datasource.GetOne(idpreg)

        return preg

    def armarPregunta(self, preg: Question, fam: str):
        if (preg.idPregunta < 8):
            pregArmada = preg.descripcion.replace('xxx',fam)
            return pregArmada
        else:
            pregArmada = preg.descripcion
            return pregArmada

    def elegirOpciones(self,preg: Question, fam: Famous):
        if (fam.nombreCompleto == "0"):
            return 0
        elif (preg.idPregunta == 2):
            if (fam.nacionalidad == 0):
                return 0
            else:
                resp_correcta = fam.nacionalidad
                resp_incorrectas = []
                f = FamosoData()
                for i in range(3):
                    resp_incorrectas.append(random.choice(f.GetPaises()))
                return resp_correcta, resp_incorrectas
        elif (preg.idPregunta == 5):
            if (fam.peso == 0):
                return 0
            else:
                resp_correcta = fam.peso
                resp_incorrectas = []
                for i in range(3):
                    ops = {'+': operator.add,
                           '-': operator.sub}
                    num1 = random.randint(0, 20)
                    op = random.choice(list(ops.keys()))
                    incorrecta = ops.get(op)(resp_correcta, num1)
                    resp_incorrectas.append(incorrecta)
                return resp_correcta,resp_incorrectas
        elif (preg.idPregunta == 4):
            if (fam.altura == 0):
                return 0
            else:
                resp_correcta = fam.altura
                resp_incorrectas = []
                for i in range(3):
                    ops = {'+': operator.add,
                           '-': operator.sub}
                    num1 = round(random.uniform(0.00,0.25),2)
                    op = random.choice(list(ops.keys()))
                    incorrecta = ops.get(op)(resp_correcta, num1)
                    resp_incorrectas.append(incorrecta)
                return resp_correcta, resp_incorrectas

p = PreguntasLogic()
j = famosos_logic.FamousLogic()
y = p.getRandomQuestion()
print(y)
k = j.getRandomFamous()
print(p.armarPregunta(y, k.nombreCompleto))
print(p.elegirOpciones(y, k))

"""    def armarPregunta(self, preg: Question, fam: Famous):
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
"""





