def mostrar_menu():
    print("=== MENÚ DE GESTIÓN DE PRODUCTOS ===")
    print("1. Mostrar productos")
    print("2. Agregar producto")
    print("3. Actualizar producto")
    print("4. Eliminar producto")
    print("5. Salir")

def mostrar_productos(productos):
    print("=== LISTA DE PRODUCTOS ===")
    if len(productos) > 0:
        for producto in productos:
            print(f"Código: {producto['codigo']}")
            print(f"Nombre: {producto['nombre']}")
            print(f"Precio: {producto['precio']}")
            print("--------------------")
    else:
        print("No hay productos registrados.")

def agregar_producto(productos):
    print("=== AGREGAR PRODUCTO ===")
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos.append({"codigo": codigo, "nombre": nombre, "precio": precio})
    print("Producto agregado exitosamente.")

def actualizar_producto(productos):
    print("=== ACTUALIZAR PRODUCTO ===")
    codigo = input("Ingrese el código del producto a actualizar: ")
    for producto in productos:
        if producto["codigo"] == codigo:
            nombre = input("Ingrese el nuevo nombre del producto: ")
            precio = float(input("Ingrese el nuevo precio del producto: "))
            producto["nombre"] = nombre
            producto["precio"] = precio
            print("Producto actualizado exitosamente.")
            return
    print("No se encontró un producto con ese código.")

def eliminar_producto(productos):
    print("=== ELIMINAR PRODUCTO ===")
    codigo = input("Ingrese el código del producto a eliminar: ")
    for producto in productos:
        if producto["codigo"] == codigo:
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            return
    print("No se encontró un producto con ese código.")

# Función principal del programa
def main():
    productos = []
    while True:
        mostrar_menu()
        opcion = input("Ingrese la opción deseada: ")
        if opcion == "1":
            mostrar_productos(productos)
        elif opcion == "2":
            agregar_producto(productos)
        elif opcion == "3":
            actualizar_producto(productos)
        elif opcion == "4":
            eliminar_producto(productos)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, intente nuevamente.")

# Ejecutar la función principal
main()