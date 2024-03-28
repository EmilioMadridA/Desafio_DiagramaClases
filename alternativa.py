class Alternativa:
    """ Clase que representa una alternativa dentro de una pregunta de una encuesta.
    """
    def __init__(self, contenido: str, ayuda=None):
        """ Metodo que inicializa una nueva instancia de Alternativa.

        Args:
            contenido (str): Cadena de texto del contenido de la alternativa.
            ayuda (str, optional): Cadena de texto de ayuda para la alternativa. Defaults to None.
        """
        self.contenido = contenido
        self.ayuda = ayuda
    
    @property
    def contenido(self):
        """ Metodo que retorna el contenido de la alternativa

        Returns:
            str: Contenido de la alternativa.
        """
        return self.contenido
    
    @property
    def ayuda(self):
        """ Metodo que retorna el texto de la ayuda.

        Returns:
            str: Texto de ayuda.
        """
        return self.ayuda
        
    def mostrar(self):
        """
        Metodo de impresión del contenido y ayuda de la alternativa.
        """
        print(f"Contenido: {self.contenido}")
        # Validacion de ayuda disponible.
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")