#Saldo = $1000. Pide un retiro. Solo es válido si es <= al saldo y múltiplo de 10. Muestra el saldo final.

saldo = 1000

print(f"Bienvenido al Cajero Automático. Su saldo actual es: ${saldo}")

retiro = int(input("Ingrese el monto que desea retirar (múltiplos de 10): "))

if retiro > 0 and retiro % 10 == 0:
    if retiro <= saldo:
        saldo_final = saldo - retiro
        print("Retiro exitoso! 🤑")
        print(f"Ha retirado: ${retiro}. Ahora su saldo es de: ${saldo_final}")
    else:
        print(f"EROR! Saldo insuficiente, tu saldo es de: ${saldo}")
else:
    if retiro <= 0 :
        print("ERROR! El monto debe ser mayor que cero.")
    else:
        print("El monto debej ser multiplo de 10 (ejemplo: 10, 20, 30, etc).")