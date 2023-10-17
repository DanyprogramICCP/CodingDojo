from Cuadrado import Cuadrado

cuadrado1 = Cuadrado(5, "rojo")
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)

print(f'Calculo del Area del Cuadrado: {cuadrado1.calcularArea()}')

print(Cuadrado.mro())

