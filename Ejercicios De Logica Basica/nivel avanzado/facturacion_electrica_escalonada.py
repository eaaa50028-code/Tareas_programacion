#Pide consumo en KWh. Factura: 0-100 a $0.50, 101-300 a $1.00, 301+ a $1.50.

consumo = float(input("Ingresa el consumo (kwh): "))

if consumo <= 100:
    costo_tramo1 = consumo * 0.50
    costo_tramo2 = 0
    costo_tramo3 = 0
    
elif consumo <= 300 :
    costo_tramo1 = 100 *0.50
    sobreante_tramo2 = consumo - 100
    costo_tramo2 = sobreante_tramo2 * 1.00
    costo_tramo3 = 0
else:
    costo_tramo1 = 100 * 0.50
    costo_tramo2 = 200 * 1.00
    sobreante_tramo3 = consumo - 300
    costo_tramo3 = sobreante_tramo3 * 1.50
    
factura = costo_tramo1 + costo_tramo2 + costo_tramo3

print("="*50)

print(f"Consumo total: {consumo}")
print("_"*50)
print(f"tramo 1 (0-100 kwh: {costo_tramo1})")
print(f"Tramo 2 (101-300 kwh: {costo_tramo2})")
print(f"Tramo 3 (301 + kwh : {costo_tramo3})")
print("_"*50)
print(f"Total a pagar: {factura}")