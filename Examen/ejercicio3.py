#Alejandra Estefani Urdaneta Fernandez
"""Evaluador de estado académico* 🎓"""

print(" " * 11,"EVALUADOR DE ESTADO ACADEMICO")
print("=" * 56)
print("|    Nombre         |     Nota   |     Estado          |")
print("-" * 55)
alumnos = [
    ("Eduardo   ", 60),
    ("Aaron     ", 70),
    ("Jose      ", 90),
    ("Pepito    ", 57),
    ("Alejandra ", 80),
    ("La_Chona  ", 10)
]

for nombres, notas in alumnos:
    if notas >= 60:
        estado = "Aprobado  🤓☝️"
    else:
        estado = "Reprobado 🤡🫵"
        
    print(f"|    {nombres}     |     {notas}     |     {estado}   |")
print("=" * 56)
