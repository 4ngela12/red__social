# negocio/publicaciones.py
from datetime import datetime
# Importación diferida para evitar bucle circular
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .comentario import Comentario


class Publicacion:
    def __init__(self, contenido: str, usuario):
        self.id = None
        self.contenido = contenido
        self.fecha = datetime.now()
        self.usuario = usuario
        self.likes = []
        self.comentarios = []
        self.tipo = "texto"

    def agregar_comentario(self, usuario, texto: str):
        from .comentario import Comentario   # 👈 Import local
        comentario = Comentario(usuario, self, texto)
        self.comentarios.append(comentario)
        return comentario


    def contar_likes(self):
        return len(self.likes)

    def eliminar_publicacion(self):
        print(f"Publicación '{self.contenido[:20]}...' eliminada")

    def __str__(self):
        return f"Publicación de {self.usuario.nombre}: {self.contenido}"
