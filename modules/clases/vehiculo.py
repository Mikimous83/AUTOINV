from abc import ABC, abstractmethod

# Clase abstracta base que representa un vehículo genérico.
class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, año: int, precio: float, vin: str):
        # Atributos privados para encapsular la información del vehículo
        self.__marca = marca            # Marca del vehículo (ej. Toyota)
        self.__modelo = modelo          # Modelo del vehículo (ej. Corolla)
        self.__año = año                # Año de fabricación
        self.__precio = precio          # Precio en dólares
        self.__vin = vin                # Número de identificación vehicular único
        self.__vendido = False          # Estado del vehículo: vendido o no

    # Getter para la marca
    @property
    def marca(self):
        return self.__marca

    # Getter para el modelo
    @property
    def modelo(self):
        return self.__modelo

    # Getter para el año
    @property
    def año(self):
        return self.__año

    # Getter para el precio
    @property
    def precio(self):
        return self.__precio

    # Setter para actualizar el precio del vehículo con validación
    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a 0")

    # Getter para el VIN (número único de identificación del vehículo)
    @property
    def vin(self):
        return self.__vin

    # Método para marcar el vehículo como vendido
    def marcar_como_vendido(self):
        self.__vendido = True

    # Retorna True si el vehículo no ha sido vendido, False si ya se vendió
    def esta_disponible(self):
        return not self.__vendido

    # Retorna un string con toda la información del vehículo, incluyendo su estado
    def mostrar_informacion(self):
        estado = "Disponible" if not self.__vendido else "Vendido"
        return (f"{self.__marca} {self.__modelo} ({self.__año}) - ${self.__precio:.2f} | "
                f"VIN: {self.__vin} | Estado: {estado}")

    # Métodos abstractos que deberán implementarse en las clases hijas
    @abstractmethod
    def calcular_seguro(self):

        pass

    @abstractmethod
    def calcular_depreciacion(self):

        pass

    @abstractmethod
    def obtener_tipo(self):

        pass
