mi_diccionario = {
"nombre": "Arke",
"edad": 22,
"carrera": "Ingeniería en Sistemas"
}

print(mi_diccionario["nombre"]) 
print(mi_diccionario,"\n\n") 

print("Impresion en lista\n")

for  clave, valor in (mi_diccionario.items()):
    print(f"{clave}: {valor}")


print("Impresion en lista ordenada\n")

for  clave, valor in sorted(mi_diccionario.items()):
    print(f"{clave}: {valor}")