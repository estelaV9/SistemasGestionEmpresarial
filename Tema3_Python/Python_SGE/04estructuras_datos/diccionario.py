# ********************** DICCIONARIO **************************
""" Se usan {}, pero en formato de los datos que se guarda es clave:valor.
La clave es el punto de acceso para llegar a un dato """

my_dict: dict = { "name": "Ana", # dict: ES TIPO DICCIONARIO
                 "surname": "Alonso",
                 "level": "2DAM"    
                }

# INSERTAR ELEMENTO 
print(my_dict["name"]) # SE ACCEDE AL DATO QUE QUEREMOS INSERTAR POR CLAVE
my_dict["email"] = "example@gmail.com" # SI NO EXISTE LA CLAVE, SE INSERTA
print(my_dict)

# ELIMINAR ELEMENTO
del my_dict["email"]
print(my_dict)

# ACTUALIZAR ELEMENTOS
my_dict["age"] = 54
print(my_dict)

# ORDENACION: SE USA LA OPERACION ITEMS QUE DEVUELVE EL CONJUNTO DE CLAVES Y VALORES
my_dict = dict(sorted(my_dict.items()))
print(my_dict)