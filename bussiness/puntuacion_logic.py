from Base_de_datos.dataPuntuacion import PuntuacionData
from entities.models import Score

class PuntuacionLogic():
    def __init__(self):
        self.p=PuntuacionData()

    def register(self, puntuacion: Score):
        guarda = self.p.register(puntuacion)
        if guarda:
            return
        raise Exception("no se pudo registrar la puntuacion")

    def myTop(self, username):
        listapuntuaciones = list()
        try:
            listapuntuaciones= self.p.myTop(username)
        except:
            pass
        return listapuntuaciones

    def top10(self):
        listapuntuaciones = list()
        try:
            listapuntuaciones = self.p.top10()
        except:
            pass
        return listapuntuaciones




