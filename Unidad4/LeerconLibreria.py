from Archivos import leer_diccionarios_de_csv
# Nombre del archivo a leer y de la función a importar

archivo = "datos.csv"
# Nombre del archivo
datos = [
    {"Nombre": "Juan", "Edad": 25, "Ciudad": "Madrid"},
    {"Nombre": "Ana", "Edad": 30, "Ciudad": "Barcelona"},
    {"Nombre": "Luis", "Edad": 35, "Ciudad": "Valencia"}
]
#Diccionarios a guardar

# Guardar los diccionarios en un archivo csv
leer_diccionarios_de_csv(archivo, datos)

# Actividad hacer un programa llamado LeerconLibreria.py que importe la función leer_diccionarios_de_csv y lea el archivo datos.csv

