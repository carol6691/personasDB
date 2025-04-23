import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'personas_db'
)
cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas(nombre, apellido, edad) VALUES(%s, %s, %s)'
valores = ('Miguel', 'Gil', 36)
cursor.execute(sentencia_sql, valores)
personas_db.commit() # guardar los cambios en la db
print('se ha agregado a la db')
cursor.close()
personas_db.close()