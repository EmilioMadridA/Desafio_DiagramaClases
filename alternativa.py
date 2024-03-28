class Alternativa:
    def __init__(self, contenido: str, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda
    
    @property
    def contenido(self):
        return self.contenido

    @contenido.setter
    def contenido(self, nuevo_contenido):
        self.contenido = nuevo_contenido
    
    @property
    def ayuda(self):
        return self.ayuda
    
    @ayuda.setter
    def ayuda(self, nueva_ayuda):
        self._ayuda = nueva_ayuda
        
    def mostrar(self):
        print(f"Contenido: {self.contenido}")
        if self.ayuda:
            print(f"Ayuda: {self.ayuda}")