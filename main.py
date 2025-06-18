from modules.clases.auto import Auto
from modules.clases.cliente import Cliente
from modules.clases.concesionario import Concesionario

def mostrar_menu():
    print("\n=== MENÚ AUTOLAND ===")
    print("1. Registrar vehículo")
    print("2. Registrar cliente")
    print("3. Vender vehículo")
    print("4. Generar reportes")
    print("5. Salir")


def main():
    autoland = Concesionario("AUTOLAND", "Av. La Marina 123, Lima")
    clientes = {}

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            año = int(input("Año: "))
            precio = float(input("Precio: "))
            vin = input("VIN: ")
            puertas = int(input("Número de puertas: "))
            combustible = input("Tipo de combustible: ")
            automatico = input("¿Es automático? (s/n): ").lower() == 's'
            auto = Auto(marca, modelo, año, precio, vin, puertas, combustible, automatico)
            autoland.agregar_vehiculo(auto)
            print("Vehículo registrado con éxito.")

        elif opcion == "2":
            dni = input("DNI: ")
            if dni in clientes:
                print("Cliente ya registrado.")
            else:
                nombre = input("Nombre: ")
                apellido = input("Apellido: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                cliente = Cliente(nombre, apellido, dni, telefono, email)
                autoland.registrar_cliente(cliente)
                clientes[dni] = cliente
                print("Cliente registrado correctamente.")

        elif opcion == "3":
            vin = input("Ingrese VIN del vehículo a vender: ")
            dni = input("DNI del cliente comprador: ")
            cliente = clientes.get(dni)
            if cliente:
                if autoland.vender_vehiculo(vin, cliente):
                    print("Venta realizada con éxito.")
                else:
                    print("Error: Vehículo no disponible o VIN incorrecto.")
            else:
                print("Cliente no encontrado. Regístrelo primero.")

        elif opcion == "4":
            autoland.generar_reportes()

        elif opcion == "5":
            print("Saliendo del sistema AUTOLAND...")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
