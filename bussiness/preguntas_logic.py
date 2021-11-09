from Base_de_datos.dataFamoso import FamosoData
from entities.models import Question, Famous
from bussiness.famosos_logic import FamousLogic
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
        f = FamousLogic()
        if 'año' in preg:
            param='LENGTH(fnac)>10 and fnac'
        elif 'nacionalidad' in preg:
            param='length(nacionalidad)'
        elif 'fortuna' in preg:
            param='fortuna'
        elif 'mide' in preg:
            param='altura'
        elif 'pesa' in preg:
            param='peso'

        famcorrecto=f.getRandomFamous(param)
        while famcorrecto is None:
            famcorrecto=f.getRandomFamous(param)
        #se pregunta por edad o año nacimiento
        if 'año' in preg:
                if 'años' in preg:
                    ######################################################### reemplazar fecha nacimiento con edad
                    edad=datetime.today()-famcorrecto.fechaNacimiento
                    edad=int(edad.total_seconds()/60/60/24/365)
                    respCorrecta=edad
                    respIncorrectas=self.generadorAnios(edad,cantResp)
                else:
                    ######################################################### reemplazar fecha nacimiento con año nac..
                    YYnac=famcorrecto.fechaNacimiento.year
                    respCorrecta=YYnac
                    respIncorrectas=self.generadorAnios(YYnac,cantResp)

        elif 'fortuna' in preg:
            respCorrecta=famcorrecto.fortuna
            while(len(respIncorrectas))+1!=cantResp:
                factor=random.choice(range(1,9))
                r=factor*famcorrecto.fortuna
                if r not in respIncorrectas and r!=famcorrecto.fortuna:
                    respIncorrectas.append(r)

        elif 'mide' in preg or 'pesa' in preg:
            respCorrecta=famcorrecto.altura if 'mide' in preg else famcorrecto.peso
            while(len(respIncorrectas))+1!=cantResp:
                agregado=random.randint(-9,9)/random.choice([10,100])
                if 'mide' in preg:
                    if famcorrecto.altura+agregado in respIncorrectas:
                        continue
                    elif 1.40 <famcorrecto.altura+agregado < 2.25 and famcorrecto.altura+agregado!=respCorrecta:
                        respIncorrectas.append(famcorrecto.altura + agregado)
                else:
                    agregado*=10
                    if famcorrecto.peso + agregado in respIncorrectas:
                        continue
                    elif famcorrecto.peso+agregado!=respCorrecta:
                        respIncorrectas.append(famcorrecto.peso + agregado)

        #se pregunta por nacionalidad
        elif 'nacionalidad' in preg:
            respCorrecta=famcorrecto.nacionalidad
            for i in range(cantResp-1):
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
        while len(li)+1!=cant:
            año=yy+random.choice(range(-9,9))
            if año not in li and año!=yy:
                li.append(año)

        return li

"""
p = PreguntasLogic()
j = famosos_logic.FamousLogic()
y = p.getRandomQuestion()
print(y)
k = j.getRandomFamous()
print(p.armarPregunta(y, k.nombreCompleto))
print(p.elegirOpciones(y, k))
"""
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





