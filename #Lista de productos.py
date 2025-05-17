# Listas precargadas
productos = ["leche", "arvejas", "pan", "agua"]
cantidades = [2, 6, 9, 0]

# Función para mostrar el menú
def mostrar_menu():
    print("\nMenú de opciones:")
    print("1. Agregar producto")
    print("2. Ver productos agotados")
    print("3. Actualizar stock")
    print("4. Ver todos los productos")
    print("5. Salir")

# Función para agregar un producto nuevo
def agregar_producto(productos, cantidades):
    nombre = input("Ingrese el nombre del producto: ").strip()
    if nombre in productos:
        print("Ese producto ya existe.")
    else:
        cantidad_valida = False
        while not cantidad_valida:
            try:
                cantidad = int(input(f"Ingrese la cantidad para '{nombre}': "))
                if cantidad >= 0:
                    productos.append(nombre)
                    cantidades.append(cantidad)
                    print(f"Producto '{nombre}' agregado con {cantidad} unidades.")
                    cantidad_valida = True
                else:
                    print("La cantidad no puede ser negativa.")
            except ValueError:
                print("Por favor, ingrese un número entero.")

# Función para ver productos con stock agotado
def ver_productos_agotados(productos, cantidades):
    agotados = False
    print("\nProductos agotados:")
    for i in range(len(productos)):
        if cantidades[i] == 0:
            print(f"- {productos[i]}")
            agotados = True
    if not agotados:
        print("No hay productos agotados.")

# Función para actualizar el stock
def actualizar_stock(productos, cantidades):
    nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
    if nombre in productos:
        index = productos.index(nombre)
        cantidad_valida = False
        while not cantidad_valida:
            try:
                nueva = int(input(f"Ingrese la nueva cantidad para '{nombre}': "))
                if nueva >= 0:
                    cantidades[index] = nueva
                    print(f"Stock de '{nombre}' actualizado a {nueva} unidades.")
                    cantidad_valida = True
                else:
                    print("La cantidad no puede ser negativa.")
            except ValueError:
                print("Ingrese un número válido.")
    else:
        print("Producto no encontrado.")

# Función para ver todos los productos con su stock
def ver_todos_los_productos(productos, cantidades):
    print("\nStock disponible:")
    for i in range(len(productos)):
        print(f"- {productos[i]}: {cantidades[i]} unidades")

# Programa principal con menú sin usar 'break'
opcion = ""
while opcion != "5":
    mostrar_menu()
    opcion = input("Seleccione una opción (1-5): ").strip()

    if opcion == "1":
        agregar_producto(productos, cantidades)
    elif opcion == "2":
        ver_productos_agotados(productos, cantidades)
    elif opcion == "3":
        actualizar_stock(productos, cantidades)
    elif opcion == "4":
        ver_todos_los_productos(productos, cantidades)
    elif opcion == "5":
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción inválida. Intente de nuevo.")