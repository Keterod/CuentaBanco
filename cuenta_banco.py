class CuentaBanco:
    def __init__(self, titular: str, saldo_inicial: float = 0.0):
        """
        Constructor de la clase CuentaBanco.

        :param titular: Nombre del titular de la cuenta
        :param saldo_inicial: Saldo inicial de la cuenta (por defecto 0.0)
        """
        self.titular = titular
        self.saldo = saldo_inicial

    def deposito_cuenta(self, monto: float):
        # Validamos que el monto sea un número (int o float)
        if not isinstance(monto, (int, float)):
            # Lanzamos TypeError si el tipo de dato no es correcto
            raise TypeError("El monto debe ser un número")

        # Validamos que el monto sea mayor que cero
        if monto <= 0:
            raise ValueError("El monto a depositar debe ser mayor que cero")

        self.saldo += monto

    def retiro_cuenta(self, monto: float):
        # Validamos que el monto sea un número
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")

        # Validamos que el monto sea mayor que cero
        if monto <= 0:
            raise ValueError("El monto a retirar debe ser mayor que cero")

        # Validamos que haya saldo suficiente
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")

        self.saldo -= monto

    def transferencia_cuenta(self, monto: float, cuenta_destino):
        # Validamos que el monto sea un número
        if not isinstance(monto, (int, float)):
            raise TypeError("El monto debe ser un número")

        # Validamos que el monto sea mayor que cero
        if monto <= 0:
            raise ValueError("El monto a transferir debe ser mayor que cero")

        # Validamos que haya saldo suficiente en la cuenta_origen
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")

        # Validamos que la cuenta destino sea un objeto CuentaBanco
        if not isinstance(cuenta_destino, CuentaBanco):
            raise TypeError("La cuenta destino debe ser una instancia de CuentaBanco")

        self.saldo -= monto
        cuenta_destino.saldo += monto

    def saldo_cuenta(self) -> float:
        return self.saldo
