from modules.clases.vehiculo import Vehiculo


class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, precio, vin, num_puertas, tipo_combustible, es_automatico):
        super().__init__(marca, modelo, año, precio, vin)
        self.__num_puertas = num_puertas
        self.__tipo_combustible = tipo_combustible
        self.__es_automatico = es_automatico

    def calcular_seguro(self):
        return self.precio * 0.03

    def calcular_depreciacion(self):
        return self.precio * 0.15

    def obtener_tipo(self):
        return "Auto"


