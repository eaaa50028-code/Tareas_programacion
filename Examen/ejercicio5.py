#Aaron
"""Gestor de inventario básico* 📦"""

inventario = {
    "Manzana": {"precio": 2.0, "cantidad": 4},
    "Platano": {"precio": 1.5, "cantidad": 12},
    "Naranja": {"precio": 3.0, "cantidad": 3},
    "Pera": {"precio": 2.5, "cantidad": 8}
}

while True:
    print("GESTOR DE INVENTARIO")
    print("1. Mostrar inventario completo")
    print("2. Actualizar cantidad de un producto")
    print("3. Salir")
    
    opcion = input("Escoja una opcion (1-3): ")

    if opcion == "1" :
        print("Inventario Actual")
        for producto, info in inventario.items():
            precio = info["precio"]
            cantidad = info["cantidad"]

            linea_producto = f"{producto}: ${precio}, Cantidad: {cantidad}"

            if cantidad < 5:
                linea_producto += "[Alerta: El Stock es Bajo]"
            print(linea_producto)

    elif opcion == "2":
        print("Actualizar Stock")
        producto = input("Coloque el nombre del producto ")

        if producto in inventario: 
            
            cantidad = int(input(f"Coloque la nueva cantidad para {producto}"))

            if   cantidad > 0:
                inventario[producto]["cantidad"] = cantidad 
                print(f"Stock de {producto} actualizado con exito")

            else: 
                print("Error: la cantidad no puede ser negativa")
        else: 
            print("Erro: el producto ingresado no se encuentra en el inventario")

    elif opcion == "3":
        print("Gracias por usar nuestro gestor de inventario")
        break

    else: 
        print("Opcion no valida, intente otra vez porfa")
        break