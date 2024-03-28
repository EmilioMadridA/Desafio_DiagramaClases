# Importacion de clases externas
from alternativa import Alternativa

class Pregunta:
    def __init__(self, enunciado: str, requerida=False, alternativas=[]):
        self.enunciado = enunciado
        self.requerida = requerida
        self.alternativas = [Alternativa(**alt) for alt in alternativas]
    
    @property
    def enunciado(self):
        return self.enunciado

    @enunciado.setter
    def enunciado(self, nuevo_enunciado):
        self._enunciado = nuevo_enunciado
    
    @property
    def requerida(self):
        return self.requerida

    @es_requerida.setter
    def requerida(self, requerida):
        self.requerida = requerida
    
    @property
    def alternativas(self):
        return self._alternativas

    def mostrar(self):
        print(f"Enunciado: {self.enunciado}")
        if self.requerida:
            print("Esta pregunta es requerida.")
        for alternativa in self.alternativas:
            alternativa.mostrar()