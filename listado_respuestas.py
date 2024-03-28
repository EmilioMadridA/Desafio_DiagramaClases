# Importacion de clases externas
from usuario import Usuario

class ListadoRespuestas:
    """
    Clase que debe almacenar las respuestas de un usuario a una encuesta específica.
    """
    def __init__(self, usuario: object, respuestas: list):
        """ Meotdo constructor de ListadoRespuestas.

        Args:
            usuario (object): Objetto del usuario que está dando las respuestas.
            respuestas (list): Listado de respuestas proporcionadas por el usuario.
        """
        self.usuario = usuario
        self.respuestas = respuestas