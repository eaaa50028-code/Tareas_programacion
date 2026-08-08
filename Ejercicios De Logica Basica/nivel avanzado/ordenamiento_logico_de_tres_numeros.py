"""Enunciado: Pide 3 números distintos. Sin usar funciones como max() o min(), muestra los 3 números ordenados de mayor a menor.
Requerimientos: Uso exclusivo y encadenado de condicionales lógicos and y if-elif-else."""

num1 = int(input("Ingresar num1: "))
num2 = int(input("Ingresar num2 : "))
num3 = int(input("Ingresar num3 : "))

print("_"*50)

if num1 == num2 or num2 == num3 or num3 == num1:
    print("ERROR: Todos los numeros deben ser diferentes entre si.")
else:
    
    if num1 > num2 and num2 > num3:
        print(F"Ordenados de mayor a menor: {num1}, {num2}, {num3}")
    elif num1 > num3 and num3 > num3:
        print(F"Ordenados de mayor a menor: {num1}, {num3}, {num2}")
    elif num2 > num1 and num1 > num3:
        print(F"Ordenados de mayor a menor: {num2}, {num1}, {num3}")
    elif num2 > num3 and num3 > num1:
        print(F"Ordenados de mayor a menor: {num2}, {num3}, {num1}")
    elif num3 > num1 and num1 > num2:
        print(F"Ordenados de mayor a menor: {num3}, {num1}, {num2}")
    elif num3 > num2 and num2 > num1:
        print(F"Ordenados de mayor a menor: {num3}, {num2}, {num1}")
print("_"*50)