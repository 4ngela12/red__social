# negocio/amigos.py
from datetime import date

class Amigos:
    def __init__(self, usuario_1, usuario_2):
        self.id = None
        self.usuario_1 = usuario_1
        self.usuario_2 = usuario_2
        self.estado = "pendiente"  # pendiente, aceptada, bloqueada
        self.fecha_inicio = date.today()

    def aceptar_solicitud(self):
        self.estado = "aceptada"

    def eliminar_amigo(self):
        self.estado = "bloqueada"

    def __str__(self):
        return f"Amistad entre {self.usuario_1.nombre} y {self.usuario_2.nombre} ({self.estado})"
