from modules.clases.vehiculo import Vehiculo

class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, precio, vin, puertas, combustible, automatico):
        super().__init__(marca, modelo, año, precio, vin)
        self.__puertas = puertas
        self.__combustible = combustible
        self.__automatico = automatico

    def calcular_seguro(self):
        return self.precio * 0.05

    def calcular_depreciacion(self):
        return self.precio * 0.15

    def obtener_tipo(self):
        return "Auto"

    def mostrar_informacion(self):
        base = super().mostrar_informacion()
        return (f"{base} | Puertas: {self.__puertas} | "
                f"Combustible: {self.__combustible} | Automático: {'Sí' if self.__automatico else 'No'}")


