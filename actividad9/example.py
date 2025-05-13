from operator import itemgetter  # uso: ordenamiento de diccionarios

# creación de diccionario
diccionarioTransacciones = {
    "2025-05-01": 15000,
    "2025-04-28": 8500,
    "2025-05-03": 12000,
    "2025-04-30": 17000,
}


def quicksort_items(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0][1]  # valor (monto)
    menores = [item for item in lista[1:] if item[1] <= pivote]
    mayores = [item for item in lista[1:] if item[1] > pivote]
    return quicksort_items(menores) + [lista[0]] + quicksort_items(mayores)


def mostrandoDiccionario():
    print("--------------Sin orden") 
    for clave, valor in diccionarioTransacciones.items():
        print(f"{clave}: {valor}")

    print("--------------Ordenado por fecha") 
    for clave, valor in sorted(diccionarioTransacciones.items(), key=itemgetter(0)):
        print(f"{clave}: {valor}")

    print("--------------Ordenado por monto") 
    for clave, valor in sorted(diccionarioTransacciones.items(), key=itemgetter(1)):
        print(f"{clave}: {valor}")

    print("--------------Ordenado por monto (Quicksort)") 
    ordenado_quicksort = quicksort_items(list(diccionarioTransacciones.items()))
    for clave, valor in ordenado_quicksort:
        print(f"{clave}: {valor}")


def buscar_por_fecha(diccionario, fecha):
    if fecha in diccionario:
        print(f"Se encontró la fecha {fecha}: Monto ${diccionario[fecha]:,.2f}")
    else:
        print(f"No se encontró la fecha {fecha}")


mostrandoDiccionario()
fechaIngresada = input("Ingrese fecha con formato 2001-01-01: ")
buscar_por_fecha(diccionarioTransacciones, fechaIngresada)
