class CuentaBancaria:
    cuentas = []
    def __init__(self, tasa_interes, balance):
        self.tasa_interes = tasa_interes
        self.balance = balance
        CuentaBancaria.cuentas.append(self)

    def deposito(self, amount):
        self.balance += amount
        print(f"Deposito de {amount} realizado con exito...")
        return self
    
    def retiro(self, amount):
        if (self.balance > amount):
            self.balance -= amount
            print(f"Retiro de {amount} realizado con exito...")
            print(f"Nuevo Saldo {self.balance}")
        else:
            print(f"El Saldo es insuficiente: ${self.balance}")
            self.balance -= 5
        return self
    
    def mostrar_info_cuenta(self):
        print(f"El monto en la cuenta es: ${self.balance}")
        return self
    
    def generar_interés(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes /100)
            print(f"Interés aplicado, nuevo saldo: {self.balance}")
        return self

    @classmethod
    def print_all_accounts(cls):
        for account in cls.cuentas:
            print(f"Balance: {account.balance}")

#Instancia para Balances
savings = CuentaBancaria(20,3000)
checking = CuentaBancaria(100, 4000)

#instanciasconcatenadas
savings.deposito(5000).mostrar_info_cuenta().generar_interés().retiro(2000).mostrar_info_cuenta()
checking.mostrar_info_cuenta().deposito(10000).mostrar_info_cuenta().generar_interés()
