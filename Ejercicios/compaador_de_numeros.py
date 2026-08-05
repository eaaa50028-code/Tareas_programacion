#Ingresar dos numeros e indicar cual es mayor, cual es menor o si son iguales
num1 = int(input("Ingresar el primernumero: "))
num2= int(input("Ingresar el segundo numero: "))

if num1 > num2:
    print(f"El primer numero {num1} es mayor que el segundo numero {num2}")
elif num1 < num2:
    print(f"El primer numero {num1} es menor que el segundo numero {num2}")
else:
    print(f"Los numeros son iguales: {num1}")