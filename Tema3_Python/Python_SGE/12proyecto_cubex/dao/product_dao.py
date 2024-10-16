import json
from json import JSONDecodeError

from model.product import product
from dao import user_dao


# FUNCION PARA LISTAR TODOS LOS PRODUCTOS
def list_product():
    try:
        with open('product.json', 'r') as file:
            products = json.load(file)
    except FileNotFoundError:
        # SI NO SE HA ENCONTRADO ARCHIVO, INCIAR LA LISTA EN NULO
        products = []

    if products:
        for product in products:
            print(product.__str__())
    else:
        print("No hay productos disponibles")


# FUNCION PARA LISTAR LOS PRODUCTOS DE UN USUARIO
def list_product_user(user_name):
    try:
        with open('product.json', 'r') as file:
            products = json.load(file)
    except FileNotFoundError:
        # SI NO SE HA ENCONTRADO ARCHIVO, INCIAR LA LISTA EN NULO
        products = []
    except JSONDecodeError:
        # SI EL JSON ESTA VACIO, INICIAR LA LISTA EN NULO
        products = []

    for product in products:
        if product['owner'] == user_name:
            print(product.__str__())


# FUNCION PARA CREAR UN PRODUCTO
def create_product(email):
    product_name = input("Nombre del producto: ")
    product_price = input("Precio del producto: ")
    stock = input("Stock disponible: ")
    categoria = input("Categoria del cubo: ")
    new_product = product(product_name, product_price, stock, categoria, email)

    with open('product.json', 'r') as file:
        list_product_create = json.load(file)  # GUARDAR TODOS LOS PRODUCTOS EN LISTA

    product_data = new_product.to_dict()
    list_product_create.append(product_data)  # GUARDAR EL NUEVO PRODUCTO EN FORMA DE DICCIONARIO EN LA LISTA

    with open('product.json', 'w') as file:
        json.dump(list_product_create, file, indent=4)  # Indent para mejor legibilidad

    print("Se ha creado el producto exitosamente")


# FUNCION PARA ELIMINAR PRODUCTO POR NOMBRE
def delete_product(product_name):
    with open('product.json', 'r') as file:
        list_product_delete = json.load(file)  # GUARDAR TODOS LOS PRODUCTOS EN LISTA
    # BUSCAR NOMBRE PRODUCTO
    product_found = False  # SABER SI EL PRODUCTO EXISTE O NO

    for product in list_product_delete:
        if product['nombre'] == product_name:  # SI HAY UN PRODUCTO CON ESE NOMBRE SE ELIMINA
            list_product_delete.remove(product)  # ELIMINAR EL PRODUCTO DE LA LISTA
            product_found = True
            break  # SALIR DEL BUCLE

    if product_found:
        # SE GUARDA LA LISTA ACTUALIZADA DE VUELTA EN EL JSON
        with open('product.json', 'w') as file:
            json.dump(list_product_delete, file, indent=4)
        print(f"Producto '{product_name}' eliminado exitosamente.")
    else:
        print(f"No se encontró el producto '{product_name}'.")


# FUNCION PARA MODIFICAR UN PRODUCTO POR SU NOMBRE
def modify_product(product_name):
    with open('product.json', 'r') as file:
        product_list = json.load(file)  # GUARDAR TODOS LOS PRODUCTOS EN UNA LISTA

    # BUSCAR NOMRBE PRODUCTO
    product_found = False  # SABER SI SE HA ENCONTRADO EL PRODUCTO
    for product in product_list:
        if product['nombre'] == product_name:  # SI HAY UN PRODUCTO CON ESE NOMBRE SE MODIFICA
            product_found = True

            # SE SOLICITA LOS NUEVOS DATOS PARA EL PRODUCTO
            new_name = input("Nombre: ")
            new_price = input("Precio: ")
            new_stock = input("Stock disponible: ")
            new_category = input("Categoría del cubo: ")

            # SE MODIFICAN LOS ATRIBUTOS
            product['nombre'] = new_name
            product['precio'] = float(new_price)
            product['stock'] = int(new_stock)
            product['categoria'] = new_category

            break  # SE SALE DEL BUCLE DESPUES DE MODIFICAR

    if product_found:
        # SE GUARDA LA LISTA ACTUALIZADA DE VUELTA AL JSON
        with open('product.json', 'w') as file:
            json.dump(product_list, file, indent=4)
        print(f"Producto '{product_name}' modificado exitosamente.")
    else:
        print(f"No se encontró el producto '{product_name}'.")


# FUNCION PARA COMPRAR PRODUCTO
def buy_product(product_name):
    with open('product.json', 'r') as file:
        product_list = json.load(file)  # GUARDAR TODOS LOS PRODUCTOS EN UNA LISTA

    # BUSCAR NOMRBE PRODUCTO
    product_found = False  # SABER SI SE HA ENCONTRADO EL PRODUCTO
    stock_disponible = True  # SABER SI HAY STOCK DISPONIBLE

    for product in product_list:
        if product['nombre'] == product_name:  # SI HAY UN PRODUCTO CON ESE NOMBRE
            product_found = True

            # SI EL STOCK NO ES CERO SE MODIFICA EL STOCK
            if product['stock'] != 0:
                new_stock = product['stock'] - 1  # SE LE RESTA 1 AL STOCK
                product['stock'] = int(new_stock)  # SE MODIFICA EL STOCK
                break
            else:
                stock_disponible = False  # SI NO HAY STOCK DEVUELVE FALSE

    if product_found and stock_disponible:  # SI EXISTE ESE PRODUCTO Y HAY STOCK DISPONIBLE ENTONCES SE GUARDA
        # SE GUARDA LA LISTA ACTUALIZADA DE VUELTA AL JSON
        with open('product.json', 'w') as file:
            json.dump(product_list, file, indent=4)
        print(f"Producto '{product_name}' comprado exitosamente.")
    elif not stock_disponible:  # SI NO HAY STOCK DISPONIBLE SALTA UN MENSAJE
        print("No hay stock disponible.")
    elif not product_found:  # SI ESE PRODUCTO NO EXISTE, SALTA UN MENSAJE
        print(f"No se encontró el producto '{product_name}'")
