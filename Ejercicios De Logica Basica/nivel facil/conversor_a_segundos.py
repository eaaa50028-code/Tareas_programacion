#Pide horas y minutos. Convierte y muestra el total en segundos

hora = int(input("Ingresar unicamente la hora: "))
minutos = int(input("Ingresar unicamente los minutos: "))

#convertir las horas en minutos
hora_minutos = hora * 60

#Sumar todos los minutos
minutos_totales = minutos + hora_minutos

#converti losminutos en segundos
segundos_total = minutos_totales * 60

print(f"Convirtiendolos serian un total de: {segundos_total} segundos")