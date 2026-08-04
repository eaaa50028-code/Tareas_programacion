#Pedir la temperatura. Si es < 15: "Ambiente frio". Entre 15 y 25: "Ambiente templado".  Si es > 25: "Ambiente caluroso".
temperatura = int(input("Ingresar la temperatura: "))

if temperatura < 15:
    print("Ambiente frio")
elif temperatura >= 15 and temperatura <= 25:
    print("Ambiente templado")
else:
    print("Ambiente caluroso")