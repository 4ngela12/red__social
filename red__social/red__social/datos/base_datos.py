# datos/base_datos.py
"""
Módulo: base_datos
Simula una base de datos en memoria para la red social.
Permite registrar, buscar y listar usuarios, publicaciones y otras entidades.
"""

from negocio.usuario import Usuario
from negocio.publicaciones import Publicacion
from negocio.like import Like
from negocio.comentario import Comentario
from negocio.amigos import Amigos
from negocio.mensaje import Mensaje


# ----- Listas globales -----
usuarios = []
publicaciones = []
likes = []
comentarios = []
amistades = []
mensajes = []


# ----- Funciones para usuarios -----
def agregar_usuario(nombre, correo, password):
    usuario = Usuario(nombre, correo, password)
    usuario.id = len(usuarios) + 1
    usuarios.append(usuario)
    return usuario


def buscar_usuario_por_correo(correo):
    for u in usuarios:
        if u.correo == correo:
            return u
    return None


def listar_usuarios():
    return usuarios


# ----- Funciones para publicaciones -----
def agregar_publicacion(usuario, contenido):
    publicacion = usuario.crear_publicacion(contenido)
    publicacion.id = len(publicaciones) + 1
    publicaciones.append(publicacion)
    return publicacion


def listar_publicaciones():
    return publicaciones


# ----- Funciones para likes -----
def agregar_like(usuario, publicacion):
    like = usuario.dar_like(publicacion)
    like.id = len(likes) + 1
    likes.append(like)
    return like


# ----- Funciones para comentarios -----
def agregar_comentario(usuario, publicacion, texto):
    comentario = usuario.comentar(publicacion, texto)
    comentario.id = len(comentarios) + 1
    comentarios.append(comentario)
    return comentario


# ----- Funciones para amistades -----
def agregar_amistad(usuario1, usuario2):
    amistad = usuario1.agregar_amigo(usuario2)
    amistad.id = len(amistades) + 1
    amistades.append(amistad)
    return amistad


# ----- Funciones para mensajes -----
def enviar_mensaje(emisor, receptor, contenido):
    mensaje = emisor.enviar_mensaje(receptor, contenido)
    mensaje.id = len(mensajes) + 1
    mensajes.append(mensaje)
    return mensaje


# ----- Función general de resumen -----
def mostrar_resumen():
    print("=== Estado actual de la base de datos ===")
    print(f"Usuarios: {len(usuarios)}")
    print(f"Publicaciones: {len(publicaciones)}")
    print(f"Comentarios: {len(comentarios)}")
    print(f"Likes: {len(likes)}")
    print(f"Amistades: {len(amistades)}")
    print(f"Mensajes: {len(mensajes)}")
    print("=========================================")
