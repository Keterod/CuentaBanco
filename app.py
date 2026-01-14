"""
Módulo principal de la aplicación bancaria.

Permite interactuar con cuentas bancarias mediante un menú de opciones
para realizar depósitos, retiros, transferencias y consultas de saldo.
"""

from cuenta_banco import CuentaBanco


def main():
    """
    Función principal de la aplicación.

    Muestra un menú interactivo para realizar operaciones bancarias
    sobre cuentas de ejemplo.
    """
    cuenta_origen = CuentaBanco("Titular Principal", 1000.0)
    cuenta_destino = CuentaBanco("Cuenta Destino", 500.0)
    while True:
        print("\n=== MENÚ DE OPERACIONES ===")
        print("1. Depósito")
        print("2. Retiro")
        print("3. Transferencia")
        print("4. Consulta de saldo")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        match opcion:
            case "1":  # Depósito
                try:
                    monto = float(input("Ingrese monto a depositar: "))
                    cuenta_origen.deposito_cuenta(monto)
                    print(f"Depósito exitoso. Saldo actual: {cuenta_origen.saldo_cuenta()}")
                except (ValueError, TypeError) as error:
                    print("Error:", error)

            case "2":  # Retiro
                try:
                    monto = float(input("Ingrese monto a retirar: "))
                    cuenta_origen.retiro_cuenta(monto)
                    print(f"Retiro exitoso. Saldo actual: {cuenta_origen.saldo_cuenta()}")
                except (ValueError, TypeError) as error:
                    print("Error:", error)

            case "3":  # Transferencia
                try:
                    monto = float(input("Ingrese monto a transferir: "))
                    cuenta_origen.transferencia_cuenta(monto, cuenta_destino)
                    print("Transferencia exitosa.")
                    print(f"Saldo cuenta origen: {cuenta_origen.saldo_cuenta()}")
                    print(f"Saldo cuenta destino: {cuenta_destino.saldo_cuenta()}")
                except (ValueError, TypeError) as error:
                    print("Error:", error)

            case "4":  # Consulta de saldo
                print(
                    f"Saldo cuenta origen ({cuenta_origen.titular}): "
                    f"{cuenta_origen.saldo_cuenta()}"
                    )
                print(
                    f"Saldo cuenta destino ({cuenta_destino.titular}): "
                    f"{cuenta_destino.saldo_cuenta()}"
                )
            case "5":  # Salir
                print("Saliendo del programa.")
                break

            case _:  # Opción inválida
                print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
