# iu/login.py
"""
Módulo: login
Permite iniciar sesión en la red social.
"""

from datos import base_datos as db

def iniciar_sesion():
    print("=== Iniciar sesión ===")
    correo = input("Correo: ").strip()
    password = input("Contraseña: ").strip()

    usuario = db.buscar_usuario_por_correo(correo)
    if usuario and usuario.password == password:
        print(f" Bienvenido, {usuario.nombre}!\n")
        return usuario
    else:
        print(" Correo o contraseña incorrectos.\n")
        return None
