class Alternativa:
    def __init__(self, contenido: str, ayuda=None):
        self.contenido = contenido
        self.ayuda = ayuda
    
    def mostrar(self):
        info = self.contenido
        if self.ayuda:
            info += f" (Ayuda: {self.ayuda})"
        print(info)