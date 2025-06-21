# Importa la clase base Vehiculo, de la cual Auto va a heredar
from modules.clases.vehiculo import Vehiculo

# Define la clase Auto, que hereda de Vehiculo
class Auto(Vehiculo):
    # Constructor que recibe atributos del auto y llama al constructor de la clase base
    def __init__(self, marca, modelo, año, precio, vin, puertas, combustible, automatico):
        super().__init__(marca, modelo, año, precio, vin)  # Llama al constructor de Vehiculo
        self.__puertas = puertas              # Número de puertas del auto
        self.__combustible = combustible      # Tipo de combustible (Gasolina, Diésel, etc.)
        self.__automatico = automatico        # Booleano: True si es automático, False si es manual

    # Calcula el valor del seguro como el 5% del precio
    def calcular_seguro(self):
        return self.precio * 0.05

    # Calcula la depreciación como el 15% del precio
    def calcular_depreciacion(self):
        return self.precio * 0.15

    # Devuelve el tipo de vehículo (en este caso siempre "Auto")
    def obtener_tipo(self):
        return "Auto"

    # Muestra toda la información relevante del auto, incluyendo lo heredado y los nuevos atributos
    def mostrar_informacion(self):
        base = super().mostrar_informacion()  # Llama al método de la clase base
        return (f"{base} | Puertas: {self.__puertas} | "
                f"Combustible: {self.__combustible} | Automático: {'Sí' if self.__automatico else 'No'}")
