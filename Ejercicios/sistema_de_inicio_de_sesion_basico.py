#Pedir una contraseña. Si es "admin1234", mostrar "Acceso concedido", de lo contrario, mostrar "Acceso denegado".

contraseña = "admin1234"
ingreso = input("Ingresa la contraseña: ")

if ingreso == contraseña:
    print("Acceso concedido")
else:
    print("Acceso denegado")