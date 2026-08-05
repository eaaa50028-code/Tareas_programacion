#Pide los 3 lados de un triángulo y di si es equilátero, isósceles o escaleno

a = float(input("Ingresa el lado A: "))
b = float(input("Ingresa el lado B: "))
c = float(input("Ingresa el lado C: "))

if a + b > c and a + c > b and b + c > a :
    
    if a == b and b == c :
        tipo_de_triangulo = "Equilatero"
    
    elif a == b or b == c or c == a :
        tipo_de_triangulo = "Isoceles"
    else: 
        tipo_de_triangulo = "Escaleno"
    print(f"Tu triangulo es un triangulo {tipo_de_triangulo} 😋")
else:
    print("Los lados ingresados no pueden formar un triangulo.")