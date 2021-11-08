from Base_de_datos.dataFamoso import FamosoData
from entities.models import Question, Famous
from bussiness import famosos_logic
import operator
from datetime import date,datetime
from typing import List
from dateutil import parser
import random


class PreguntasLogic:
    def __init__(self):
        self.listaPreguntas=['¿Cuantos años tiene xxx',
                             '¿De que nacionalidad es xxx',
                             '¿Cual es la fortuna de xxx',
                             '¿Cuantos metros mide xxx',
                             '¿Cuantos kilogramos pesa xxx',
                             '¿En que año nacio xxx',]

    def getRandomQuestion(self, cantResp:int) -> [Question]:
        """:returns:[pregunta,respuesta_correcta, respuestas_incorrectas:List()"""
        respIncorrectas=list()
        idpreg= random.randint(0,len(self.listaPreguntas)-1)
        preg = self.listaPreguntas[idpreg]
        f = famosos_logic.FamousLogic()
        if 'año' in preg:
            param='fnac'
        elif 'nacionalidad' in preg:
            param='nacionalidad'
        elif 'fortuna' in preg:
            param='fortuna'
        elif 'mide' in preg:
            param='altura'
        elif 'pesa' in preg:
            param='peso'
        famcorrecto=f.getRandomFamous(param)

        #se pregunta por edad o año nacimiento
        if 'año' in preg:
                if 'años' in preg:
                    ######################################################### reemplazar fecha nacimiento con edad
                    edad=datetime.today()-parser.parse(famcorrecto.fechaNacimiento)
                    edad=int(edad.total_seconds()/60/60/24/365)
                    respCorrecta=edad
                    respIncorrectas.append(*self.generadorAnios(edad,cantResp-1))
                else:
                    ######################################################### reemplazar fecha nacimiento con año nac..
                    YYnac=parser.parse(famcorrecto.fechaNacimiento).year
                    respCorrecta=YYnac
                    respIncorrectas.append(*self.generadorAnios(YYnac,cantResp-1))

        elif 'fortuna' in preg:
            respCorrecta=famcorrecto.fortuna
            for i in range(cantResp):
                factor=random.choice(range(-i,i))
                respIncorrectas.append(factor*famcorrecto.fortuna)

        elif 'mide' in preg or 'pesa' in preg:
            respCorrecta=famcorrecto.altura if 'mide' in preg else famcorrecto.peso
            for i in range(cantResp):
                agregado=random.randint(-i,i)/random.choice([10,100])
                if 'mide' in preg:
                    respIncorrectas.append(famcorrecto.altura+agregado)
                else:
                    agregado*=10
                    respIncorrectas.append(famcorrecto.peso+agregado)

        #se pregunta por nacionalidad
        elif 'nacionalidad' in preg:
            respCorrecta=famcorrecto.nacionalidad
            for i in range(cantResp - 1):
                r= random.choice(f.GetPaises())
                if r in respIncorrectas or r==famcorrecto.nacionalidad:
                    while r in respIncorrectas or r==famcorrecto.nacionalidad:
                        r=random.choice(f.GetPaises())
                respIncorrectas.append(r)

        preg=self.armarPregunta(preg, famcorrecto.nombreCompleto)

        return preg, respCorrecta, respIncorrectas


    def armarPregunta(self, preg: str, fam: str):
        pregArmada = preg.replace('xxx',fam)
        return pregArmada

    """def elegirOpciones(self,preg: Question, fam: Famous):
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
                return resp_correcta, resp_incorrectas"""

    def generadorAnios(self, yy, cant):
        li=list()
        for i in range(cant):
            factor = random.choice([1, -1])
            r = (factor * i) + yy
            li.append(r)
        return li


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





