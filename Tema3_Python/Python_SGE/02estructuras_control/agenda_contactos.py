# EJERCICIO ADICIONAL AGENDA CONTACTOS
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
            print("********* BUSCAR CONTACTO *********")
            name_contact_search = input("¿Qué nombre de contacto desea buscar? ")


        case 2:
            print("********* INSERTAR CONTACTO *********")
            name_contact = input("Introduzca el nombre del contacto: ")
            phone_contact = input("Introduzca el numero de telefono del contacto (máximo 9 dígitos): ")
            # COMPRUEBA SI SOLO TIENE NUMEROS Y UN MAX DE 9 DIGITO
            # isdigit(): COMPRUEBA SI TODOS LOS CARACTERES EN LA CADENA SON NUMEROS
            if telefono.isdigit() and len(telefono) <= 9:
                print("Error: Debes introducir un número válido con máximo 9 dígitos. Intenta de nuevo.")
            my_contact_list.append(0)
        case 3:
            print("********* ACTUALIZAR CONTACTO *********")
            
           
        case 4:
            print("********* ELIMINAR CONTACTO *********")
          
        case 5:
            print("********* MOSTRAR CONTACTOS *********")
          
        case _:
            print("numero no valido")
          