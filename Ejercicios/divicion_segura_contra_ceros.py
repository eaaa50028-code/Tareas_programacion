#Pedir dos numeros para dividirlos. Si el divisor es 0, mostrar "Error". Si no, realiza la division
dividendo = int(input("Ingresar el dividendo: "))
divisor = int(input("Ingresar el divisor: "))

if divisor == 0:
    print("Error")
else:
    resultado = dividendo / divisor
    print(f"El resultado de la division es: {resultado}")
