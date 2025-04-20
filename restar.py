# Función para restar...

def restar_lista(numeros):
    if not numeros:
        return 0  # o podrías lanzar un error, según lo que necesites

    resultado = numeros[0]
    for num in numeros[1:]:
        resultado -= num

    return resultado