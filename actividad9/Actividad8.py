'''PEP 8
Autores : 
Codermatz Valentino <valecodermatz@gmail.com>
Meza Santaigo <santiagoexe75@gmail.com>
Alcaraz Nicolas <nicolasagustinalcaraz@gmail.com>
Estado :Activo
Creado :30 de abril de 2025
'''
import time
import random
from typing import List, Callable, Tuple

class AlgoritmoOrdenamiento:
    def __init__(self, nombre: str, funcion: Callable):
        self.nombre = nombre
        self.funcion = funcion
        self.tiempo_ejecucion = 0
        self.comparaciones = 0

    def ejecutar(self, lista: List[int]) -> Tuple[List[int], float, int]:
        inicio = time.time()
        resultado = self.funcion(lista.copy())
        fin = time.time()
        self.tiempo_ejecucion = fin - inicio
        return resultado, self.tiempo_ejecucion, self.comparaciones

# Algoritmos de ordenamiento directo
def burbuja(lista: List[int]) -> List[int]:
    n = len(lista)
    comparaciones = 0
    for i in range(n):
        for j in range(0, n-i-1):
            comparaciones += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

def seleccion(lista: List[int]) -> List[int]:
    n = len(lista)
    comparaciones = 0
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            comparaciones += 1
            if lista[j] < lista[min_idx]:
                min_idx = j
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista

# Algoritmos de ordenamiento logarítmico
def quicksort(lista: List[int]) -> List[int]:
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    izquierda = [x for x in lista if x < pivot]
    medio = [x for x in lista if x == pivot]
    derecha = [x for x in lista if x > pivot]
    return quicksort(izquierda) + medio + quicksort(derecha)

# Algoritmos de búsqueda
def busqueda_lineal(lista: List[int], objetivo: int) -> int:
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1

def busqueda_binaria(lista: List[int], objetivo: int) -> int:
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def generar_lista_aleatoria(tamano: int) -> List[int]:
    return random.sample(range(1, tamano + 1), tamano)

def main():
    # Crear instancias de algoritmos
    algoritmos_ordenamiento = [
        AlgoritmoOrdenamiento("Burbuja", burbuja),
        AlgoritmoOrdenamiento("Selección", seleccion),
        AlgoritmoOrdenamiento("QuickSort", quicksort)
    ]

    # Generar lista de prueba
    lista_prueba = generar_lista_aleatoria(1000)
    
    # Probar algoritmos de ordenamiento
    print("Resultados de ordenamiento:")
    for algoritmo in algoritmos_ordenamiento:
        resultado, tiempo, comparaciones = algoritmo.ejecutar(lista_prueba)
        print(f"\n{algoritmo.nombre}:")
        print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
        print(f"Comparaciones realizadas: {comparaciones}")

if __name__ == "__main__":
    main()
input("\nPresione enter para continuar...")