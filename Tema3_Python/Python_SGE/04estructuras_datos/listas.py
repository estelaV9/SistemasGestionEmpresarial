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

# ORDENACION
for i in range (0, len(my_list_example)):
    print(my_list_example[i])
