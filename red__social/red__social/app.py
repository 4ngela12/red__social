# app.py
import sys
import os
sys.path.append(os.path.dirname(__file__))

from negocio.usuario import Usuario


if __name__ == "__main__":
    # Crear usuarios
    ana = Usuario("Ana", "ana@mail.com", "1234")
    pedro = Usuario("Pedro", "pedro@mail.com", "abcd")

    # Publicación
    pub = ana.crear_publicacion("¡Hola a todos!")
    pedro.dar_like(pub)
    pedro.comentar(pub, "¡Qué buena publicación!")

    # Amistad
    ana.agregar_amigo(pedro)

    # Mensaje
    ana.enviar_mensaje(pedro, "¿Cómo estás?")

    # Mostrar resultados
    print(pub)
    print(f"Likes: {pub.contar_likes()}")
    for c in pub.comentarios:
        print(c)



from datos import base_datos as db

if __name__ == "__main__":
    # Crear usuarios
    ana = db.agregar_usuario("Ana", "ana@mail.com", "1234")
    pedro = db.agregar_usuario("Pedro", "pedro@mail.com", "abcd")

    # Publicación
    pub = db.agregar_publicacion(ana, "¡Hola a todos!")
    db.agregar_like(pedro, pub)
    db.agregar_comentario(pedro, pub, "¡Qué buena publicación!")

    # Amistad y mensaje
    db.agregar_amistad(ana, pedro)
    db.enviar_mensaje(ana, pedro, "¿Cómo estás?")

    # Mostrar resumen de la base de datos
    db.mostrar_resumen()


# app.py
from iu import registro, login
from datos import base_datos as db

def menu_inicio():
    while True:
        print("=== RED SOCIAL ===")
        print("1. Registrarse")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registro.registrar_usuario()
        elif opcion == "2":
            usuario = login.iniciar_sesion()
            if usuario:
                menu_usuario(usuario)
        elif opcion == "3":
            print(" Saliendo del sistema...")
            break
        else:
            print("Opción inválida.\n")

def menu_usuario(usuario):
    print(f"=== Menú de {usuario.nombre} ===")
    print("1. Crear publicación")
    print("2. Ver resumen de base de datos")
    print("3. Cerrar sesión")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        contenido = input("Escribe tu publicación: ")
        db.agregar_publicacion(usuario, contenido)
        print(" Publicación creada.\n")
    elif opcion == "2":
        db.mostrar_resumen()
    elif opcion == "3":
        print(" Cerrando sesión...")
        return
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    menu_inicio()
