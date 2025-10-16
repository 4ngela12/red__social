# negocio/usuario.py
from datetime import date
from .publicaciones import Publicacion
from .like import Like
from .mensaje import Mensaje
from .amigos import Amigos

class Usuario:
    def __init__(self, nombre: str, correo: str, password: str):
        self.id = None  # se asignará automáticamente
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.fecha_registro = date.today()
        self.estado = "activo"
        self.publicaciones = []
        self.amigos = []
        self.mensajes = []

    def crear_publicacion(self, contenido: str):
        publicacion = Publicacion(contenido, self)
        self.publicaciones.append(publicacion)
        return publicacion

    def dar_like(self, publicacion):
        like = Like(self, publicacion)
        publicacion.likes.append(like)
        return like

    def comentar(self, publicacion, texto: str):
        return publicacion.agregar_comentario(self, texto)

    def enviar_mensaje(self, receptor, contenido: str):
        mensaje = Mensaje(self, receptor, contenido)
        self.mensajes.append(mensaje)
        receptor.mensajes.append(mensaje)
        return mensaje

    def agregar_amigo(self, otro_usuario):
        amistad = Amigos(self, otro_usuario)
        self.amigos.append(amistad)
        otro_usuario.amigos.append(amistad)
        return amistad

    def __str__(self):
        return f"Usuario({self.nombre}, {self.correo})"
