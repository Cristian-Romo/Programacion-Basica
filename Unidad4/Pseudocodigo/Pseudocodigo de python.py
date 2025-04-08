import random

def menu_riego():
    opcion = 0
    while opcion != 4:
        print("---- MENÚ ----")
        print("1. Medir humedad")
        print("2. Abrir llave")
        print("3. Cerrar llave")
        print("4. Salir")

        opcion = int(input("Elija una opción: "))
        
        if opcion == 1:
            humedad = random.randint(10, 100)
            print(f"Humedad actual: {humedad}%")
            
            if humedad < 40:
                print("Humedad baja. Activando riego.")
            else:
                print("Humedad suficiente. No se activa riego.")
        if opcion == 2:
            print("Abriendo llave de manera manual.")
        if opcion == 3:
            print("Cerrando llave de manera manual.")
        if opcion == 4:
            print("Saliendo del programa.")
        if opcion > 4:
            print("Error, seleccione otra opcion.")

menu_riego()