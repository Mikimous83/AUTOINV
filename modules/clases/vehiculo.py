from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca: str, modelo: str, año: int, precio: float, vin: str):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__precio = precio
        self.__vin = vin
        self.__vendido = False

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            raise ValueError("El precio debe ser mayor a 0")

    def marcar_como_vendido(self):
        self.__vendido = True

    def esta_disponible(self):
        return not self.__vendido

    def mostrar_informacion(self):
        return f"{self.__marca} {self.__modelo} ({self.__año}) - ${self.__precio}"

    @abstractmethod
    def calcular_seguro(self):
        pass

    @abstractmethod
    def calcular_depreciacion(self):
        pass

    @abstractmethod
    def obtener_tipo(self):
        pass