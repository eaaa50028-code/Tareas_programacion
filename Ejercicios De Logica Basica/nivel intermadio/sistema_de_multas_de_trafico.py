#Pide el límite de velocidad y la velocidad actual. Si excede, cobra $50 base + $5 por cada km extra.

limite = 180
actual = int(input("Ingresar velocidad actual: "))

if actual > limite :
    exceso = actual - limite
    multa = 50 + (exceso * 5)
    print(f"Exceso de velocidad detectado {exceso}km por encima del limite\n"
          f"Deberas pagar una multa de ${multa}")

else: 
    print("Fleicidades, no estas excedieno la velocidad perimitida! 😎") 