import mysql.connector

personas_db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'admin',
    database = 'personas_db'
)
#delete
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (8,)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('se ha eliminado el registro')
cursor.close()
personas_db.close()
