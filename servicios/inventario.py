# servicios/inventario.py

from modelos.producto import Producto


class Inventario:
    """
    Gestiona una lista de productos y operaciones básicas:
    agregar, eliminar, actualizar, buscar y listar.
    """

    def __init__(self):
        # Lista principal de almacenamiento
        self.__productos: list[Producto] = []

    def __buscar_por_id(self, producto_id: str) -> Producto | None:
        """Búsqueda interna por ID (devuelve Producto o None)."""
        for p in self.__productos:
            if p.get_id() == producto_id:
                return p
        return None

    def anadir_producto(self, producto: Producto) -> bool:
        """
        Agrega un producto si el ID no existe.
        Retorna True si se agregó; False si el ID ya estaba repetido.
        """
        if self.__buscar_por_id(producto.get_id()) is not None:
            return False

        self.__productos.append(producto)
        return True

    def eliminar_producto(self, producto_id: str) -> bool:
        """
        Elimina un producto por ID.
        Retorna True si lo eliminó; False si no encontró el ID.
        """
        producto = self.__buscar_por_id(producto_id)
        if producto is None:
            return False

        self.__productos.remove(producto)
        return True

    def actualizar_producto(self, producto_id: str, nueva_cantidad: int | None = None, nuevo_precio: float | None = None) -> bool:
        """
        Actualiza cantidad y/o precio de un producto por ID.
        Retorna True si actualizó; False si no existe el producto.
        """
        producto = self.__buscar_por_id(producto_id)
        if producto is None:
            return False

        if nueva_cantidad is not None:
            producto.set_cantidad(nueva_cantidad)

        if nuevo_precio is not None:
            producto.set_precio(nuevo_precio)

        return True

    def buscar_por_nombre(self, texto: str) -> list[Producto]:
        """
        Devuelve lista de productos cuyo nombre contenga 'texto' (coincidencia parcial).
        No distingue mayúsculas/minúsculas.
        """
        texto = texto.strip().lower()
        if not texto:
            return []

        resultados: list[Producto] = []
        for p in self.__productos:
            if texto in p.get_nombre().lower():
                resultados.append(p)

        return resultados

    def listar_productos(self) -> list[Producto]:
        """Devuelve una copia de la lista para evitar modificaciones externas directas."""
        return list(self.__productos)
