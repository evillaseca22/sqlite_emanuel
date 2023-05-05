import sqlite3 #importo el módulo sqlite3 para trabajar con bases de datos SQLite

conexion=sqlite3.connect("bd1.db")
#Creo una conexión a la base de datos SQLite "bd1.db" y le asigno la variable "conexion".

cursor=conexion.execute("select codigo,descripcion,precio from articulos")
for fila in cursor:
    print(fila)
"""
En las líneas anteriores realizo una consulta SQL para obtener los datos de la tabla "articulos", los guardo en la 
variable "cursor" y los imprimo mediante un bucle for.
"""
conexion.close() #En esta línea cierro la conexión a la base de datos SQLite.