# Práctica 7: Ejercicios Iniciales de Python
## Ejercicio 0: <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/00sintaxis/sintaxis_variables.py">Sintaxis y variables</a>
1. Sintaxis y variables
``` python
  my_string = "My String"; # CREAR UNA CADENA DE TEXTO
  my_number = 12; # CREAR UN NUMERO ENTERO
  my_decimal = 23.33; # CREAR UN NUMERO DECIMAL
  my_boolean = True; # CREAR UN BOOLEANO (Bool)
```

2. Imprimir por terminal el contenido de las variables.
   - De forma concatenada con `+` (hay que poner `str()` a las variables)
     ``` python
     print("******* VARIABLES PYTHON *******" +
      "\nCadena de texto: " + my_string + 
      "\nNumero Entero: " + str(my_number) +
      "\nNumero Decimal: " + str(my_decimal) +
      "\nBooleano: " + str(my_boolean) + "\n")
     ```
   - De forma concatenada con `,` (**no** es necesario poner `str()`)
     ``` python
     print("******* VARIABLES PYTHON *******" ,
      "\nCadena de texto: " , my_string ,
      "\nNumero Entero: " , my_number ,
      "\nNumero Decimal: " , my_decimal ,
      "\nBooleano: " , my_boolean , "\n")
     ```
   - En una sola línea.
     ``` python
     print(my_string)
     ```
3. Imprimir el tipo de cada variable.
   ``` python
     print(type(my_string))
     ```

## Ejercicio 1: <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/01operadores/operadores.py">Operadores</a>
1. `print(f"Suma: 8 + 14 = {8 + 14}")`
Esa linea permiten incluir expresiones directamente dentro de una cadena, 
que serán evaluadas y sustituidas en el momento de la ejecución.

2. Obtener un texto escrito por teclado --> `input()`
  ``` python
  nombre = input("Escribe tu nombre: ")
  print(f"Hola, {nombre}!")
  ```
3. Operadores
   - de Comparación
     ``` python
     """ Estos operadores comparan dos valores y devuelven True o False 
      dependiendo de la relación entre los valores."""
      a = 5
      b = 3
      
      print(f"{a} == {b} ->", a == b)  # == 
      print(f"{a} != {b} ->", a != b)  # != 
      print(f"{a} > {b} ->", a > b)    # > 
      print(f"{a} < {b} ->", a < b)    # < 
      print(f"{a} >= {b} ->", a >= b)  # >=  
      print(f"{a} <= {b} ->", a <= b)  # <= 
     ```
     
   - Lógicos
     ``` python
     """ Estos operadores permiten combinar expresiones que devuelven valores booleanos. """
      x = True
      y = False
      
      print(f"{x} and {y} ->", x and y)  # AND (ambos deben ser True)
      print(f"{x} or {y} ->", x or y)    # OR (al menos uno debe ser True)
      print(f"not {x} ->", not x)        # NOT (invierte el valor lógico)
     ```
     
   - de Asignación
     ``` python
     """ Estos operadores asignan un valor a una variable y también permiten hacer 
        operaciones matemáticas combinadas con la asignación. """
        z = 10
        print(f"z = {z}")   # Asignación simple
        z += 5  # SUMA Y ASIGNA 
        print(f"z += 5 -> {z}")
        z -= 3  # RESTA Y ASIGNA
        print(f"z -= 3 -> {z}")
        z *= 2  # MULTIPLICA Y ASIGNA
        print(f"z *= 2 -> {z}")
        z /= 4  # DIVIDE Y ASIGNA
        print(f"z /= 4 -> {z}")
        z %= 3  # MODULO Y ASIGNA
        print(f"z %= 3 -> {z}")
     ```
