"""Enunciado: Pide elección a 2 jugadores y determina quién gana aplicando las reglas clásicas.
Requerimientos: if-elif-else múltiples evaluando todas las combinaciones sin bucles"""

""""
papel, tijera
tijera, papel"""

print("_"*20, "BIENVENIDO AL JUEGO DE PIEDRA PAPEL O TIJERAS", "_"*25)

print("Piedra, Papel o Tigera?")

opciones = ["Piedra", "Papel", "Tijera"]

jugador1 = input("Jugador1: ").strip().capitalize()
if jugador1 not in opciones:
    print("Opcion no valida. Debes elegir Piedra, Papel o Tijera")
else:
    
    jugador2 = input("Jugador2: ").strip().capitalize()
    if jugador2 not in opciones:
        print("Opcion no valida. Debes elegir Piedra, Papel o Tijera")
    else:
        if jugador1 == jugador2:
            print("Empate, ambos ganaron")
        elif jugador1 == opciones[0] and jugador2 == opciones[1]:
            print("Jugador 2 gana")
        elif jugador1 == opciones[1] and jugador2 == opciones[0]:
            print("Jugador 1 gana")
        elif jugador1 == opciones[0] and jugador2 == opciones[2]:
            print("Jugador 1 gana")
        elif jugador1 == opciones[2] and jugador2 == opciones[0]:
            print("Jugador 2 gana")
        elif jugador1 == opciones[1] and jugador2 == opciones[2]:
            print("Jugador 2 gana")
        elif jugador1 == opciones[2] and jugador2 == opciones[1]:
            print("Jugador 1 gana")
