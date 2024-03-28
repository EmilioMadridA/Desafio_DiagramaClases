# Importar clases externas
from listado_respuestas import ListadoRespuestas

class Usuario:
    def __init__(self, correo: str, edad: int, region: str):
        self.correo = correo
        self.edad = edad
        self.region = region
    
    @property
    def correo(self):
        return self._correo

    @property
    def edad(self):
        return self._edad
    
    @property
    def region(self):
        return self._region


    def contestar_encuesta(self, encuesta):
        listado_respuestas = ListadoRespuestas(self, encuesta)

        # Ciclo for para responder preguntas
        for pregunta in encuesta.preguntas:
            respuesta = input("Ingrese su respuesta: \n")
            listado_respuestas.append(pregunta.enunciado, respuesta)

        encuesta.agregar_listado_respuestas(listado_respuestas)
        print("Encuesta contestada.")