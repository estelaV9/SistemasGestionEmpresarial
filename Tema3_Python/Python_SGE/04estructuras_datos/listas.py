# ****************** LISTAS *********************
""" INVESTIGAR LA ESTRUCTURA DE DATOS LISTAS """
my_list_example = []
# INSERCION
name_insert = input("Inserte un nombre para el array: ")
my_list_example.append(name_insert)

# BORRADO
name_delete = input("Inserte el nombre que desee eliminar: ")
if name_delete in my_list_example:
    my_list_example.remove(name_delete)
    print("Se ha eliminado correctamente")
else:
    print("Ese nombre NO esta en la lista")

# ACTUALIZACION
name_original = input("Ingrese el nombre al que le quiera modificar: ")
new_name = input("Ingrese el nombre nuevo que quiera darle: ")
index = my_list_example.index(name_original)
my_list_example[index] = new_name
print("Se actualizo correctamente")

""" otra forma """
my_list_example[1]
print(my_list_example[1])
my_list_example[1] = "Pedro"
print(my_list_example)

# ORDENACION
my_list_example.sort() # POR DEFECTO LO ORDENA ALFABETICAMENTE
print(my_list_example)
print(type(my_list_example)) # AÑADIR EL TIPO DE CLASE 
