# Importacion de clases externas
from usuario import Usuario

class ListadoRespuestas:
    def __init__(self, usuario: object, respuestas: list):
        self.usuario = usuario
        self.respuestas = respuestas