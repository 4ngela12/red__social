# negocio/like.py
from datetime import datetime

class Like:
    def __init__(self, usuario, publicacion):
        self.id = None
        self.usuario = usuario
        self.publicacion = publicacion
        self.fecha_hora = datetime.now()

    def anular_like(self):
        print(f"{self.usuario.nombre} quitó su 'Me gusta' en una publicación.")

    def __str__(self):
        return f"{self.usuario.nombre} dio 'Me gusta' a una publicación de {self.publicacion.usuario.nombre}"
