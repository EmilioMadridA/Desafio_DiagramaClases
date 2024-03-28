# Importar clases externas
from listado_respuestas import ListadoRespuestas

class Usuario:
    """
    Clase que representa a un usuario.
    """
    def __init__(self, correo: str, edad: int, region: str):
        """ Metodo que inicializa una nueva instancia de Usuario.

        Args:
            correo (str): Cadena de texto correspondiente al correo electrónico del usuario.
            edad (int): Edad del usuario.
            region (str): Cadena de texto correspondiente a la región del usuario.
        """
        self.correo = correo
        self.edad = edad
        self.region = region
    
    @property
    def correo(self) -> str:
        """ Metodo de retorno del correo electrónico del usuario.

        Returns:
            str: Retorna el correo del usuario.
        """
        return self._correo

    @property
    def edad(self) -> int:
        """ Metodo de retorno de la edad del usuario.

        Returns:
            int: Retorna la edad del usuario.
        """
        return self._edad
    
    @property
    def region(self) -> str:
        """ Metodo de retorno de la región del usuario.

        Returns:
            str: Retorna la region del usuario.
        """
        return self._region


    def contestar_encuesta(self, encuesta):
        """ Metodo que permite al usuario contestar una encuesta.

        Args:
            encuesta (object): Instancia de clase Encuensta
        """

        listado_respuestas = ListadoRespuestas(self, [])

        # Ciclo for para responder preguntas
        for pregunta in encuesta.preguntas:
            respuesta = input(f"{pregunta.enunciado}.\n Ingrese su respuesta: \n")
            listado_respuestas.respuestas.append(pregunta, respuesta)

        encuesta.agregar_listado_respuestas(listado_respuestas)
        print("Muchas gracias por contestar la encuesta.")