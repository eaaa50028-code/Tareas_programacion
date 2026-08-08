print("="*45)
print(" "*10, "Clasificador_de_numeros", " "*11)
print("="*45)

validador = False
positivos = 0
negativos = 0
ceros = 0

while validador == False:
    cantidad = int(input("\nIngresa una cantidad de numeros (minimo 3):"))
    if cantidad >=3 :
        validador = True
        
        for i in range (1, cantidad +1):
            numeros = float(input("Ingresar un numero: "))
            
            if numeros > 0:
                positivos += 1
            elif numeros < 0:
                negativos +=1
            else:
                ceros += 1
        
        print("_"*45)        
        print(f"\n Cantidad de positivos: {positivos}\n Cantidad de ceros: {ceros}\n Cantidad de negativos: {negativos}")
    else:
        print("\nERRORRR! Cantida no valida :/")
