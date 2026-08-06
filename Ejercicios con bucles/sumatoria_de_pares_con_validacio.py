""" Desarrolla un programa que pida un número entero positivo. Valida que sea mayor a cero.
Luego, calcula y muestra la suma de todos los números pares desde 1 hasta ese número (inclusive)."""

#Pedir el numero y definir variable para la suma
numero = int(input("Ingresa un numero entero positivo: "))
suma = 0

#Bucle Wwhile para validar que el numero sesa mayor que 0
while numero <= 0:
    print("El numero debe ser mayor que 0")
    #Si no es mayor, se le pide al user que ingrese el numero nuevamente
    numero = int(input("Ingresa un numero entero positivo: "))

#Con el range(1, numero + 1) Le decimos que empiece del numero 1 y termine en un numero despues del ingresado
for i in range(1, numero + 1):
    #Cada vez qeu se ejecute el bucle tomara en cuenta que si un numero par, se sumara a la variable suma
    #Pero cuando es impar, el programaa lo ignorara y seguira su camino xd
    if i % 2 == 0:
        suma += i

#Imprimir el resultado de la suma
print(f"La suma de los numeros pares es de: {suma} :D")