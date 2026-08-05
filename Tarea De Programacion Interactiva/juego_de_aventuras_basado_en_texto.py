"""Vamos a crear un juego de aventuras basado en texto 🕹️💭. Preaparate para desafiar tu creatividad y logica en python
con esta actividad super dinamica.

Instrucciones:
1. Debes incluir al menos 10 niveles de decisiones. Cada una co escecarios y opciones unicas.
2,. Minimo 6 niveles dben tener mas de 2 opciones.
3. Cada mensaje debe mostrar las decisiones en MAYUSCULAS Para que el jugador sepa claramente que puede escribir.
4. Tu codigo debe permitir que escriban las opciones en minusculas o mayusculas, y que el juego funcione correctamente.
5. Diferentes decisiones = Diferentes escenarios. No debe hacer respuestas duplicadas para opciones distintas.
6. Las opciones deben funcionar solo para un escenario correspondiente.
7. Usa estructuras condicionales anidadas (if, elif, else).
8. Incluye clausula else para manejar respuestas invalidas."""

print("====================================================================\n"
      "                  BIENVENIDO AL BOSQUE\n"
      "====================================================================\n")

#Nivel 1 (Dos opciones)
print("Estás caminando por un bosque oscuro y encuentras dos objetos:")
eleccion1= input("Con cuál te quedas? (FOSFORO / LINTERNA): ").upper()
print("_______________________________________________________________________")

