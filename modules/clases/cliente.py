# Definición de la clase Cliente, que representa a un cliente de un concesionario
class Cliente:
    # Constructor: inicializa todos los atributos del cliente
    def __init__(self, nombre, apellido, dni, telefono, email):
        self.__nombre = nombre                            # Nombre del cliente (privado)
        self.__apellido = apellido                        # Apellido del cliente (privado)
        self.__dni = dni                                  # Documento Nacional de Identidad (privado)
        self.__telefono = telefono                        # Número de teléfono (privado)
        self.__email = email                              # Correo electrónico (privado)
        self.__vehiculos_comprados = []                   # Lista de vehículos comprados (privado)

    # Método para registrar un nuevo vehículo en la lista de compras del cliente
    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos_comprados.append(vehiculo)

    # Método que devuelve una cadena con la información resumida del cliente
    def mostrar_info(self):
        return f"{self.__nombre} {self.__apellido} - {self.__dni} ({len(self.__vehiculos_comprados)} vehículo(s) comprados)"

    # Propiedad para acceder al nombre del cliente de forma segura
    @property
    def nombre(self):
        return self.__nombre

    # Propiedad para acceder al apellido del cliente
    @property
    def apellido(self):
        return self.__apellido

    # Propiedad para acceder al DNI del cliente
    @property
    def dni(self):
        return self.__dni

    # Propiedad para acceder al número de teléfono
    @property
    def telefono(self):
        return self.__telefono

    # Propiedad para acceder al correo electrónico
    @property
    def email(self):
        return self.__email

