def encontrar_maxima_coincidencia(numero, lista2):
    
    diccionario_lista2 = {numero: None for numero in lista2}
    maxima_coincidencia = None
    
    for i in range(1, len(numero) + 1):
        subnumero = numero[:-i]
        if subnumero in diccionario_lista2:
            maxima_coincidencia = subnumero
            break
    
    return maxima_coincidencia
