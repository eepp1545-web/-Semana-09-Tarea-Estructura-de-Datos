# main.py

from modelos.producto import Producto
from servicios.inventario import Inventario


def leer_entero(mensaje: str, minimo: int | None = None) -> int:
    """Lee un entero con validación básica."""
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if minimo is not None and valor < minimo:
                print(f"  Debe ser un número >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida. Ingresa un número entero.")


def leer_flotante(mensaje: str, minimo: float | None = None) -> float:
    """Lee un flotante con validación básica."""
    while True:
        entrada = input(mensaje).strip().replace(",", ".")  # por si escriben 10,50
        try:
            valor = float(entrada)
            if minimo is not None and valor < minimo:
                print(f"  Debe ser un número >= {minimo}.")
                continue
            return valor
        except ValueError:
            print("  Entrada inválida. Ingresa un número (ej: 12.50).")


def leer_texto_no_vacio(mensaje: str) -> str:
    """Lee texto no vacío."""
    while True:
        texto = input(mensaje).strip()
        if texto:
            return texto
        print("  No puede estar vacío.")


def mostrar_menu() -> None:
    print("\n====== SISTEMA DE INVENTARIO ======")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Listar inventario")
    print("6. Salir")


def opcion_anadir(inventario: Inventario) -> None:
    print("\n--- Añadir producto ---")
    producto_id = leer_texto_no_vacio("ID (único): ")
    nombre = leer_texto_no_vacio("Nombre: ")
    cantidad = leer_entero("Cantidad: ", minimo=0)
    precio = leer_flotante("Precio: ", minimo=0.0)

    producto = Producto(producto_id, nombre, cantidad, precio)
    if inventario.anadir_producto(producto):
        print(" Producto agregado correctamente.")
    else:
        print(" No se pudo agregar: el ID ya existe.")


def opcion_eliminar(inventario: Inventario) -> None:
    print("\n--- Eliminar producto ---")
    producto_id = leer_texto_no_vacio("ID del producto a eliminar: ")

    if inventario.eliminar_producto(producto_id):
        print(" Producto eliminado.")
    else:
        print(" No se encontró un producto con ese ID.")


def opcion_actualizar(inventario: Inventario) -> None:
    print("\n--- Actualizar producto ---")
    producto_id = leer_texto_no_vacio("ID del producto a actualizar: ")

    print("¿Qué deseas actualizar?")
    print("1. Cantidad")
    print("2. Precio")
    print("3. Cantidad y precio")

    opcion = leer_entero("Elige una opción (1-3): ", minimo=1)
    while opcion not in (1, 2, 3):
        print("  Opción inválida.")
        opcion = leer_entero("Elige una opción (1-3): ", minimo=1)

    nueva_cantidad = None
    nuevo_precio = None

    if opcion in (1, 3):
        nueva_cantidad = leer_entero("Nueva cantidad: ", minimo=0)
    if opcion in (2, 3):
        nuevo_precio = leer_flotante("Nuevo precio: ", minimo=0.0)

    if inventario.actualizar_producto(producto_id, nueva_cantidad, nuevo_precio):
        print(" Producto actualizado.")
    else:
        print(" No se encontró un producto con ese ID.")


def opcion_buscar(inventario: Inventario) -> None:
    print("\n--- Buscar producto por nombre ---")
    texto = leer_texto_no_vacio("Ingresa parte del nombre: ")
    resultados = inventario.buscar_por_nombre(texto)

    if not resultados:
        print(" No se encontraron productos con esa coincidencia.")
        return

    print(f" Se encontraron {len(resultados)} producto(s):")
    for p in resultados:
        print(" -", p)


def opcion_listar(inventario: Inventario) -> None:
    print("\n--- Listar inventario ---")
    productos = inventario.listar_productos()

    if not productos:
        print(" Inventario vacío.")
        return

    for p in productos:
        print(" -", p)


def main() -> None:
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = leer_entero("Selecciona una opción (1-6): ", minimo=1)

        if opcion == 1:
            opcion_anadir(inventario)
        elif opcion == 2:
            opcion_eliminar(inventario)
        elif opcion == 3:
            opcion_actualizar(inventario)
        elif opcion == 4:
            opcion_buscar(inventario)
        elif opcion == 5:
            opcion_listar(inventario)
        elif opcion == 6:
            print(" Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("  Opción inválida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
