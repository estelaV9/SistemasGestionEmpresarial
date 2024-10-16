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
    except JSONDecodeError:
        # SI EL JSON ESTA VACIO, INICIAR LA LISTA EN NULO
        products = []

    for product in products:
        print(product.__str__())

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
def create_product (email):
    product_name = input("Nombre del producto: ")
    product_price = input("Precio del producto: ")
    stock = input("Stock disponible: ")
    categoria = input("Categoria del cubo: ")
    new_product = product(product_name, product_price, stock, categoria, email)

    with open('product.json', 'r') as file:
        list_product_create = json.load(file) # GUARDAR TODOS LOS PRODUCTOS EN LISTA

    product_data = new_product.to_dict()
    list_product_create.append(product_data) # GUARDAR EL NUEVO PRODUCTO EN FORMA DE DICCIONARIO EN LA LISTA

    with open('product.json', 'w') as file:
        json.dump(list_product_create, file, indent=4)  # Indent para mejor legibilidad

    print("Se ha creado el producto exitosamente")

def delete_product(product_name):
    with open('product.json', 'r') as file:
        list_product_delete = json.load(file) # GUARDAR TODOS LOS PRODUCTOS EN LISTA
    # BUSCAR NOMBRE PRODUCTO
    product_found = False # SABER SI EL PRODUCTO EXISTE O NO

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
