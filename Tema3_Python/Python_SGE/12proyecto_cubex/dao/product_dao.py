import json
from json import JSONDecodeError

from model import product

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