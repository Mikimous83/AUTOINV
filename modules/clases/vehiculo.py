from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, año: int, precio: float, vin: str):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__precio = precio
        self.__vin = vin
        self.__vendido = False

    # Getters
    @property
    def marca(self):
        return self.__marca

    @property
    def modelo(self):
        return self.__modelo

    @property
    def año(self):
        return self.__año

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a 0")

    @property
    def vin(self):
        return self.__vin

    def marcar_como_vendido(self):
        self.__vendido = True

    def esta_disponible(self):
        return not self.__vendido

    def mostrar_informacion(self):
        estado = "Disponible" if not self.__vendido else "Vendido"
        return (f"{self.__marca} {self.__modelo} ({self.__año}) - ${self.__precio:.2f} | "
                f"VIN: {self.__vin} | Estado: {estado}")

    @abstractmethod
    def calcular_seguro(self):
        pass

    @abstractmethod
    def calcular_depreciacion(self):
        pass

    @abstractmethod
    def obtener_tipo(self):
        pass
