import datetime
import random

# Diccionarios para almacenar empleados y productos
empleados = {}
productos = {}

# Función para imprimir el menú
def imprimir_menu():
    print("\n--- Menú de Gestión de Empresa ---")
    print("1. Agregar Empleado")
    print("2. Eliminar Empleado")
    print("3. Imprimir Lista de Empleados")
    print("4. Agregar Producto")
    print("5. Eliminar Producto")
    print("6. Imprimir Lista de Productos")
    print("7. Salir")

# Función para agregar un empleado
def agregar_empleado():
    id_empleado = random.randint(1000, 9999)
    nombre = input("Ingrese el nombre del empleado: ")
    puesto = input("Ingrese el puesto del empleado: ")
    fecha_contratacion = datetime.datetime.now().strftime("%Y-%m-%d")
    empleados[id_empleado] = {"Nombre": nombre, "Puesto": puesto, "Fecha de Contratación": fecha_contratacion}
    print(f"Empleado {nombre} agregado con ID {id_empleado}.")

# Función para eliminar un empleado
def eliminar_empleado():
    id_empleado = int(input("Ingrese el ID del empleado a eliminar: "))
    if id_empleado in empleados:
        empleado_eliminado = empleados.pop(id_empleado)
        print(f"Empleado {empleado_eliminado['Nombre']} eliminado.")
    else:
        print("Empleado no encontrado.")

# Función para imprimir la lista de empleados
def imprimir_empleados():
    if empleados:
        print("\n--- Lista de Empleados ---")
        for id_empleado, info in empleados.items():
            print(f"ID: {id_empleado}, Nombre: {info['Nombre']}, Puesto: {info['Puesto']}, Fecha de Contratación: {info['Fecha de Contratación']}")
    else:
        print("No hay empleados registrados.")

# Función para agregar un producto
def agregar_producto():
    id_producto = random.randint(1000, 9999)
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos[id_producto] = {"Nombre": nombre, "Precio": precio}
    print(f"Producto {nombre} agregado con ID {id_producto}.")

# Función para eliminar un producto
def eliminar_producto():
    id_producto = int(input("Ingrese el ID del producto a eliminar: "))
    if id_producto in productos:
        producto_eliminado = productos.pop(id_producto)
        print(f"Producto {producto_eliminado['Nombre']} eliminado.")
    else:
        print("Producto no encontrado.")

# Función para imprimir la lista de productos
def imprimir_productos():
    if productos:
        print("\n--- Lista de Productos ---")
        for id_producto, info in productos.items():
            print(f"ID: {id_producto}, Nombre: {info['Nombre']}, Precio: ${info['Precio']:.2f}")
    else:
        print("No hay productos registrados.")

# Programa principal
def main():
    while True:
        imprimir_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_empleado()
        elif opcion == "2":
            eliminar_empleado()
        elif opcion == "3":
            imprimir_empleados()
        elif opcion == "4":
            agregar_producto()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            imprimir_productos()
        elif opcion == "7":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Por favor seleccione una opción del 1 al 7.")

if __name__ == "__main__":
    main()