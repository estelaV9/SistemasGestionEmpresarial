class product:
    def __init__(self, nombre, precio, stock, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.categoria = categoria

    # METODO PARA DEVOLVER LOS PRODUCTOS EN TIENDA, SE LE PASA UNA LISTA DE PRODUCTOS Y SE RECORRE
    def devolver_productos (lista):
        print("********** PRODUCTOS EN TIENDA **********")
        for product in lista:
            print(product)

    def __str__(self):
        # METODO PARA DEVOLVER INFORMACION SOBRE LOS PRODUCTOS
        return (f"Producto: {self.nombre}, Precio: {self.precio}€, "
                f"Stock: {self.stock} und, Categoria: {self.categoria} ")