#Pedir el total de la compra. Si supera los $500 aplicar un 10% de descuento. Mostrar el total a pagar

total_compra = float(input("Ingresa el total de la compra: "))

if total_compra > 500:
    descuento = total_compra * 0.1