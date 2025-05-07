# Checador de flujo de agua

def obtener_estado_sensor():
    sensor_activado = True  # Simulación de datos del sensor
    return sensor_activado

while True:
    print("\nBienvenido vamos a verificar si está fluyendo agua.")
    
    estado_sensor = obtener_estado_sensor()
    
    if estado_sensor:
        print("En este momento está fluyendo agua por la manguera.")
    else:
        print("No está fluyendo agua por la manguera.")
    
    respuesta = input("Quieres revisar nuevamente? (si/no): ").strip().lower()
    if respuesta != "si":
        print("Saliendo del programa")
        break