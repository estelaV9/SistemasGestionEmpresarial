# HACER UN PRINT CON LA ESTRUCTURA IF
print("*********** ESTRUCTURA IF-ELSE **********")
number = int(input("Ingrese un numero: "))
if(number < 0) : 
    print("El número " + str(number) + " es negativo")
else:
   print(f"El número " + str(number) + " es positivo") 

# HACER UN PRINT CON LA ESTRUCTURA CASE
print("\n*********** ESTRUCTURA CASE **********")
day = int(input("Ingrese el dia de la semana: "))

# CREAMOS UNA FUNCION QUE RECIBA UN DIA
def dias_de_la_semana(day):
    # EN EL BLOQUE DE LA FUNCION, CREAMOS UN MATCH A 
    # DIA QUE RETORNARA LOS VALORES ESTABLECIDOS
    match day:
        case 1:
            return "Lunes"
        case 2:
            return "Martes"
        case 3:
            return "Miércoles"
        case 4:
            return "Jueves"
        case 5:
            return "Viernes"
        case 6:
            return "Sábado"
        case 7:
            return "Domingo"
        case _:
            return "Día inválido"

# SEGUN EL DIA QUE PONGA EL USUARIO, DEVOLVERA EL NOMBRE 
# DEL DIA DE LA SEMANA
print("El dia de la semana es: " , dias_de_la_semana(day)) 





