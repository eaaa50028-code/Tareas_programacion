#Pedir el total de la compra. Si supera los $500 aplicar un 10% de descuento. Mostrar el total a pagar

compra = float(input("Ingresa el total de la compra: "))

if compra > 500:
    descuento = compra * 0.1
    total_a_pagar = compra - descuento
    print(f"Total a pagar con un descuento de 10%: ${total_a_pagar}")
else:
    print(f"Total a pagar sin descuento: ${compra}")
