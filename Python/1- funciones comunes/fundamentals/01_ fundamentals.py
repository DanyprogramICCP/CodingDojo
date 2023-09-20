'''
# ! Python Fundatmentals

# TODO: Syntax
#       * Indentation
#       * Block of code
# TODO: Data and Composite Types
#       * Integers
#       * Strings
#       * Booleans
#       * Lists
#       * Dictionaries
#       * Tuples
# TODO: Conditionals
#       * if, elif, else
#       * chaining conditional statements
# TODO: Loops
#       * for loops
#       * using with range
#       * using with composite types
#TODO: Built In Methods
#       * print()
#       * len()
#       * conversions: str(), int()
#       * range()
# TODO: Functions
#       * parameters
#       * arguments
#       * return vs print
'''

# class ClaseVacía:
#     pass

# mi_cadena = ""

# for val in mi_cadena:
#     pass
# tiene_hambre = True
# tiene_pecas = False
# edad = 35 # almacenar un entero
# peso = 160.57 # almacenar un flotante
# nombre = "Joe Blue"
# perro = ('Bruce', 'cocker spaniel', 19, False)
# print(perro[0])		# salida: Bruce
# perro[1] = 'dachshund'	# ERROR: no se puede modificar ('tuple' el objeto no es compatible con la asignación)
# dic_vacío = {}
# new_person = {'name': 'John', 'edad': 38, 'peso': 160.2, 'usa_lentes': False}
# new_person['name'] = 'Jack'	# actualiza si la llave existe, agrega un par clave-valor si no
# new_person['hobbies'] = ['escalada', 'programación']
# print(new_person)	
# # salida: {'name': 'Jack', 'edad': 38, 'peso: 160.2, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}
# w = new_person.pop('peso')	# remueve la llave indicada y devuelve el valor
# print(w)		# salida: 160.2
# print(new_person)	
# # salida: {'name': 'Jack', 'edad': 38, 'usa_lentes': False, 'hobbies': ['escalada', 'programación']}        
# import random
# new_person  = "Hola"

# print(type(2.63))		# salida: <class 'float'>
# print(type(new_person))		# salida: <class 'dict'>

# print(len(new_person))		# salida: 4 (el número de pares clave-valor)
# print(len('Coding Dojo'))	# salida: 11
# print(type(24))
# print(type(3.9))
# print(type(3j))
# int_to_float = float(35)
# float_to_int = int(44.2)
# int_to_complex = complex(35)
# print(int_to_float)
# print(float_to_int)
# print(int_to_complex)
# print(type(int_to_float))
# print(type(float_to_int))
# print(type(int_to_complex))

# print(random.randint(2,5)) # proporciona un número aleatorio entre 2 y 5

# print("Hola " + str(42))			# salida: TypeError
# print("Hola " + str(42))		# salida: Hola 42

# total = 35
# user_val = "26"
# # total = total + user_val		# salida: TypeError
# total = total + int(user_val)		# el total será 61

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print(f"Mi nombre is {first_name} {last_name} y tengo {age} años de edad.")

# first_name = "Zen"
# last_name = "Coder"
# age = 27
# print("Mi nombre es {} {} y tengo {} años de edad.".format(first_name, last_name, age))
# # salida: Mi nombres es Zen Coder y tengo 27 años de edad.
# print("Mi nombre es {} {} y tengo {} años de edad.".format(age, first_name, last_name))
# salida: Mi nombre es 27 Zen y tengo Coder años de edad.

# hw = "Hola %s" % "mundo" 	# con valores literales
# py = Me encanta Python %d" % 3 
# print(hw, py)
# # salida: Hola mundo Me encanta Python 3
# name = "Zen"
# age = 27
# print("Mi nombre es %s y tengo %d" % (name, age))		# o con variables
# # salida: Mi nombre es Zen y tengo 27

x = "hola mundo"
print(x.title())
# salida:
"Hola Mundo"

lista = ['Hola','mundo','de','Python']
cadena_concatenada = ' '.join(lista)
print(cadena_concatenada)
