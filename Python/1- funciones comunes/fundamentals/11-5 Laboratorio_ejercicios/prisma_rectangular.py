class Prisma:
    #Calcular volumen de Prisma
    def __init__(self, ancho, altura, profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad
        
    def calcularVolumen(self):
        return self.ancho * self.altura * self.profundidad
    
h = int(input("Ingrese altura del objeto: "))
w = int(input("Ingrese ancho del objeto: "))
p = int(input("Ingrese profundidad del objeto: "))

prisma1 = Prisma(h,w,p)
print(f'El Calculo del volumen es: {prisma1.calcularVolumen()}')