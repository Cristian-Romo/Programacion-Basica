# Solicitar al usuario un texto para analizar
texto = input("Introduce un texto para analizar: ")

# Inicializar contadores
contador_vocales = 0
contador_consonantes = 0
contador_numeros = 0
contador_otros = 0

# Recorrer cada carácter del texto
for caracter in texto:
    caracter = caracter.lower()  # Convertir a minúscula

    if caracter in 'aeiou':
        contador_vocales += 1
    elif 'a' <= caracter <= 'z':  # Si es una letra entre 'a' y 'z'
        contador_consonantes += 1
    elif '0' <= caracter <= '9':  # Si es un dígito entre '0' y '9'
        contador_numeros += 1
    else:
        contador_otros += 1

# Mostrar resultados
print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")
print(f"Números: {contador_numeros}")
print(f"Otros caracteres: {contador_otros}")