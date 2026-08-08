#Pide un año y determina si es bisiesto (divisible por 4, no por 100, excepto por 400)

anio = int(input("Ingresa un anio: "))

if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
    print(f"El anio {anio} es bisiesto")
else:
    print(f"El anio {anio} NO es bisiesto")
