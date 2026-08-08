#Enunciado: Pide día, mes y año. Verifica si la fecha es real (cuidando meses de 30/31 días y años bisiestos)."

print("_"*20,"Ingresar fecha", "_"*20)
anio = int(input("     Año: "))
mes = int(input("     Mes: "))
dia = int(input("     Dia: "))

if anio > 0 :
    if mes >= 1 and mes <= 12 :
        if mes == 4 or mes == 6 or mes == 9 or mes == 11:
            maximo_de_dias = 30
        elif mes == 2:
            if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
                maximo_de_dias = 29
            else:
                maximo_de_dias = 28
        else:
            maximo_de_dias = 31
        if dia > 1 and dia <= maximo_de_dias:
                valido = True
        else:
            valido = False
    else:
        valido = False
else:
    valido = False

if valido:
    print(f"La fecha {dia}/{mes}/{anio} es valida")
else: 
    print(f"La fecha {dia}/{mes}/{anio} no es valida")
