#Eduardo José Hernández Peña
"""Clasificador de números pares e impares* 🔢"""

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

numeros_pares = []
numeros_impares = []

for i in numeros:
    if i % 2 == 0:
        numeros_pares.append(i)
    else:
        numeros_impares.append(i)

print(f"estos numeros son pares: {numeros_pares}")
print(f"estos numeros son impares: {numeros_impares}")