if eleccion1 == "FOSFORO":
    #Nivel 2A (3 opciones)
    print("Coges el fósforo y lo enciendes. Por un instante, el bosque se ilumina...\n"
          "Y ves un gran oso Grizzly cerca! El fosforo se apaga rapidamente.")
    eleccion2a = input("Que haces? (CORRER / ESCONDERTE / TREPAR): ").upper()
    print("_______________________________________________________________________")
    
    if eleccion2a == "CORRER":
        
        #Nivel 3A (2 opciones)
        print("Corres a toda velocidad topezando conraices. Llegas al borde de un barranco.\n"
              "Ves una cuerda colgando, un rio abajo y una cueva cercana.")
        eleccion3a = input("Que decides hacer? (CUERDA / RIO / CUEVA): ").upper()
        print("_______________________________________________________________________")
        
        if eleccion3a == "RIO":
            
            #Nivel 4A (2 opciones)
            print("Saltas al rio y la corriente te arrastra hacia una playa de piedras.\n"
                  "A lo lejos ves una fogata encendida y una pequeña choza abandonada.")
            eleccion4a = input("Adonde te diriges? (FOGATA / CHOZA): ").upper().strip()
            print("_______________________________________________________________________")
            
            if eleccion4a == "FOGATA":
                print("Te acercas a la fogata y encuentras a unos exploradores amables\n"
                      "Te dan mantas calientes y comida. FIN DEL JUEGO: HAS SOBREVIVIDO! 🏆")
            elif eleccion4a == "CHOZA":
                print("Entras a la choza, pero el piso cede bajo tus pies y caes en una trampa.\n"
                      "FIN DEL JUEGO: HAS QEDAD ATRAPADO!💀")
            else:
                print("Opcion no valida. Quedaste paralizado por el frio. FIN DEL JUEGO! ❄️")
                
        elif eleccion3a == "CUERDA":
            
            #Nivel 4B (3 opciones)
            print("Te sujetas de la cuerda pero esta empieza a deshilacharse rapidamente.\n"
                  "Debes actuar en segundos antes de que se rompa.")
            eleccion4b = input("Que intentas? (BALANCEARCE / SOLTARSE / SUBIR): ").upper()
            print("_______________________________________________________________________")
            
            if eleccion4b == "BALANCEARCE":
                print("Te balanceas con fuerza y logras aterrizar al otor lado del barranco.\n" 
                      "Encuentras el camino de vuelta a la ciudad.\n FIN DEL JUEGO: VICTORIA! 🥳")
            elif eleccion4b == "SOLTARSE":
                print("Te sueltas demasiado pronto y caes bruscamente lesionando tu pierna.\n"
                      "FIN DEL JUEGO: NO PUEDES COTINUAR! 💔")
            elif eleccion4b == "SUBIR":
                print("Intentas subir, pero la cuerda se rompe por completo. \n FIN DEL JUEGO: HAS CAIDO! 😵")
            else: 
                print("Opcion ni valida. Dudaste demasiado y la cuerda cedio.\n FIN DEL JUEGO! :C")
        
        elif eleccion3a == "CUEVA":
            
            #Nivel 4C (3 Opciones)
            print("Entras a la cueva budcando refugop y ves tres tuneles iluminados.")
            eleccion4c = input("Por cual tunel avanzas? (IZQUIERDA / CENTRO / DERECHA): ").upper()
            print("_______________________________________________________________________")
            
            if eleccion4c == "IZQUIERDA":
                print("El tunel conduce directamente a la salida de bosque. \n FIN DEL JUEGO: HAS ESCAPADO! 🎉")
            
            elif eleccion4c == "CENTRO":
                print("Llegas a un nido de murcielagos gigante que te espantan hacia el abismo. \n FIN DEL JUEGO: PERDISTE! 🦇")
            
            elif eleccion4c == "DERECHA":
                print("Encuentras un antiguo tesoro pirata, pero la cueva se derrumba.\n FIN DEL JUEGO: EL TESORO FUE TU PERDICION! 💎")
            
            else:
                print("Opcion no valida. Te quedaste a oscuras en la cueva. \n FIN DEL JUEGO! 😔")
        else:
            print("Opcion no valida. El sos te alcanzo. \n FIN DEL JUEGO! 🐻")
            
    elif eleccion2a == "ESCONDERTE":
        
        #Nivel 3B (3 opciones)
        print("Te escondes detras de un roble centenario. El oso pasa de largo.\n Al darte la vuelta encuentras"
              "un mapa antiguo, una brujula dorada y una daga brillante.")
        eleccion3b = input("Que objeto tomas? (MAPA / BRUJULA / DAGA): ").upper()
        print("_______________________________________________________________________")
        
        if eleccion3b == "MAPA":
            
            #Nivel 4D (2 opciones)
            print("Examinas el mapa con cuidado y ves una ruta que lleva a un  templo...\n"
                  "Y otra ruta que lleva a un puente colgante.")
            eleccion4d = input("A donde decides ir? (TEMPLO / PUENTE): ").upper()
            print("_______________________________________________________________________")
            
            if eleccion4d == "TEMPLO":
                print("En el templo descifras un enigma y desbloqueas una salida secreta\n"
                      "FIN DEL JUEGO: HAS GANADO!!! 🗝️")
            
            elif eleccion4d == "PUENTE":
                print("El puente de madera estaba podrido y colapso al cruzar.\n FIN DEL JUEGO: HAS CAID AL VACIO! 🌉")
            
            else: 
                print("Opcion no valida. Perdiste el rumbo en la noche. \n FIN DEL JUEGO! 🌌")
            
        elif eleccion3b == "BRUJULA":
            
            print("Labrujulamaguica teguia a la salida del bosque. \n FIN DEL JUEGO: ESCAPASTE SIN PROBLEMAS! 🧭")
        
        elif eleccion3b == "DAGA":
            print("Sostienes ladaga pero hace un destello que atrae a lasbestias del bosque.\n FIN DEL JUEGO: FUISTE ACORRALADO. ⚔️")
        
        else: 
            print("Opcion no valida. No recogiste nada y el frio te vencio.\n FIN DEL JUEGO. 🥶")
    
    elif eleccion2a == "TREPAR":
        
        print("Subes a un arbol alto. Espeeras hasta el amanecer y ves la salida a lo lejos\n"
              "FIN DEL JUEGO: SOBREVIVISTE LA NOCHE 🔆")
    else:
        print("Opcion no valida. Te quedaste inmovil y el oso te descubrio.\n GAME OVER 😭")
        
