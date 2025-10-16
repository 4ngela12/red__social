# negocio/mensajes.py

from datetime import datetime

class Mensaje:
    def __init__(self, emisor, receptor, contenido: str):
        self.id = None
        self.contenido = contenido
        self.fecha_hora = datetime.now()
        self.emisor = emisor
        self.receptor = receptor
        self.leido = False

    def marcar_como_leido(self):
        self.leido = True

    def eliminar_mensaje(self):
        print(f"Mensaje eliminado: {self.contenido[:20]}...")

    def __str__(self):
        estado = "leído" if self.leido else "no leído"
        return f"De {self.emisor.nombre} a {self.receptor.nombre}: {self.contenido} ({estado})"
