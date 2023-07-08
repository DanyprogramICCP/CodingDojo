from usuario import Usuario

# Lista de usuarios registrados
usuarios = []

while True:
    print("----- Menú Principal -----")
    print("1. Crear usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        nuevo_usuario = Usuario(nombre_usuario)
        usuarios.append(nuevo_usuario)
        print("Usuario creado exitosamente.")

    elif opcion == "2":
        nombre_usuario = input("Ingrese el nombre de usuario: ")
        usuario_encontrado = None
        for usuario in usuarios:
            if usuario.nombre == nombre_usuario:
                usuario_encontrado = usuario
                break

        if usuario_encontrado:
            while True:
                print(f"----- Sesión de {usuario_encontrado.nombre} -----")
                print("1. Agregar cuenta")
                print("2. Mostrar saldos")
                print("3. Realizar transferencia")
                print("4. Cerrar sesión")

                opcion_usuario = input("Ingrese una opción: ")

                if opcion_usuario == "1":
                    usuario_encontrado.agregar_cuenta()

                elif opcion_usuario == "2":
                    usuario_encontrado.mostrar_saldos()
                    subopcion = input("Presione 1 para volver al menú principal o 2 para salir: ")
                    if subopcion == "2":
                        break

                elif opcion_usuario == "3":
                    usuario_encontrado.realizar_transferencia()

                elif opcion_usuario == "4":
                    print("Cerrando sesión...")
                    break

                else:
                    print("Opción inválida.")

        else:
            print("Usuario no encontrado.")

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida.")
