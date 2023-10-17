from FiguraGeometrica import figuraGeometrica
from Color import Color

class Cuadrado(figuraGeometrica, Color):
    def __init__(self, lado, color):
        #super().__init__()
        figuraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
        
    def calcularArea(self):
        return self.alto * self.ancho
    