import sqlite3 #importo el módulo sqlite3 para trabajar con bases de datos SQLite

conexion=sqlite3.connect("bd1.db")
#Creo una conexión a la base de datos SQLite "bd1.db" y le asigno la variable "conexion".

try:
    conexion.execute("""create table articulos (
                              codigo integer primary key autoincrement,
                              descripcion text,
                              precio real
                        )""")
    print("se creo la tabla articulos")
except sqlite3.OperationalError:
    print("La tabla articulos ya existe")
"""
En las lineas anteriores ejecuto una sentencia SQL para crear una nueva tabla llamada "articulos" con tres columnas: 
"codigo" (de tipo integer, clave primaria, con autoincremento), "descripcion" (de tipo texto) y "precio" (de tipo 
real).
Si la tabla anterior no existe, la sentencia se ejecutará correctamente y se imprimirá "se creo la tabla articulos".
Si la tabla ya existe, se producirá un error OperationalError y se imprimirá "La tabla articulos ya existe".
"""
conexion.close() #En esta línea cierro la conexión a la base de datos SQLite.