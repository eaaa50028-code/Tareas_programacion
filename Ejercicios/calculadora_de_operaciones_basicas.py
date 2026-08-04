#Pedir dos numeros y un simbolo (+,-,*,/). Ejecuta la operacion y mostrar el resultado

primer_numero = int(input("Primer numero: "))
segundo_numero = int(input("Segundo numero: "))
operador = input("Que operacion deseas reslizar? \n Suma: + \n Resta: - \n Multiplicacion: * \n Divicion: / \n : ")

suma = primer_numero + segundo_numero
resta = primer_numero - segundo_numero
multiplicacion = primer_numero * segundo_numero
division = primer_numero / segundo_numero

if operador == "+" :
    print(f"La suma de los numeros es: {suma}")
    
elif operador == "-" :
    print(f"La resta de los numeros es: {resta}")
    
elif operador == "*" :
    print(f"La multiplicacion de los numeros es: {multiplicacion}")
    
elif operador == "/" :
    print(f"La divicion de los numeros es: {division}")
    
else:
    print("Operador no valido :v")
