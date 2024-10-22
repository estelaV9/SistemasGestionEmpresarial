# Práctica 12: Proyecto Python
## Introducción
Realizar una aplicación en Python que englobe todos los contenidos vistos hasta ahora:
- `Bucles`.
- `Estructuras Condicionales`.
- `Funciones`.
- `Fucniones Lambda`.
- `Estructuras de datos`: **diccionarios**, **tuplas**, **sets**, **listas**...
- `Librerías`.
- `Clases`.
- `Manejo de excepciones`.
- `JSON` - `Peticiones HTTP`.<br>

Se desarrollará una <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/blob/master/Tema3_Python/deVega_Martin_Estela_Practica12_Proyecto_Python.pdf">memoria</a>
que contenga la `descripción general` del proyecto (los objetivos, entorno de trabajo, herramientas utilizadas...), la `documentación técnica`
donde incluya el diseño de la aplicación y las `conclusiones` y `posibles ampliaciones`.

## Proyecto
### Introducción
Está práctica se ha inspirado en el <a href="https://github.com/estelaV9/AccesoADatos/tree/master/Tema1_AccesoBDRelacionales/EjercicioFormularioFX">ejercicio</a> 
de JavaFx realizado en el módulo de **Acceso a Datos**. <br>
Se ha realizado un <a href="https://github.com/estelaV9/SistemasGestionEmpresarial/tree/master/Tema3_Python/Python_SGE/12proyecto_cubex">ejercicio</a>
en **Python** sobre la tienda de cubos **CubeX**. Este proyecto permite la gestión de prodyctos y usuarios en la tienda. 

### Estructura del proyecto
- `Caperta DAO`: contendrá las clases **user_dao** y **producto_dao** que tendrá los métodos CRUD de cada clase.
- `Carpeta Model`: contendrá las clases **user** y **product** que tendrá los atributos de cada clase, con su método `str()` y el método para convertir un objeto a un diccionario `to_dict()`.
- `Main`: contendrá el código principal, tendrá varias funciones para mayor legibilidad.


 


## Puntos Clave
### Función Lambda
Se crea una función lambda para filtrar que un número sea un dígito y positivo.
```python
validar_numero = lambda x: x.isdigit() and int(x) > 0
```
Por ejemplo: 
```python
# MOSTRAR LAS CATEGORIAS PARA QUE ELIJA
# RECORRER LA TUPLA CON LA FUNCION DE 'enumerate' LA CUAL DEVUELVE UN OBJETO ENUMERADO
for idx, category in enumerate(categories, 1):
    print(f"{idx}. {category}")

# SE VALIDA QUE INTRODUZCA BIEN EL NUMERO DE LA CATEGORIA
while True:
    try:
        category_option = int(input("Introduce el número de la categoría: "))
        # SE COMPRUEBA QUE LA CATEGORIA SEA MAYOR O IGUAL A 1 Y QUE SEA MENOR O IGUAL A LA LONGUITUD DE LA TUPLA
        if 1 <= category_option and category_option <= len(categories):
            categoria = categories[category_option - 1] # SI ES CORRECTO SE AÑADE LA OPCION
            break
        else:
            print("Elección inválida, elige un número válido.") # SI NO ES CORRECTO SALTA UN ERROR
    except ValueError:
        print("Debes ingresar un número válido.") # SE VALIDA QUE NO PONGA LETRAS
```


### Fichero JSON
Este ejercicio manipula los ficheros JSON, por lo que se crea una función para `leer` archivos. 
```python
# FUNCION PARA LEER ARICHIVO Y NO DUPLICAR CODIGO
def leer_archivo():
    try:
        with open('product.json', 'r') as file:
            products = json.load(file) # GUARDAR TODOS LOS PRODUCTOS EN UNA LISTA
    except (FileNotFoundError, JSONDecodeError):
        # SI NO SE HA ENCONTRADO ARCHIVO, INCIAR LA LISTA EN NULO
        products = []
    return products
```
Para crear un dato y `escribirlo` en el archivo, se guarda en una lista todos los datos y luego se sobreescribe con esos datos.
```python
with open('product.json', 'w') as file:
    json.dump(list_product_delete, file, indent=4)
```


Por ejemplo: 
```python
# FUNCION PARA ELIMINAR PRODUCTO POR NOMBRE
def delete_product(product_name):
    list_product_delete = leer_archivo()
    # BUSCAR NOMBRE PRODUCTO
    product_found = False  # SABER SI EL PRODUCTO EXISTE O NO

    for product in list_product_delete:
        if product['nombre'] == product_name:  # SI HAY UN PRODUCTO CON ESE NOMBRE SE ELIMINA
            list_product_delete.remove(product)  # ELIMINAR EL PRODUCTO DE LA LISTA
            product_found = True
            break  # SALIR DEL BUCLE

    if product_found:
        # SE GUARDA LA LISTA ACTUALIZADA DE VUELTA EN EL JSON
        with open('product.json', 'w') as file:
            json.dump(list_product_delete, file, indent=4)
        print(f"Producto '{product_name}' eliminado exitosamente.")
    else:
        print(f"No se encontró el producto '{product_name}'.")
```


#### Listar según atributos
```python
# FUNCION PARA LISTAR LOS PRODUCTOS DE UN USUARIO
def list_product_user(user_name):
  products = leer_archivo()
  # RECORRER LA LISTA
  for product in products:
      if product['owner'] == user_name:
          print(product.__str__()) # RETORNA LOS DATOS
```

#### Modificar datos
```python
 # SE MODIFICAN LOS ATRIBUTOS
product['nombre'] = new_name
product['precio'] = float(new_price)
product['stock'] = int(new_stock)
product['categoria'] = categoria
```

### Clases
#### - Método para convertir un objeto a diccionario
```python
def to_dict(self):
    # CONVERTIR UN OBJETO A UN DICCIONARIO
    return {
        "nombre": self.nombre,
        "precio": self.precio,
        "stock": self.stock,
        "categoria": self.categoria,
        "owner": self.owner
    }
```

#### - Método para devolver información 
```python
def __str__(self):
    # METODO PARA DEVOLVER INFORMACION SOBRE LOS PRODUCTOS
    return (f"Producto: {self.nombre}, Precio: {self.precio}€, "
            f"Stock: {self.stock} und, Categoria: {self.categoria}, Propietario: {self.owner}")
```


> [!NOTE]
> Para saber si un atributo es `nulo` se usa el `None`:
> ```python
> if email is not None: # SI NO ES NULO SE SALE DEL BUCLE (se encontro usuario)
>     break
> ```





---
<div align="center">
  <h2>¡Disfruta de la Práctica!</h2>
</div>

>_IES Ribera de Castilla 24/25._
