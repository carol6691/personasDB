from cliente import Cliente
from conexion import Conexion
import mysql.connector

class ClienteDAO:
    def __init__(self, cliente):
        self.cliente = cliente
    def listar_cliente(self):
        Conexion.obtener_conexion_de_un_pool()
        cursor.execute('SELECT * FROM clientes')
        resultado = cursor.fetchall()
        for cliente in resultado:
            print(cliente)
        cursor.close()
        cursopython_db.close()
    def agregar_cliente(self, cliente):
        Conexion.obtener_conexion_de_un_pool()
        sentencia_sql = 'INSERT INTO clientes (id, nombre, apellido, membresia) VALUES(%s, %s, %s)'
        valores = ('id', 'nombre', 'apellido', 'membresia')
        cursor.execute(sentencia_sql, valores)
        cursopython_db.commit()  # guardar los cambios en la db
        print('se ha agregado a la db')
        cursor.close()
        cursopython_db.close()
    def actualizar_cliente(self):
        Conexion.obtener_conexion_de_un_pool()
        sentencia_sql = 'UPDATE clientes SET nombre=%s, APELLIDO=%s, membresia=%s WHERE id=%s'
        valores = ('nombre', 'apellido', 'membresia', 'id')
        cursor.execute(sentencia_sql, valores)
        cursopython_db.commit()
        print('se ha modificado')
        cursor.close()
        cursopython_db.close()
    def eliminar_cliente(self):
        Conexion.obtener_conexion_de_un_pool()
        sentencia_sql = 'DELETE FROM clientes WHERE id=%s'
        valores = ('id',)
        cursor.execute(sentencia_sql, valores)
        cursopython_db.commit()
        print('se ha eliminado el registro')
        cursor.close()
        cursopython_db.close()
