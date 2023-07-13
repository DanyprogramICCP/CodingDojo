class Persona:
# Metodo de tipo donder o doble guion bajo __
    def __init__(self, nombre, apellido, edad):
# Atributos de instancia
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad
    #metodo get para obtener el valor de la variable encapsulada
    @property
    def nombre(self):
        return self._nombre
    #metodo set para modificar la variable
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
#Metodo en Python - Parametro Self permite acceder a métodos y atributos de instancia
    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
        
# Instancia de la clase u objeto
persona1 = Persona("Dany","Hernandez", 29)
persona1.mostrarDetalle()
persona1.nombre = 'Alberto'
print(persona1.nombre)
'''
Para encapsular en Python no es posible generar restricciones de acceso publico o priva
do, de modo que se sugiere hacer referencia a las variables con _. por ejemplo _nombre.

Si queremos restringir la modificacion de una variable en Python se sugiere utilizar __,
por ejemplo __nombre
'''