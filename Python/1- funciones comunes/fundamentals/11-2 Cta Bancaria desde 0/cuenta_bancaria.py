# Creación de Clase CuentaBancaria
class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    
    #Creación de metodo el cual realiza deposito en Cuenta Bancaria
    def deposito(self, monto):
        self._saldo += monto
        print(f"Deposito de: {monto} realizado correctamente")
        self.mostrar_saldo()
    
    #Creación de método el cual realiza retiro en Cuenta Bancaria
    def retiro(self, monto):
        if self.saldo >= monto:
            self._saldo -= monto
            print(f"Retiro de: {monto} realizado correctamente")
            self.mostrar_saldo()
        else:
            print("Saldo Insuficiente!")
        
    # Muestra Saldo Actual
    def mostrar_saldo(self):
        print(f"Saldo disponible de: {self.saldo}")
        
    # Recupera Saldo
    def obtener_saldo(self):
        return self.saldo