# negocio/comentario.py
from datetime import datetime

class Comentario:
    def __init__(self, usuario, publicacion, texto: str):
        self.id = None
        self.usuario = usuario
        self.publicacion = publicacion
        self.texto = texto
        self.fecha_hora = datetime.now()

    def editar_comentario(self, nuevo_texto: str):
        self.texto = nuevo_texto

    def __str__(self):
        return f"{self.usuario.nombre} comentó: {self.texto}"

