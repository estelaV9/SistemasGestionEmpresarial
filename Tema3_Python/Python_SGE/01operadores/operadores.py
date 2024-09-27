""" Interpolación: f-strings permiten incluir variables directamente dentro de una cadena, 
que serán evaluadas y sustituidas en el momento de la ejecución. """
print(f"Suma: 8 + 14 = {8 + 14}")

# OBTENER UN TEXTO ESCRITO POR TECLADO
nombre = input("Escribe tu nombre: ")
print(f"Hola, {nombre}!")

# OPERADORES DE COMPARACION 
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

# OPERADORES LOGICOS
""" Estos operadores permiten combinar expresiones que devuelven valores booleanos. """
x = True
y = False

print(f"{x} and {y} ->", x and y)  # AND (ambos deben ser True)
print(f"{x} or {y} ->", x or y)    # OR (al menos uno debe ser True)
print(f"not {x} ->", not x)        # NOT (invierte el valor lógico)

# OPERADORES DE ASIGNACION
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
