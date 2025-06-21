from modules.clases.auto import Auto

class Concesionario:
    def __init__(self, nombre, direccion):
        # Atributos privados para almacenar información del concesionario
        self.__nombre = nombre
        self.__direccion = direccion
        self.__vehiculos = []  # Lista para guardar los vehículos disponibles o vendidos
        self.__clientes = []   # Lista para guardar los clientes registrados

    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un nuevo vehículo al inventario del concesionario.
        """
        self.__vehiculos.append(vehiculo)

    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el concesionario.
        """
        self.__clientes.append(cliente)

    def vender_vehiculo(self, vin, cliente):
        """
        Busca un vehículo por su VIN (número de identificación del vehículo),
        verifica si está disponible y lo marca como vendido si lo está.
        Luego lo asigna al cliente.
        """
        for v in self.__vehiculos:
            # Acceso al atributo privado __vin usando nombre de clase base _Vehiculo__vin
            if v.esta_disponible() and v._Vehiculo__vin == vin:
                v.marcar_como_vendido()     # Marca el vehículo como vendido
                cliente.agregar_vehiculo(v) # Asocia el vehículo al cliente
                return True
        return False  # Si no se encuentra un vehículo disponible con ese VIN

    def generar_reportes(self):
        """
        Imprime por consola un resumen de todos los vehículos y clientes.
        Útil para revisiones rápidas desde consola.
        """
        print("\n--- REPORTE DE VEHÍCULOS ---")
        for v in self.__vehiculos:
            print(v.mostrar_informacion())

        print("\n--- REPORTE DE CLIENTES ---")
        for c in self.__clientes:
            print(c.mostrar_info())
