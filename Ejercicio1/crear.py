import sqlite3 #importo el módulo sqlite3 para trabajar con bases de datos SQLite
import os #importo el módulo os para trabajar con las funcionalidades del SO

def check_db(filename):
    return os.path.exists(filename)
#Aquí compruebo si existe el archivo con el que trabajaré

db_file = 'database.db'
schema_file = 'schema.sql'
"""
Aquí defino dos variables "db_file" y "schema_file" que almacenan los nombres de archivos de la base de datos y 
su esquema.
"""

if check_db(db_file):
    print('La base de datos ya existe.')
    exit(0)
"""
Aquí compruebo se la base de datos "database.db" existe o no, si existe se imprimirá por pantalla un texto de "La base
de datos ya existe" y luego saldrá del programa
"""

with open(schema_file, 'r') as rf:
    #Lee el esquema desde el archivo
    schema = rf.read()
#Aquí abro el archivo con los permisos de lectura "r"

with sqlite3.connect(db_file) as conn:
    print('Conexión creada!')
    # Ejecuta la búsqueda sql para crear la tabla
    conn.executescript(schema)
    print('Tabla creada! Insertando...')
    conn.executescript("""
                       insert into imagenes (nombre, size, fecha)
                       values
                       ('emanuel.jpg', 100, '2023-12-11'),
                       ('emanuelito.jpg', 200, '2023-01-08'),
                       ('emanuelon.jpg', 2100, '2023-07-17');
                       """)
    #Aquí añado los valores que están entre comillas a la tabla "imagenes"
    print('Valores insertados en la tabla!')
    #Imprimo un mensaje de "Valores Insertados en la tabla!"
print('Conexión cerrada!')
#Cierro la conexión mediante el texto "Conexión cerrada!"
