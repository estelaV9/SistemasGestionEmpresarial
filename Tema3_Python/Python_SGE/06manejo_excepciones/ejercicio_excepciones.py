""" LANZAR EN ERRORES EN PYTHON SE UTILIZA raise """

# EXCEPCION CREADA POR NOSOTROS
class StrTypeError(Exception):
    pass

def process_params(parameters: list):
    # VERIFICA QUE LA LISTA TENGA AL MENOS 3 ELEMENTOS 
    if len(parameters) < 3:
        raise IndexError()  # LANZA UN ERROR DE IndexError SI NO HAY SUFICIENTES ELEMENTOS
    elif parameters[1] == 0:
        raise ZeroDivisionError()  # LANZAR UN ERROR DE ZeroDivisionError SI EL SEGUNDO ELEMENTO ES CERO
    elif type(parameters[2]) == str:
        raise StrTypeError("El tercer elemento no puede ser una cadena de texto")  # LANZAR UN ERROR StrTypeError SI EL TERCER ELEMENTO ES UNA CADENA
    
    # IMPRIME EL TERCER ELEMENTO DE LA LISTA
    print(parameters[2]) 
    
    # SE REALIZA UNA DIVISION Y MUESTRA EL RESULTADO
    print(parameters[0] / parameters[1]) 
    
    # SUMAR UN NUMERO A UNA CADENA (esto generará un TypeError)
    print(parameters[2] + 5)  # GENERA UN ERROR SI parameters[2] ES UNA CADENA

try:   
    # LLAMAR A LA FUNCION CON UNA LISTA DE PARAMETROS
    process_params([23, 2, 2, 45])
except IndexError as e:  # IndexError
    print("La lista debe tener más de 2 elementos")  # MENSAJE DE ERROR
except ZeroDivisionError as e:  # ZeroDivisionError
    print("El segundo elemento de la lista no puede ser cero")  
except StrTypeError as e:  # StrTypeError
    print(f"{e}")  
except Exception as e:  # OTRA EXCEPCION NO MANEJADA
    print(f"Se ha producido un error inesperado: {e}")
else:  # SI SE EJECUTA SIN EXCEPCIONES MUESTRA UN MENSAJE DE EXITO
    print("No se ha producido ningún error") 
finally:
    print("El programa finaliza sin detenerse")  # MENSAJE FINAL

print("Fin del programa") 