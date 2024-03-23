# Importacion de clases externas
from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre: str, preguntas: dict):
        self.nombre = nombre
        self.preguntas = [Pregunta(**pregunta) for pregunta in preguntas]
        self.listados_respuestas = []

    def mostrar(self):
        print(f"Encuesta: {self.nombre}")
        for pregunta in self.preguntas:
            pregunta.mostrar()

    def agregar_listado_respuestas(self, listado):
        self.listados_respuestas.append(listado)

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int, preguntas: dict):
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, regiones: str, preguntas: dict):
        super().__init__(nombre)
        self.regiones = regiones