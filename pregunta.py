# Importacion de clases externas
from alternativa import Alternativa

class Pregunta:
    """ Clase que representa una pregunta.
    """
    def __init__(self, enunciado: str, requerida=False, alternativas=[]):
        """ Metodo que inicializa una nueva instancia de Pregunta.

        Args:
            enunciado (str): Cadena de texto del enunciado de la pregunta.
            requerida (bool, optional): Bool que Indica si la respuesta a la pregunta es obligatoria. Defaults to False.
            alternativas (list, optional): Listado de objetos Alternativa asociados a la pregunta. Defaults to [].
        """
        self.enunciado = enunciado
        self.requerida = requerida
        self.alternativas = [Alternativa(**alt) for alt in alternativas]
    
    @property
    def enunciado(self):
        """ Metodo de retorno del enunciado de la pregunta.

        Returns:
            str: Retorna el enunciado.
        """
        return self.enunciado
    
    @property
    def requerida(self):
        """ Metodo que retorna si la pregunta es requerida o no.

        Returns:
            bool: True o False dependiendo del caso.
        """
        return self.requerida

    @es_requerida.setter
    def requerida(self, requerida):
        """ Metodo que establece si la pregunta es requerida

        Args:
            requerida (bool): Nuevo estado que determina si la pregunta es requerida o no.
        """
        self.requerida = requerida
    
    @property
    def alternativas(self):
        """ Metodo que retorna la lista de alternativas de la pregunta.

        Returns:
            list: Listado de las alternativas
        """
        return self._alternativas

    def mostrar(self):
        """ Metodo de impresión de los detalles de la pregunta.
        """
        print(f"Enunciado: {self.enunciado}")
        # Validacion de requerimiento de pregunta
        if self.requerida:
            print("Esta pregunta es requerida.")
        # Alternativas
        for alternativa in self.alternativas:
            alternativa.mostrar()