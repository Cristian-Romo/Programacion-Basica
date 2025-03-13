print("Bienvenido a la base de datos del tecnologico, donde puede consultar si ya puede aplicar servicio o residencia con base en sus creditos.")
nombre = input("¿Cuál es tu nombre? ")
numero = int(input("Ingresa tus creditos que obtuviste hasta este momento: "))
if numero >= 80 and numero <= 119:
    print("El alumno ",nombre, "puede hacer su servicio social")

if numero >= 120 and numero <= 360:
    print("El alumno ",nombre, "puede hacer su residencia")

if numero >= 1 and numero <= 79:
    print("El alumno ",nombre, "aun no puede realizar ninguna actividad")