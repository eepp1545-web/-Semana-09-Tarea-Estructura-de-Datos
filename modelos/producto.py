# modelos/producto.py

class Producto:
    """
    Representa un producto dentro del inventario.
    Incluye atributos básicos y métodos getters/setters.
    """

    def __init__(self, producto_id: str, nombre: str, cantidad: int, precio: float):
        self.__id = producto_id
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters
    def get_id(self) -> str:
        return self.__id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_cantidad(self) -> int:
        return self.__cantidad

    def get_precio(self) -> float:
        return self.__precio

    # Setters
    def set_id(self, producto_id: str) -> None:
        self.__id = producto_id

    def set_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def set_cantidad(self, cantidad: int) -> None:
        self.__cantidad = cantidad

    def set_precio(self, precio: float) -> None:
        self.__precio = precio

    def __str__(self) -> str:
        # Representación amigable para impresión en consola
        return (
            f"ID: {self.__id} | "
            f"Nombre: {self.__nombre} | "
            f"Cantidad: {self.__cantidad} | "
            f"Precio: ${self.__precio:.2f}"
        )
