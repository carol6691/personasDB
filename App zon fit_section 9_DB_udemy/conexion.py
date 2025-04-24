import mysql.connector

class Conexion:
    def obtener_conexion_de_un_pool(self):
        cursopython_db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='admin',
            database='cursopython_db'
        )
        cursor = cursopython_db.cursor()