class Cliente:
    def __init__(self, nombre, apellido, dni, telefono, email):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__telefono = telefono
        self.__email = email
        self.__vehiculos_comprados = []

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos_comprados.append(vehiculo)

    def mostrar_info(self):
        return f"{self.__nombre} {self.__apellido} - {self.__dni} ({len(self.__vehiculos_comprados)} vehículo(s) comprados)"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def dni(self):
        return self.__dni

    @property
    def telefono(self):
        return self.__telefono

    @property
    def email(self):
        return self.__email
