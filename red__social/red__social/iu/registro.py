# iu/registro.py
"""
Módulo: registro
Permite registrar nuevos usuarios en la red social.
"""

from datos import base_datos as db

def registrar_usuario():
    print("=== Registro de nuevo usuario ===")
    nombre = input("Nombre: ").strip()
    correo = input("Correo electrónico: ").strip()
    password = input("Contraseña: ").strip()

    # Validar si el correo ya está registrado
    existente = db.buscar_usuario_por_correo(correo)
    if existente:
        print(" Ya existe un usuario con ese correo.")
        return None

    # Crear y guardar nuevo usuario
    nuevo_usuario = db.agregar_usuario(nombre, correo, password)
    print(f" Usuario {nuevo_usuario.nombre} registrado con éxito.\n")
    return nuevo_usuario
