import sqlite3 #importo el módulo sqlite3 para trabajar con bases de datos SQLite

conexion=sqlite3.connect("bd1.db")
#Creo una conexión a la base de datos SQLite "bd1.db" y le asigno la variable "conexion".

precio=float(input("Ingrese un precio:"))
cursor=conexion.execute("select descripcion from articulos where precio<?", (precio, ))
filas=cursor.fetchall()
if len(filas)>0:
    for fila in filas:
        print(fila)
else:
    print("No existen artículos con un precio menor al ingresado.")
"""
En las líneas anteriores permito al usuario ingresar un precio, que lo almaceno en la variable "precio", y busco los 
artículos en la tabla "articulos" de la base de datos con un precio menor al ingresado. Si se encuentran artículos, se 
imprime su descripción. Si no se encuentran artículos, se imprime un mensaje de error con el texto "No existen 
artículos con un precio menor al ingresado".
"""
conexion.close() #En esta línea cierro la conexión a la base de datos SQLite.