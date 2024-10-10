# ************************ PETICIONES API **********************************
""" Realizar un ejercicio para aprender a acceder a una API a través de peticiones HTTP:
•	Visitar la web: https://pokeapi.co y leer la documentación
•	En la pestaña “About”, leer la definición de API. 
•	Ir a la pestaña API v2  menú izquierdo Pokémon  Pokemon ver el endpoint que sugieren. 
    Escribirlo en un navegador y observar la respuesta (https://pokeapi.co/api/v2/pokemon/35/). 
    Es un JSON con información del Pokemon 35: name, types, weight…

API (Interfaz de Programación de Aplicaciones): Una API es un conjunto de reglas y protocolos que permite que diferentes 
aplicaciones se comuniquen entre sí. Actúa como un intermediario que permite que un programa solicite datos o servicios de otro. 
Las APIs pueden ser de varios tipos, como APIs web, APIs de sistema operativo, APIs de bibliotecas, etc.

Endpoint: Un endpoint es una URL específica donde se puede acceder a un recurso en un servidor a través de una API. 
Cada endpoint representa una función o un conjunto de datos que se pueden consultar o manipular mediante peticiones HTTP 
(GET, POST, PUT, DELETE, etc.). En el contexto de una API RESTful, un endpoint generalmente está vinculado a un recurso 
específico, como un usuario, un producto o una entrada en una base de datos.

API RESTful: Una API RESTful es un tipo de API que sigue los principios de REST (Transferencia de Estado Representacional). 
REST es un estilo arquitectónico para el desarrollo de servicios web que utiliza los métodos HTTP y se basa en el uso de recursos
identificados por URLs. Las APIs RESTful son sin estado, lo que significa que cada petición del cliente al servidor debe contener
toda la información necesaria para entender y procesar la solicitud.

Uso de Endpoints
En una API RESTful, los endpoints son fundamentales para acceder a los recursos. Aquí hay ejemplos de cómo se utilizan:

GET /productos: Obtiene una lista de todos los productos.
GET /productos/{id}: Obtiene un producto específico por su ID.
POST /productos: Crea un nuevo producto.
PUT /productos/{id}: Actualiza un producto existente por su ID.
DELETE /productos/{id}: Elimina un producto específico por su ID. """

""" Realiza un programa que haga lo siguiente, controlando errores: """
import requests
url = "https://pokeapi.co/api/v2/pokemon/35/" # REALIZAR UNA PETICIÓN GET PARA OBTENER UNA PAGINA WEB


# SOLICITAR INFORMACION DE UN POKEMON CONCRETO, UTILIZANDO SU NOMBRE O NUMERO
try:
    x = requests.get(url)    
    # UNA PETICION HTTP DEVUELVE UNA RESPUESTA (codigo HTTP). SE VERIFICA QUE LA PETICION FUESE EXITOSA
    if x.status_code == 200:
        print("njdsnkfa")
    else:
        print(f"La petición no tuvo éxito. Código de error: {x.status_code}")

except Exception as e:
    print(f"Ocurrió un error al realizar la petición: {e}")

# CONTROLAR QUE EL NOMBRE DEL POKEMON ESTE EN MINUSCULAS

# MOSTRAR LOS SIGUIENTES DATOS DEL POKEMON: nombre, id, peso, altura y tipos de Pokémon (esto es una lista)