elif eleccion1 == "LINTERNA":
    
    #Nivel 2B (3 opciones)
    print("Enciende la linterna y ves un camino despejado.\n De pronto escuchas un ruido extrano entre la maleza.")
    eleccion2b = input("Que decides hacer? (SEGUIR / BUSCAR / APAGAR): ").upper()
    print("_______________________________________________________________________")
    
    if eleccion2b == "SEGUIR":
        
        #Nivel 3C (3 opciones)
        print("Avanzas por el camino iluminado hasta llegar a un cruce con tres senderos\n"
              "Un sendero cubierto de flores, no con huellas frestas y uno con niebla densa.")
        eleccion3c = input("Cual eliges? (FLORES / HUELLAS / NIEBLA): ").upper()
        print("_______________________________________________________________________")
        
        if eleccion3c == "FLORES":
            print("El camino te lleva a una aldea pacifica de duendes.\n FIN DEL JUEGO: BIENVENIDO A TU NUEVO HOGAR!🌷")
        
        elif eleccion3c == "HUELLAS":
            
            #Nivel 4E (2 Opciones)
            print("Sigues las huellas y encuentras un cazador furtivo acampando.")
            eleccion4e = input("Que decides hacer? (HABLAR / ROBAR):").upper()
            print("_______________________________________________________________________")
            
            if eleccion4e == "HABLAR":
                print("El cazador te comparte de su comida y te lleva afuera del bosque por la manana\n"
                      "FIN DEL JUEGO: SOBREVIVISTE!!! 🏕️")
            
            elif eleccion4e == "ROBAR":
                print("Intentas robar su mochila, pero despiertan sus perros guardianes.\n FIN DEL JUEGO: HAS SIDO ATRAPADO 🐕")
            else: 
                print("Opcion no valida, te descubrieron por dudar. FIN DEL JUEGO. 😔")
                
        elif eleccion3c == "NIEBLA":
            print("Te perdes por completo en la niebla y terminas vagando en circulos para siempre.\n"
                  "FIN DEL JUEGO: TE HAS PERDIDO... ")
        else: 
            print("Opcion no valida. Tr quedaste sin pilas en la cueva.\n FIN DEL JUEGO... 🔦")
    
    elif eleccion2b == "BUSCAR":
        
        #Nivel 3D (3 opciones)
        print("Apuntas la linterna hacia la maleza y ves un lobo herido.")
        eleccion3d = input("Qu haras? (CURAR / HUIR / ATACAR): ").upper()
        print("_______________________________________________________________________")
        
        if eleccion3d == "CURAR":
            print("Ayudas al lobo. En agradecimiento, te lleva a la salida del bosque\n"
                  "FIN DEL JUEGO: GANASTE UN ALIADO Y TU LIBERTAD 🐺")
        
        elif eleccion3d == "HUIR":
            print("Tropiezas al huir en la oscuridad y tu linterna se rompe.\n FIN DEL JUEGO: NO PUEDES VER NADA!!👀")
        
        elif eleccion3d == "ATACAR":
            print("El lobo se defiende a pesar de sus heridas.\n FIN DEL JUEGO: HAS SIDO DERROTADO...🤡")
        else:
            print("Opcion no valida. El lobo se asusto y te ataco.\n FIN DEL JUEGO!")
    
    elif eleccion2b == "APAGAR" :
        print("Apagas la linterna. Una criatura pasa al lado tuyo sin notar tu presencia.\n"
              "Avanzas hasta que encuentras la carretera!\n FIN DEL JUEGO: HAS SOBREVIVIDO!!! 🛣️")
    
    else:
        print("Opcion no valida! Te deslumbras a ti mismo y tropezaste.\n FIN DEL JUEGO :/")
else:
    print("Opcion no valida. Debes elegir entre el fosforo y la linterna para comenzar...\n FIN DEL JUEGO.")