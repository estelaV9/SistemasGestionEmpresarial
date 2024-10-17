class product:
    def __init__(self, nombre, precio, stock, categoria, owner):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria
        self.owner = owner

    def to_dict(self):
        # CONVERTIR UN OBJETO A UN DICCIONARIO
        return {
            "nombre": self.nombre,
            "precio": self.precio,
            "stock": self.stock,
            "categoria": self.categoria,
            "owner": self.owner
        }


    def __str__(self):
        # METODO PARA DEVOLVER INFORMACION SOBRE LOS PRODUCTOS
        return (f"Producto: {self.nombre}, Precio: {self.precio}€, "
                f"Stock: {self.stock} und, Categoria: {self.categoria}, Propietario: {self.owner}")