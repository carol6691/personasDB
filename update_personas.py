import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'personas_db'
)
#update
cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, APELLIDO=%s, EDAD=%s WHERE id=%s'
valores = ('Pili', 'Requesens', 60, 10)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('se ha modificado')
cursor.close()
personas_db.close()
