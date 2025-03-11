#Lista de nombres
nombres = ["Lupe", "Ontiveros", "Victor", "Aron", "Alexa", "Oswaldo", "Roberto", "Adan", "Sabayd", "Juan", "Arath"]

# Lista de números
numeros = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18,]

#Razones por las que saba es hermoso
razones = ["Buen compa", "Tiene los mejores cortes de pelo", "Leal", "Juega roblox", "Se tarda en salir", "Dice mensadas", "Su enemigo es tuerto", "Su otro enemigo es sau", "Molesta a alexa con angel","Esta cieguito"]

#Lista de materias
Materias = ["Programacion Basica", "Calculo integral", "Administracion de empresas", "Ingles", "Propiedades de los materiales", "Algebra lineal", "Contabilidad"]

#Lista de profesores
Profesores = ["El de los drones", "La risas fuertes", "La de contabilidad", "La timida", "El presumido", "El ASMR", "Abuelo de Manuel"]

print(len(nombres))
print(max(numeros))
print(min(numeros))
nombres.sort()
print(nombres)
Materias.remove("Programacion Basica")
print(Materias)
Materias.append("Programacion Avanzada")

Materias.append("Programacion Basica")
print(Materias)