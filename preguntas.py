# Importacion de clases externas
from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, ayuda=None, requerida=False, alternativas=None):
        self.enunciado = enunciado
        self.ayuda = ayuda
        self.requerida = requerida
        self.alternativas = alternativas
    
    def mostrar(self):
        print(self.enunciado)
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")
        for alt in self.alternativas:
            alt.mostrar()