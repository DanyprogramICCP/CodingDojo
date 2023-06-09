# Asignación: Funciones intermedias I
# Objetivos
# Practicar el escribir funciones e iterar a través de diccionarios
# Lograr una mayor comprensión sobre cómo recorrer una lista de diccionarios o un diccionario de listas
# Nota: Evita nombrar las variables y parámetros con palabras claves de clase como int, str, list y dict.

# Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
print(estudiantes)

print(x)
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
print(directorio_deportes)
z = [ {'x': 10, 'y': 20} ]
print(z)

# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x)
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes)
# En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0] = 'Andrés'
print(directorio_deportes)
# Cambia el valor 20 en z a 30.
z[0]['y'] = 30
print(z)
# Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios, la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:
# estudiantes = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
#     ]
# iterateDictionary(estudiantes) 
# # debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# # un bonus para que aparezcan exactamente como se muestra a continuación)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonelcopy
# Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, la función imprima el valor almacenado en esa clave para cada diccionario. Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:
# Michael
# John
# Mark
# KB
# copy
# Y iterateDictionary2('last_name', estudiantes) debería generar:

# Jordan
# Rosales
# Guillen
# Tonel
# copy
# Iterar a través de un diccionarios con valores de lista
# Crea una función printInfo(some_dict)que, dado un diccionario cuyos valores son todos listas, imprima el nombre de cada clave junto con el tamaño de su lista, y luego imprima los valores asociados dentro de la lista de cada clave. Por ejemplo:

