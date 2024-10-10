# ************************** EJERCICIO 9 *********************

""" Servicio web: Un servicio web es un sistema diseñado para soportar la interoperabilidad entre aplicaciones
a través de redes. Permite a diferentes aplicaciones comunicarse y compartir datos.

RESTful API: Es un tipo de API (Interfaz de Programación de Aplicaciones) que sigue los principios REST
(Transferencia de Estado Representacional). Utiliza métodos HTTP y es sin estado, lo que significa que cada
solicitud del cliente al servidor debe contener toda la información necesaria para entender y procesar
la solicitud.

Protocolo HTTP: El Protocolo de Transferencia de Hipertexto (HTTP) es un protocolo de comunicación
que se utiliza para la transmisión de información en la web. Es un protocolo sin estado que permite
la transferencia de datos entre un cliente (como un navegador web) y un servidor.

Peticiones HTTP: Son solicitudes que un cliente envía a un servidor para obtener información o
realizar alguna acción. Los métodos más comunes son GET, POST, PUT y DELETE.

Respuestas HTTP: Son los mensajes que un servidor envía de vuelta a un cliente después de procesar
una solicitud. Algunos códigos de respuesta comunes son:
- 200: OK. La solicitud fue exitosa y el servidor devolvió la información solicitada.
- 404: Not Found. El recurso solicitado no fue encontrado en el servidor.
- 500: Internal Server Error. Se produjo un error en el servidor al procesar la solicitud.

La librería de Python para realizar peticiones HTTP es `requests`. Para ello instalarlo 'pip install requests' """

import requests

# REALIZAR UNA PETICIÓN GET PARA OBTENER UNA PAGINA WEB
url = "https://github.com/estelaV9"

try:
    x = requests.get(url)
    
    # UNA PETICION HTTP DEVUELVE UNA RESPUESTA (codigo HTTP). SE VERIFICA QUE LA PETICION FUESE EXITOSA
    if x.status_code == 200:
        print("La petición fue exitosa. Contenido de la web:")
        print(x.text)  # DEVUELVE EL CODIGO FUENTE DE LA WEB; SE PODRIA VER REPRESENTADA
    else:
        print(f"La petición no tuvo éxito. Código de error: {x.status_code}")

except Exception as e:
    print(f"Ocurrió un error al realizar la petición: {e}")
