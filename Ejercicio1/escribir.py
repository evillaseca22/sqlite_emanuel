import sqlite3 #importo el módulo sqlite3 para trabajar con bases de datos SQLite

db_filename = 'database.db' #Guardo el nombre de la base de datos en la variable "db_filename"

def display_table(conn):
    cursor = conn.cursor()
    cursor.execute('select nombre, size, fecha from imagenes;')
    for nombre, size, fecha in cursor.fetchall():
        print(nombre, size, fecha)
"""
Aquí creo un cursor a partir de la conexión y ejecuto una consulta SQL para seleccionar los campos nombre, size y 
fecha de la tabla imagenes. Luego, con un bucle for, itero a través de estos resultados y los imprimo.
"""

with sqlite3.connect(db_filename) as conn1:
    print('Antes de los cambios:')
    display_table(conn1)
    """
    Guardo la conexión a la base de datos SQLite en la variable "conn1", luego imprimo un texto de "Antes de los 
    cambios:" y muestro los datos actuales de la tabla imagenes
    """

    cursor1 = conn1.cursor()
    cursor1.execute("""
    insert into imagenes (nombre, size, fecha)
    values ('Emanuelito.png', 2000, '2020-02-20');
    """)
    #Aquí creo un cursor e inserto un nuevo registro en la tabla imagenes

    print('\nDespués de los cambios en conn1:')
    display_table(conn1)
    #Imprimo un texto de "Después de los cambios en conn1:" y muestro los datos actualizados de la tabla imagenes

    print('\nAntes del commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)
    """
    Imprimo un teto de "Antes del commit", guardo la conexión sql en la variable "conn2" y muestro los datos actuales
    de la tabla "imagenes"
    """

    # Comit de la primera conexión
    conn1.commit() #Confirmo los cambios
    print('\nAfter commit:')
    with sqlite3.connect(db_filename) as conn3:
        display_table(conn3)
        #muestro los datos actualizados de la tabla imagenes después del commit

    cursor1.execute("""
    insert into imagenes (nombre, size, fecha)
    values ('Emanuel.png', 100, '2020-01-18');
    """)
    #Inserto nuevos registros en la tabla imagenes

    print('\nAntes del commit:')
    with sqlite3.connect(db_filename) as conn2:
        display_table(conn2)
    #Imprimo un texto de "Antes del commit" y muestro los datos actuales de la tabla antes del commit

    #Revierto los cambios antes de la confirmación de conn1
    conn1.rollback() #Aquí deshago la inserción del registro realizado previamente en la tabla imagenes.
    print('\nDespués de la conexión 1 (rollback):')
    with sqlite3.connect(db_filename) as conn4:
        display_table(conn4)
    """
    Imprimo un texto de "Después de la conexión 1 (rollback):" y muestro  los datos sin el registro insertado 
    anteriormente, ya que el rollback deshizo los cambios.
    """