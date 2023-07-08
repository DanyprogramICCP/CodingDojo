class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial

    def deposito(self, monto):
        """
        Realiza un depósito en la cuenta bancaria.
        """
        self._saldo += monto
        print(f"Depósito de {monto} realizado con éxito.")

    def retiro(self, monto):
        """
        Realiza un retiro de la cuenta bancaria.
        """
        if self._saldo >= monto:
            self._saldo -= monto
            print(f"Retiro de {monto} realizado con éxito.")
        else:
            print("Saldo insuficiente.")

    def mostrar_saldo(self):
        """
        Muestra el saldo actual de la cuenta bancaria.
        """
        print(f"Saldo disponible: {self._saldo}")

    def obtener_saldo(self):
        """
        Obtiene el saldo actual de la cuenta bancaria.
        """
        return self._saldo
