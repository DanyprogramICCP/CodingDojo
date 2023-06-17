class User:
    # Constructor de la clase User
    def __init__(self, name):
        self.name = name
        self.amount = 0

    # Metodo para depositar
    def deposit(self, amount):
        self.amount += amount
        print(f"Deposito realizado correctamente! Monto depositado: {amount}")
        self.display()
    
    #Metodo para retirar
    def ret(self, amount):
        self.amount -= amount
        print(f"Retiro realizado correctamente! Monto retirado: {amount}")
        self.display()
        
    #Metodo para Mostrar
    def display(self):
        print(f"Usuario: {self.name}, Monto: {self.amount}")
    
    #Metodo para realizar transferencia
    def trans(self, amount, user):
        self.amount -= amount
        user.amount += amount
        print(f"Traspaso realizado correctamente de {amount} pesos")
        self.display()
        user.display()
        
#Instancias para la Clase Usuario
Dany = User("Dany")
Geral = User("Geral")
Kevin = User("Kevin")

#Operaciones Para Dany
Dany.deposit(20000)
Dany.ret(5000)

#Operaciones Geral
Geral.deposit(30000)
Geral.trans(5000, Dany)