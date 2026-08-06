numero_secreto = 15
jugar = "si"

while jugar == "si":
    adivinado = False
    
    for intento in range(1, 4):
        print(f"Tines: {intento} de 3 intentos")
        numero_jugador = int(input("Ingresa tu numero: "))
        
        if numero_jugador == numero_secreto:
            print("ADIVINASTE EL NUMERO!!! FELICIDADES, GANASTEEEE 🥳🥳🥳")
            adivinado = True
            break
        elif numero_jugador < numero_secreto:
            print("Intenta un numero mas alto + ")
        else:
            print("Intenta un numero mas bajo - ")
            
    if not adivinado:
        print(f"JAJAJA PERDISTEE. El numero era {numero_secreto} 🤣🤣🤣")
        
    jugar = input("¿Quieres volver a jugar? (no/no): ").lower
else:
    print("Bueno 😔")
