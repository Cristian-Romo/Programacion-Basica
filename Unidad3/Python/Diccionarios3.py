estudiantes = {
    "Ontiveros": {"edad": 18, "carrera": "Mecatronica"},
    "Victor": {"edad": 18, "carrera": "Mecatronica"},
    "Lupe": {"edad": 18, "carrera": "Mecatronica"},
    "Aron": {"edad": 18, "carrera": "Mecatronica"},
    "Alexa": {"edad": 18, "carrera": "Mecatronica"},
    "Oswaldo": {"edad": 18, "carrera": "Mecatronica"},
    "Roberto": {"edad": 18, "carrera": "Mecatronica"},
    "Adan": {"edad": 18, "carrera": "Mecatronica"},
    "Sabayd": {"edad": 19, "carrera": "Mecatronica"},
    "Juan": {"edad": 18, "carrera": "Mecatronica"},
    "Arath": {"edad": 18, "carrera": "Mecatronica"}
}

# Imprimir el diccionario completo
print("Diccionario de estudiantes:")
for nombre, detalles in estudiantes.items():
    print(f"{nombre}: {detalles}")

profesores = {
    "Eduardo": {"Materia": "Programacion Basica", "Promedio": 7.9},
    "La risitas": {"Materia": "Calcuo integral", "Promedio": 10.0},
    "La gallos": {"Materia": "Contabilidad", "Promedio": 10.0},
    "Finish Class": {"Materia": "Ingles", "Promedio": 8.4},
    "El presumido": {"Materia": "Ingenieria de los materiales", "Promedio": 9.1},
    "El ASMR": {"Materia": "Algebra lineal", "Promedio": 0.0},
    "Abuelo de manuel": {"Materia": "Abuelo de manuel", "Promedio": 8.0}
}

# Imprimir el diccionario completo
print("Diccionario de profesores:")
for nombre, detalles in profesores.items():
    print(f"{nombre}: {detalles}")