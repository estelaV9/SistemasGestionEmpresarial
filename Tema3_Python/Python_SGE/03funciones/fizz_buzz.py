# *********************** PRACTICA 8 *********************
""" CREAR UNA FUNCION QUE RECIBA DOS PARAMETROS DE TIPO CADENA
Y RETORNE UN NUMERO.
LA FUNCION IMPRIMIRA TODOS LOS NUMEROS DE 1 AL 100. TENIENDO EN CUENTA QUE:
    - SI EL NUMERO ES %3, MUESTRA FIZZ
    - SI ES %5, MUESTRA BUZZ
    - SI ES %3%5, MUESTRA FIZZ+BUZZ
LA FUNCION RETORNARA EL NUMERO DE VECES QUE SE HA IMPRESO EL NUMERO
EN LUEGAR DE LOS TEXTOS"""
def return_number(text_one, text_two):
    contador = 0
    for i in range(1, 100):
        if i% 5 == 0 and i % 3 == 0:
            print(f"{text_one}_{text_two}")
        elif i % 5 == 0:
            print(text_two)
        elif i % 3 == 0:
            print(text_one)
        else:
            print(i)
            contador+=1
    return contador

print("Han aparecido: ", return_number("FIZZ", "BUZZ"), " numeros")
