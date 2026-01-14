"""
Módulo cuenta_banco

Contiene la definición de la clase CuentaBanco que permite realizar
operaciones básicas bancarias como depósito, retiro, transferencia y consulta de saldo.
"""

class CuentaBanco:
    """
    Representa una cuenta bancaria con operaciones básicas.

    Atributos:
        titular (str): Nombre del titular de la cuenta.
        saldo (float): Saldo actual de la cuenta.
    """
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """
        Constructor de la clase CuentaBanco.

        :param titular: Nombre del titular de la cuenta
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto 0.0)
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def deposito_cuenta(self, monto: float):
        """
        Realiza un depósito en la cuenta.

        :param monto: Cantidad de dinero a depositar.
        :raises TypeError: Si el monto no es un número.
        :raises ValueError: Si el monto es menor o igual a cero.
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")

        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero")

        self.saldo += monto

    def retiro_cuenta(self, monto: float):
        """
        Realiza un retiro de la cuenta.

        :param monto: Cantidad de dinero a retirar.
        :raises TypeError: Si el monto no es un número.
        :raises ValueError: Si el monto es menor o igual a cero.
        :raises ValueError: Si no hay saldo suficiente.
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")

        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero")

        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= monto

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        """
        Transfiere dinero a otra cuenta bancaria.

        :param monto: Cantidad de dinero a transferir.
        :param cuenta_destino: Cuenta que recibirá el dinero.
        :raises TypeError: Si el monto no es un número o la cuenta destino no es válida.
        :raises ValueError: Si el monto es menor o igual a cero o no hay saldo suficiente.
        """
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")

        if monto <= 0:
            raise ValueError("El monto a transferir debe ser mayor que cero")

        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")

        if not isinstance(cuenta_destino, CuentaBanco):
            raise TypeError("La cuenta destino debe ser una instancia de CuentaBanco")

        self.saldo -= monto
        cuenta_destino.saldo += monto

    def saldo_cuenta(self) -> float:
        """
        Devuelve el saldo actual de la cuenta.

        :return: Saldo disponible.
        """
        return self.saldo
