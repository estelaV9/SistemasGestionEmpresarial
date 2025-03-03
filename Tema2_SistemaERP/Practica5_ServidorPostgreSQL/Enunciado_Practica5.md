# PRÁCTICA 5: SERVIDOR POSTGRESQL

## Paso 1: Abrir la máquina virtual Windows10_Odoo (clonada)  
Vamos a utilizar la herramienta **pgAdmin**:  

Buscarla en la instalación de Odoo en Windows 10. La herramienta **pgAdmin** es una de las herramientas más utilizadas para acceder a un servidor PostgreSQL (local o remoto) y se puede instalar en cualquier máquina. La podemos descargar de la página oficial ([www.pgadmin.org](https://www.pgadmin.org)); Odoo la incorpora en la instalación para Windows.  

En la instalación de Odoo en Windows, buscar **pgAdmin**. En primer lugar, hay que introducir una contraseña (*master password*) para pgAdmin.  

En la parte izquierda de la pantalla principal de pgAdmin se ven todos los servidores PostgreSQL a los que podemos acceder con esta herramienta, ya sean en la misma máquina o en máquinas remotas. En una misma máquina pueden coexistir varios servidores PostgreSQL, que deben escuchar por diferentes puertos.  

El servidor PostgreSQL instalado por Odoo aparece con una cruz roja que indica que no estamos conectados. Para conectarnos:  
- Hacer **doble clic** sobre él y nos pedirá la contraseña del usuario `openpg` (**openpgpwd**).  

Si nos situamos sobre la conexión **PostgreSQL** → Botón derecho del ratón → **Propiedades**  

---

## Exploración del servidor PostgreSQL  
En la parte izquierda de la pantalla de pgAdmin aparece el contenido del servidor PostgreSQL: bases de datos, esquemas, usuarios.  

- Un servidor PostgreSQL puede tener varios usuarios. En nuestro caso, el usuario `openpg` es el **superusuario** del servidor PostgreSQL.  
  - Botón derecho → Propiedades → Tiene privilegios totales.  
- **No confundir** los usuarios del SGBD con los usuarios del ERP.  
  - Los usuarios del ERP están almacenados en las tablas del ERP.  
  - El ERP usa un usuario de PostgreSQL (`openpg`) para acceder a la base de datos de la empresa.  

Si nos fijamos en las bases de datos, vemos que el servidor PostgreSQL tiene **2 bases de datos**:  

1. **postgres**  
   - Es la base de datos de mantenimiento del servidor y **no se puede eliminar**.  
2. **Base de datos del ERP**  
   - Una base de datos de PostgreSQL está compartimentada en **esquemas**.  
   - Al menos existe un esquema llamado **public**.  
   - Los contenidos de este esquema son accesibles para todos los usuarios con acceso a la base de datos.  
   - Cada empresa se corresponde con una base de datos que tiene toda la información en un único esquema público.  
   - Un esquema contiene: **dominios, tablas, vistas, funciones, secuencias y disparadores**.  

En la barra de direcciones de pgAdmin aparece:  

```
127.0.0.1:58229/browser
```
- PostgreSQL usa el puerto **5432** para gestionar conexiones a la base de datos.  
- El puerto **58229** es usado por **pgAdmin** para mostrar su interfaz web en el navegador.  
- Ambos están funcionando en paralelo con propósitos diferentes.  

Se puede ver un listado de las tablas, campos, descripción, etc.  

---

## Ejercicios  
### 1. Usando sentencias SQL, mostrar el contenido de la tabla `res_partner`, ordenado por el campo `id` en orden ascendente  
```sql
SELECT * FROM res_partner ORDER BY id ASC;
```

---

### 2. Cerrar PgAdmin y buscar el archivo `odoo.conf` (archivo de configuración de Odoo).  
Hacer una captura del mismo y explicar brevemente el contenido de los siguientes campos:  
- **`admin_passwd`** → Contraseña del administrador de Odoo.  
- **`addons_path`** → Ruta donde se encuentran los módulos adicionales de Odoo.  
- **`db_host`** → Servidor donde está alojada la base de datos PostgreSQL.  
- **`db_port`** → Puerto de conexión a PostgreSQL (por defecto **5432**).  
- **`db_user`** → Usuario de PostgreSQL utilizado por Odoo.  
- **`db_password`** → Contraseña del usuario de PostgreSQL para Odoo.  

>_Estela de Vega Martín | IES Ribera de Castilla 24/25_
