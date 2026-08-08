#Pide promedio, ingresos y distancia. Beca Completa (prom>90 e ingresos<500) o Beca Transporte (prom>80 y distancia>50).


promedio = float(input("Ingresa el promedio del estudiante: "))
ingreso = float(input("Ingresa los ingresos familiares ($)"))
distancia = float(input("Ingresa la distancia de la universidad (km): "))

if (promedio >= 90 and ingreso < 500):
    print("FELICIDADES!\nObtienes Una Beca Completa")
elif promedio >= 80 and distancia >= 50 :
    print("FELICIDADES\nObtienes Una Beca Transporte")
else:
    print("No odtienes ningun tipo de beca")
    