#Si el cliente tiene 60 anos o mas,  aplicale un descuento de 20% a una entrada de $10




edad = int(input("Ingresa tu edad: "))
entrada = 10
descuento = entrada * 0.20

pago_total = entrada - descuento

if edad >= 60:
    print("Felicidades!!! Has recibido un descuento del 20%\n"
          f"Ahora tu entrada pasa de costar ${entrada} a costar ${pago_total}")