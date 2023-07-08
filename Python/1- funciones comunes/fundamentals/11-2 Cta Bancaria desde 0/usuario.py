from cuenta_bancaria import CuentaBancaria
from cuenta_corriente import CuentaCorriente

# Creación de Clase Usuario
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        tipo_cuenta = input("Ingrese el tipo de cuenta (bancaria/corriente): ")
        saldo_inicial = float(input("Ingrese Saldo Inicial: "))
        if tipo_cuenta == "bancaria":
            cuenta = CuentaBancaria(saldo_inicial)
        elif tipo_cuenta == "corriente":
            linea_credito = float(input("Ingrese la línea de crédito: "))
            cuenta = CuentaCorriente(saldo_inicial, linea_credito)
        else:
            print("Ingrese un tipo de cuenta valido")
            return
        
        self.cuentas.append(cuenta)
        print("Cuenta agregada correctamente!")
        
    def mostrar_saldos(self):
        print(f"------- Saldos de {self.nombre} -------")
        for i, cuenta in enumerate(self.cuentas):
            print(f"Cuenta: {i+1}")
            cuenta.mostrar_saldo()
    
    def realizar_transferencia(self):
        if len(self.cuentas) < 2:
            print("Debe tener al menos 2 cuentas para realizar una transferencia")
            return
        
        print("Seleccione la cuenta de origen: ")
        self.mostrar_saldos()
        cuenta_origen = int(input("Ingrese el numero de la cuenta de origen: ")) -1
        
        print("Seleccione la cuenta de destino:")
        self.mostrar_saldos()
        cuenta_destino = int(input("Ingrese el número de la cuenta de destino: ")) - 1

        monto = float(input("Ingrese el monto a transferir: "))

        if cuenta_origen < 0 or cuenta_origen >= len(self.cuentas) or cuenta_destino < 0 or cuenta_destino >= len(self.cuentas):
            print("Número de cuenta inválido.")
            return

        if cuenta_origen == cuenta_destino:
            print("La cuenta de origen y la cuenta de destino deben ser diferentes.")
            return

        origen = self.cuentas[cuenta_origen]
        destino = self.cuentas[cuenta_destino]

        if origen.obtener_saldo() < monto:
            print("Saldo insuficiente en la cuenta de origen.")
            return

        origen.retiro(monto)
        destino.deposito(monto)
        print("Transferencia realizada con éxito.")