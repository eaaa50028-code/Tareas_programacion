#Ingresar el total de la cuenta y el % de propina. Calcula la propina y el total a pagar.

cuenta = float(input("Ingresa total de la cuenta: $"))
porcentaje = int(input("Ingresa el porcentaje de propina que deseas agg: "))
propina = cuenta * porcentaje / 100

cuenta_total = cuenta + propina

print(f"El total de la cuenta a pagar es de: {cuenta_total}")
