import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'personas_db'
)
# la sentencia select
cursor = personas_db.cursor()
cursor.execute('SELECT * FROM personas')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)
cursor.close()
personas_db.close()

