from modules.clases.auto import Auto
class Concesionario:
    def __init__(self, nombre, direccion):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__vehiculos = []
        self.__clientes = []

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def registrar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def vender_vehiculo(self, vin, cliente):
        for v in self.__vehiculos:
            if v.esta_disponible() and v._Vehiculo__vin == vin:
                v.marcar_como_vendido()
                cliente.agregar_vehiculo(v)
                return True
        return False

    def generar_reportes(self):
        print("\n--- REPORTE DE VEHÍCULOS ---")
        for v in self.__vehiculos:
            print(v.mostrar_informacion())

        print("\n--- REPORTE DE CLIENTES ---")
        for c in self.__clientes:
            print(c.mostrar_info())