#Enunciado: Pide un salario. Tramos: 0-10k (0%), 10,001-30k (10%), más de 30k (20%). Calcula el total a pagar.

salario = float(input("Ingresar salario ($): "))

if salario <= 10000 :
    impuesto = 0
elif salario <= 30000 :
    impuesto = (salario - 10000 ) * 0.10
else: 
    impuesto = (20000 * 0.10) + ((salario - 30000) * 0.20)
salario_neto = salario - impuesto

print("=" * 30)
print(f"Salario Burto: {salario}")
print(f"Impuesto total: {impuesto}")
print(f"Salario Neto: {salario_neto}")
print("="*30)