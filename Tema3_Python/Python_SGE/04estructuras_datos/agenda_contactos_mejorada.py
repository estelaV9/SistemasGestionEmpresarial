# EJERCICIO ADICIONAL AGENDA CONTACTOS MEJORADA UTILIZANDO FUNCIOENS
# FUNCIONES
def search_contact (name):
    if name in my_contact_list: # IF IN
        input(f"El usuario {name} esta registrado en la agenda")
    else:
        input(f"El usuario {name} NO esta registrado")

def insert_contact (name_contact, phone_contact):
    # COMPRUEBA SI SOLO TIENE NUMEROS Y UN MAX DE 9 DIGITO
    # isdigit(): COMPRUEBA SI TODOS LOS CARACTERES EN LA CADENA SON NUMEROS
    if phone_contact.isdigit() and len(phone_contact) < 9:
        print("Error: Debes introducir un número válido con máximo 9 dígitos. Intenta de nuevo.")
    my_contact_list.append(name_contact) # DENTRO DEL APPEND SE PONE EL PARAMETRO QUE QUEREMOS GUARDAR

def update_contact (original_contact, new_name):
    # ENCONTRAMOS EL INDICE DEL CONTACTO Y ACTUALIZAMOS
    index = my_contact_list.index(name_contact)
    my_contact_list[index] = name_update
    print(f"El contacto {name_contact} ha sido actualizado a {name_update}.")
    
def delete_contact (name_contact):
    if name_contact in my_contact_list: # IF IN
        my_contact_list.remove(name_contact)
        input(f"El usuario {name_contact} ha sido eliminado con exito")
    else:
        input(f"El usuario {name_contact_search} NO esta registrado")

def show_contact():
    for i in range(0,len(my_contact_list)):
        print(my_contact_list[i])



print("Bienvenido a Agenda. ¿Qué desea hacer?")
opcion = -1
my_contact_list = []
while(opcion != 0):
    print("\n1-Buscar contacto.",
          "\n2-Insertar contacto.",
          "\n3-Actualizar contacto.",
          "\n4-Eliminar contacto.",
          "\n5-Mostrar todos los contacto.",
          "\n0-Salir.")
    opcion = int(input("Introduzca una opcion: "))
    match opcion:
        case 1:
            print("\n********* BUSCAR CONTACTO *********")
            name_contact_search = input("¿Qué nombre de contacto desea buscar? ")
            search_contact(name_contact_search)

        case 2:
            print("\n********* INSERTAR CONTACTO *********")
            name_contact = input("Introduzca el nombre del contacto: ")
            phone_contact = input("Introduzca el numero de telefono del contacto (máximo 9 dígitos): ")
            insert_contact(name_contact, phone_contact)

        case 3:
            print("\n********* ACTUALIZAR CONTACTO *********")
            name_contact = input("Introduza el nombre del contacto a actualizar: ")
            name_update = input("Introduzca el nuevo nombre del contacto: ")
            update_contact(name_contact, name_update)

        case 4:
            print("\n********* ELIMINAR CONTACTO *********")
            name_contact = input("Introduzca el nombre del contacto a eliminar: ")
            delete_contact(name_contact)

        case 5:
            print("\n********* MOSTRAR CONTACTOS *********")
            show_contact()

        case _:
            print("numero no valido")

print("¡Hasta pronto!")
