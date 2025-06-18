from modules.clases.auto import Auto
from modules.clases.cliente import Cliente
from modules.clases.concesionario import Concesionario

if __name__ == "__main__":
    autoland = Concesionario("AUTOLAND", "Av. La Marina 123, Lima")

    # Registrar vehículo
    auto1 = Auto("Toyota", "Corolla", 2023, 25000.0, "VIN001", 4, "Gasolina", True)
    autoland.agregar_vehiculo(auto1)

    # Registrar cliente
    cliente1 = Cliente("Juan", "Pérez", "12345678", "987654321", "juan@example.com")
    autoland.registrar_cliente(cliente1)

    # Venta
    exito = autoland.vender_vehiculo("VIN001", cliente1)
    if exito:
        print("Venta realizada exitosamente.")
    else:
        print("Vehículo no disponible.")

    # Reportes
    autoland.generar_reportes()
