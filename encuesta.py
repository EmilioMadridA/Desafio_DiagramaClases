# Importacion de clases externas
from pregunta import Pregunta
from listado_respuestas import ListadoRespuestas

class Encuesta:
    """
    Clase que representa una encuesta con un conjunto de preguntas.
    """
    def __init__(self, nombre: str, preguntas: list):
        """ Metodo que inicializa una instancia de Encuesta.

        Args:
            nombre (str): Nombre de la encuesta.
            preguntas (list): Listas de diccionarios de preguntas.
        """
        self.nombre = nombre
        self.preguntas = [Pregunta(**pregunta) for pregunta in preguntas]
        self.listados_respuestas = []
    
    @property
    def nombre(self):
        """ Metodo de retorno del nombre de la encuesta.

        Returns:
            str: Retorna el nombre de la encuesta.
        """
        return self.nombre
    
    @property
    def preguntas(self):
        """ Metodo de retorno de las preguntas de la encuesta.

        Returns:
            list: Listado de las preguntas.
        """
        return self.preguntas
    
    @property
    def listados_respuestas(self):
        """ Metodo de retorno del listado de respuestas.

        Returns:
            list: Listado de las respuestas.
        """
        return self.listados_respuestas

    def mostrar(self):
        """ Metodo que imprime los detalles de la encuesta.
        """
        print(f"Encuesta: {self.nombre}")
        # Ciclo for para la impresión.
        for pregunta in self.preguntas:
            pregunta.mostrar()

    def agregar_listado_respuestas(self, listado):
        """ Metodo que añade un listado de respuestas a la encuesta.

        Args:
            listado (object): Listado de respuestas a agregar.
        """
        # Validación
        if isinstance(listado, ListadoRespuestas):
            self.listados_respuestas.append(listado)
        else:
            print("El listado debe ser una instancia de ListadoRespuestas")

class EncuestaLimitadaEdad(Encuesta):
    """ Subclase de Encuesta con restricciones por edad.

    Args:
        Encuesta (object): Clase de la que hereda Metodos y Atributos.
    """
    def __init__(self, nombre: str, edad_minima: int, edad_maxima: int):
        """ Metodo que inicializa una encuesta limitada por edad.

        Args:
            nombre (str): Nombre de la encuesta.
            edad_minima (int): Edad minima requerida.
            edad_maxima (int): Edad maxima requerida.
        """
        super().__init__(nombre)
        self.edad_minima = edad_minima
        self.edad_maxima = edad_maxima

    @property
    def edad_minima(self):
        """ Metodo de retorno de la edad minima requerida.

        Returns:
            int: Edad minima requerida.
        """
        return self.edad_minima

    @property
    def edad_maxima(self):
        """ Metodo de retorno de la edad máxima requerida.

        Returns:
            int: Edad máxima requerida.
        """
        return self.edad_maxima

class EncuestaLimitadaRegion(Encuesta):
    """ Subclase de Encuesta con restricciones por región.

    Args:
        Encuesta (object): Clase de la que hereda Metodos y Atributos.
    """
    def __init__(self, nombre: str, region: str):
        """ Metodo que inicializa una encuesta limitada por región.

        Args:
            nombre (str): Nombre de la encuesta.
            región (str): Cadena de texto correspondiente a la región requerida.
        """
        super().__init__(nombre)
        self.region = region

    @property
    def region(self):
        """ Metodo de retorno de la regiónrequerida.

        Returns:
            str: región requerida.
        """
        return self.region