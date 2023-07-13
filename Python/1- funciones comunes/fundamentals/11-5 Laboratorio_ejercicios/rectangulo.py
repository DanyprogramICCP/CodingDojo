class Rectangulo:
    #Calcular Area de un rectangulo Base x Altura
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return self.base * self.altura
        
b = int(input("Ingrese Base de rectangulo: "))
h = int(input("Ingrese Altura de rectangulo: "))

Area = Rectangulo(b,h)
print(f'El Area del rectangulo es: {Area.calcularArea()}')