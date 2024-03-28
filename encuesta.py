# Importacion de clases externas
from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    def __init__(self, nombre: str, preguntas: dict):
        self.nombre = nombre
        self.preguntas = [Pregunta(**pregunta) for pregunta in preguntas]
        self.listados_respuestas = []
    
    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self, nombre_nuevo) -> str:
        self.nombre = nombre_nuevo
    
    @property
    def preguntas(self):
        return self.preguntas
    
    @property
    def listados_respuestas(self):
        return self.listados_respuestas

    

    def mostrar(self):
        print(f"Encuesta: {self.nombre}")
        for pregunta in self.preguntas:
            pregunta.mostrar()

    def agregar_listado_respuestas(self, listado):
        if isinstance(listado, ListadoRespuestas):
            self.listados_respuestas.append(listado)
        else:
            print("El listado debe ser una instancia de ListadoRespuestas")

class EncuestaLimitadaEdad(Encuesta):
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int):
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    @property
    def edad_minima(self):
        return self.edad_minima

    @property
    def edad_maxima(self):
        return self.edad_maxima

class EncuestaLimitadaRegion(Encuesta):
    def __init__(self, nombre: str, regiones: str):
        super().__init__(nombre)
        self.regiones = regiones

    @property
    def regiones(self):
        return self._regiones