inventario = {}

def agregar_item(nombre_item, cantidad):
    if nombre_item in inventario:
        inventario[nombre_item] += cantidad
        print(f"Cantidad de '{nombre_item}' actualizado a {inventario[nombre_item]}")
    else:
        inventario[nombre_item] = cantidad
        print(f"'{nombre_item}' añadido al inventario con cantidad {cantidad}.")

def vista_inventario():
    print("\n--- Inventario Actual ---")
    if not inventario:
        print("El Inventario está vacío.")
    else:
        for item, cantidad in inventario.items():
            print(f"- {item}: {cantidad}")
        print("---------------------------")

def main():
    print("Sistema de Gestión de Inventario")
    agregar_item("Laptop", 10)
    agregar_item("Mouse", 50)
    agregar_item("Laptop", 5)
    vista_inventario()
    
if __name__=="__main__":
    main()