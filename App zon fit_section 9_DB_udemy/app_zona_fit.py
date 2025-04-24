from cliente import Cliente

class ZonaFit:
    def __init__(self):
        pass
    cliente1 = ClienteDAO()
    def Menu(self):
        while True:
            try:
                print('''*** App Zon Fit ***
                Opciones:
                1. Listar clientes
                2. Agregar cliente
                3. Modificar datos de cliente
                4. Eliminar cliente
                5. Salir
                ''')
                opcion = int(input('Introduce una opcion (1-5): '))
                if opcion == 1:
                    pass
                if opcion == 2:
                    nombre = str(input('Introduce nombre: '))
                    apellido = str(input('Introduce apellido: '))
                    membresia = str(input('Introduce membresia (full/half): '))
                    nuevo_cliente = Cliente(nombre, apellido, membresia)
                    gym1.agregar.cliente(nuevo_cliente)
                elif opcion == 3:
                    pass
                elif opcion == 4:
                    pass
                elif opcion == 5:
                    print("Saliendo...")
                else:
                    print('Error. Introduce de nuevo')
            except Exception as e:
                print(f'Error details: {e}')