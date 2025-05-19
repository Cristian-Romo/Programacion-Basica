# Solicitar el nombre del programa
nombre_programa = input("Introduce el nombre del programa: ")

print(f"Has iniciado el programa: {nombre_programa}")

# Solicitar una frase o texto al usuario
texto_usuario = input("Escribe una frase o texto: ")

# Dividir el texto en palabras utilizando los espacios como separador
palabras = texto_usuario.split()

# Obtener el número de palabras
cantidad_palabras = len(palabras)

# Mostrar el resultado
print(f"El texto contiene {cantidad_palabras} palabras.")