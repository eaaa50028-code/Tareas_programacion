#Jose Daniel Garcia Ortiz
"""Extractor de datos únicos* 🔍"""

lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista2 = [2, 4, 6, 8, 10, 12, 14]
lista3 = []

for numero in lista1 : 
    if numero not in lista2:
        lista3.append(numero)
print(lista3)