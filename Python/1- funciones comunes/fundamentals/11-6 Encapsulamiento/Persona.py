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
    # Metodo set para modificar la variable - Si eliminamos este metodo el atributo deja
    # de ser modificable.
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
        
#Metodo en Python - Parametro Self permite acceder a métodos y atributos de instancia
    def mostrarDetalle(self):
        print(f'Persona: {self._nombre} {self.apellido} {self.edad}')
        
    def __del__(self):
        print(f'Persona:  {self._nombre} {self.apellido}')
        
# Instancia de la clase u objeto
if __name__ == '__main__':
    persona1 = Persona("Dany","Hernandez", 29)
    persona1.mostrarDetalle()
    persona1.nombre = 'Alberto'
    persona1.mostrarDetalle()

    print(__name__)
'''
Para encapsular en Python no es posible generar restricciones de acceso publico o priva
do, de modo que se sugiere hacer referencia a las variables con _. por ejemplo _nombre.

Si queremos restringir la modificacion de una variable en Python se sugiere utilizar __,
por ejemplo __nombre
'''