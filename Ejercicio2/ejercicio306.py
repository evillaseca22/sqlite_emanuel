import sqlite3 #importo el módulo sqlite3 para trabajar con bases de datos SQLite

conexion=sqlite3.connect("bd1.db")
#Creo una conexión a la base de datos SQLite "bd1.db" y le asigno la variable "conexion".

codigo=int(input("Ingrese el código de un artículo:"))
cursor=conexion.execute("select descripcion,precio from articulos where codigo=?", (codigo, ))
fila=cursor.fetchone()
if fila!=None:
    print(fila)
else:
    print("No existe un artículo con dicho código.")
"""
En las líneas anteriores permito que el usuario ingrese el código de un artículo, lo almaceno en la variable "código" y 
busco ese artículo en la tabla "articulos" de la base de datos utilizando una consulta SQL. Si se encuentra el artículo,
se muestra su descripción y precio. Si no se encuentra el artículo, se muestra un mensaje de error en la consola con
el mensaje "No existe un artículo con dicho código"
"""
conexion.close() #En esta línea cierro la conexión a la base de datos SQLite.