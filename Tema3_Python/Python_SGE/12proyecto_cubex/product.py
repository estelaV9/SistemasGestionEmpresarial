class product:
    def __init__(self, nombre, precio, stock, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    def __str__(self):
        # METODO PARA DEVOLVER INFORMACION SOBRE LOS PRODUCTOS
        return (f"Producto: {self.nombre}, Precio: {self.precio}€, "
                f"Stock: {self.stock} und, Categoria: {self.categoria} ")