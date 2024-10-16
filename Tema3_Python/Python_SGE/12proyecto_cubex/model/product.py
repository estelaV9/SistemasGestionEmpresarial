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

    # METODO PARA DEVOLVER LOS PRODUCTOS EN TIENDA, SE LE PASA UNA LISTA DE PRODUCTOS Y SE RECORRE
    def devolver_productos (lista):
        print("********** PRODUCTOS EN TIENDA **********")
        for product in lista:
            print(product)

    def __str__(self):
        # METODO PARA DEVOLVER INFORMACION SOBRE LOS PRODUCTOS
        return (f"Producto: {self.nombre}, Precio: {self.precio}€, "
                f"Stock: {self.stock} und, Categoria: {self.categoria}, Propietario: {self.owner}")