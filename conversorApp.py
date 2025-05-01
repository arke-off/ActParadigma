'''PEP 8
Autores : 
Meza Santaigo <santiagoexe75@gmail.com>
Alcaraz Nicolas <nicolasagustinalcaraz@gmail.com>
Estado :Activo
Creado :30 de abril de 2025
'''
import os 
from msvcrt import getch
os.system("cls")

def ingresoDivisa():
	print("Bienvenido al conversor de monedas\n")
	print("Indique la moneda que utiliza actualmente")

	print("1. USD\n")
	print("2. EUR\n") 
	print("3. ARS\n")
	print("4. BRL")

	print("Presionando un Numero");opcion = getch()

ingresoDivisa()
#montoIngresado = input("Presionando un Numero: ")
#monedaSeleccionada = input("seleccione una moneda: ")