4. <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/01operadores/calculadora.py">Calculadora</a>
   Pedir por teclado 2 números y muestre por pantalla estas operaciones aritméticas:
    - Suma.
    - Resta.
    - Multiplicación.
    - División.
    - Resto.

    ``` python
    print("************* CALCULADORA ****************")
    print("Ingrese dos numeros por teclado")
    # HAY QUE CONVERTIR EL TIPO DE DATO QUE VA A SER (en este caso int())
    num_one = int(input("Ingrese el primer numero: ")) 
    num_two = int(input("Ingrese el primer numero: "))
    
    print("\n************** RESULTADOS *************"
         f"\nSuma: {num_one + num_two}",
         f"\nResta: {num_one - num_two}",
         f"\nMultiplicación: {num_one * num_two}",
         f"\nDivisión: {float(num_one / num_two)}",
         f"\nResto: {num_one % num_two}") 
    ```
    
## Ejercicio 2: <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/02estructuras_control/condicionales.py">Estructuras de control</a>
1. Hacer un `print` con la estructura `if`
``` python
print("*********** ESTRUCTURA IF-ELSE **********")
number = int(input("Ingrese un numero: "))
if(number < 0) : 
    print("El número " + str(number) + " es negativo")
else:
   print(f"El número " + str(number) + " es positivo") 
```

2. Hacer un `print` con la estructura `case`
``` python
# HACER UN PRINT CON LA ESTRUCTURA CASE
print("\n*********** ESTRUCTURA CASE **********")
day = int(input("Ingrese el dia de la semana: "))

# CREAMOS UNA FUNCION QUE RECIBA UN DIA
def dias_de_la_semana(day):
    # EN EL BLOQUE DE LA FUNCION, CREAMOS UN MATCH A DIA QUE RETORNARA LOS VALORES ESTABLECIDOS
    match day:
        case 1: return "Lunes"
        case 2: return "Martes"
        case 3: return "Miércoles"
        case 4: return "Jueves"
        case 5: return "Viernes"
        case 6: return "Sábado"
        case 7: return "Domingo"
        case _: return "Día inválido"

# SEGUN EL DIA QUE PONGA EL USUARIO, DEVOLVERA EL NOMBRE DEL DIA DE LA SEMANA
print("El dia de la semana es: " , dias_de_la_semana(day)) 
```
  
3. Hacer un `print` con un <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/02estructuras_control/bucles.py">bucle</a> `for`
``` python
# HACER UN PRINT CON LA ESTRUCTURA ITERATIVA FOR
print("*********** ESTRUCTURA FOR **********")
for i in range(1, 11): # range(1, 11) genera los números del 1 al 10
    print(i)
```

4. Hacer un `print` con un bucle `while`
``` python
# HACER UN PRINT CON LA ESTRUCTURA ITERATIVA FOR
print("\n*********** ESTRUCTURA WHILE **********")
number = 0
print("Introduzca 1 para salir de la aplicacion")
while(number != 1):
    number = int(input())
print("Hasta pronto!")
```


## Ejercicio 3: <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/tree/master/Tema3_Python/Python_SGE/03funciones">Funciones</a>
1. <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/03funciones/funciones.py">Explicación</a> sobre las funciones en **Python**.
``` python
  def greet():
      print("Holaa!!, bienvenidos al curso 24/25") 
  greet()
```
2. Ejercicio <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/03funciones/fizz_buzz.py">fizz_buzz</a> que según el módulo de 3/5 o los dos muestre un parámetro y otro, o los dos.

## Ejercicio 4: <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/tree/master/Tema3_Python/Python_SGE/04estructuras_datos">Estructuras de Datos</a>
1. <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/04estructuras_datos/agenda_contactos_mejorada.py">Agenda mejorada</a> de contactos.
2. Funcionamiento de <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/Python_SGE/04estructuras_datos/listas.py">listas</a>.
   - Insercción.
   - Borrado.
   - Actualización.
   - Ordenación.




---
<div align="center">
  <h2>¡Disfruta de los ejercicios!</h2>
</div>

>_IES Ribera de Castilla 24/25._
