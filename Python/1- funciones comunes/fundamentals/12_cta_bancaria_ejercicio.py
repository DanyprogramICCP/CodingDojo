class CuentaBancaria:
    nombre = ""
    cuentas = []
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, tasa_interes, balance): 
        self.tasa_interes = tasa_interes
        self.balance = balance
        self.cuentas.append(self)
        
    def depósito(self, amount):
        self.balance += amount
        return self

    def retiro(self, amount):
        if self.balance < amount:
            print("Saldo insuficiente para realizar retiro")
        else:
            self.balance -= amount
        return self

    def mostrar_info_cuenta(self):
        print(f'El Balance actual es de {self.balance}')
        
    def generar_interés(self):
        self.balance = self.balance * self.tasa_interes
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for cuentas in cls.cuentas:
            cuentas.mostrar_info_cuenta()

persona1 = CuentaBancaria(1.6,1000)
# persona1.retiro(500).depósito(200).depósito(200).depósito(2000).mostrar_info_cuenta()
persona2= CuentaBancaria(.2,3000) 
# persona2.retiro(500).depósito(200).depósito(200).depósito(3000).mostrar_info_cuenta()

CuentaBancaria.print_all_accounts()
