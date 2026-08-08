#Cada quien aporto su grnito de arena 🤓
"""Analizador de frecuencias de caracteres* 🔠"""

texto = input("Ingresar Texto: ").strip().upper()
print("_" * 100)

signos = [" ", ".", ",", "?", "!", "/", "@", "#", "$", "%", "&", "*", "(", ")", "-", "_", "+", "=", "|", "~"]
frecuencia = {}

for caracter in texto:
        if caracter != signos:
            if caracter in frecuencia:
                frecuencia[caracter] += 1
            else:
                frecuencia[caracter] = 1
            
print("_" *40, "FRECUEENCIA", "_"*47)
print(frecuencia)



#Texto para probar el programa:
"""Urano está compuesto de agua, metano y amoniaco sobre un pequeño centro rocoso. Su atmósfera está hecha de hidrógeno y helio, como Júpiter y Saturno, pero además contiene metano. El metano es lo que le da a Urano el color azul."""
