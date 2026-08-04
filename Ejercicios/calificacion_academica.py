#Pedir el una nota del 0 al 100. Si la nota es 60 o mas, imprimir "Aprobado", sino "Reprobado"

nota = int(input("Ingresa tu nota (0-100): "))

if nota >= 60:
    print("Aprobado :D")
else:
    print("Reprobado :(")