ninjas = ['Rozen', 'KB', 'Oliver']
mi_lista = ['4', ['lista', 'en', 'una', 'lista'], 987]
lista_vacía = []

frutas = ['manzana', 'plátano', 'naranja', 'frutilla']
vegetales = ['lechuga', 'pepino', 'zanahorias']
frutas_y_vegetales = frutas + vegetales
print(frutas_y_vegetales)
ensalada = 3 * vegetales
print(ensalada)

cajón = ['documentos', 'sobres', 'lápices']
# acceder al cajón con índice 0 y valor print
print(cajón[0])  # imprime documentos
# acceder al cajón con índice 1 y  valor print
print(cajón[1]) # imprime sobres
# acceder al cajón con índice 2 y valor print
print(cajón[2]) # imprime lápices

x = [1,2,3,4,5]
x.append(99)
print(x)
# la salida sería [1,2,3,4,5,99]

x = [99,4,2,5,-3]
print(x[:])
# la salida sería [99,4,2,5,-3]
print(x[1:])
# la salida sería [4,2,5,-3];
print(x[:4])
# la salida sería [99,4,2,5]
print(x[2:4])
# la salida sería [2,5];

mi_lista = [1, 'Zen', 'hola']
print(len(mi_lista))
# salida
3

mi_lista = [1,5,2,8,4]
mi_lista.append(7)
print(mi_lista)
# salida:
# [1,5,2,8,4,7]

