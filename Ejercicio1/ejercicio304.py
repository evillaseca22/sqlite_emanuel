import sqlite3 #importo el módulo sqlite3 para trabajar con bases de datos SQLite

conexion=sqlite3.connect("bd1.db")
#Creo una conexión a la base de datos SQLite "bd1.db" y le asigno la variable "conexion".

conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("naranjas", 23.50))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("peras", 34))
conexion.execute("insert into articulos(descripcion,precio) values (?,?)", ("bananas", 25))
"""
Las líneas anteriores ejecutan sentencias SQL para insertar datos en la tabla "articulos". Cada una utiliza el signo de 
interrogación (?) para indicar los valores que se deben insertar, los cuales se pasan como una tupla separada por comas 
en el segundo argumento de la función.
"""
conexion.commit() #Aquí guardo los cambios hechos en la base de datos
conexion.close() #En esta línea cierro la conexión a la base de datos SQLite.