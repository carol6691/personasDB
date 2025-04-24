from udemy import nombre


class Cliente:
    contador_clientes = 0
    def __init__(self, nombre, apellido, membresia):
        Cliente.contador_clientes += 1
        self.id = Cliente.contador_clientes
        self.nombre = nombre
        self.apellido = apellido
        self.membresia = membresia
    def __str__(self):
        print(f'Datos del cliente: {self.id}, {self.nombre}, {self.apellido}, {self.membresia}')