from cuenta_bancaria import CuentaBancaria

class CuentaCorriente(CuentaBancaria):
    def __init__(self, saldo_inicial, linea_credito):
        super().__init__(saldo_inicial)
        self._linea_credito = linea_credito
        
    def obtener_linea_credito(self):
        return self._linea_credito

    def establecer_linea_credito(self, nueva_linea_credito):
        self._linea_credito = nueva_linea_credito