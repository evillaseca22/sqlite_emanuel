import sqlite3 #importo el módulo sqlite3 para trabajar con bases de datos SQLite

db_file = 'database.db' #Guardo el nombre de la base de datos en la variable "db_file"

with sqlite3.connect(db_file) as conn:
    cursor = conn.cursor() #Aquí creo un cursor
    cursor.execute("""
                   select * from imagenes
                   """)
    #Selecciono todas las columnas de la tabla "imagenes" y las guardo en el cursor
    for row in cursor.fetchall():
        nombre, size, fecha = row
        print(f'{nombre} {size} {fecha}')
        """
        Aquí itero sobre los resultados de la consulta y devuelvo una lista de tuplas, donde cada tupla representa una 
        fila de resultados.
        """