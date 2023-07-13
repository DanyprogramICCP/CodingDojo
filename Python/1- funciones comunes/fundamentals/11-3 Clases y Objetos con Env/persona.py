class Persona:
# Metodo de tipo donder o doble guion bajo __
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
# Atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos

#Metodo en Python - Parametro Self permite acceder a métodos y atributos de instancia
    def mostrarDetalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')
        
# Instancia de la clase u objeto
persona1 = Persona("Dany","Hernandez", 29,1,2,3,4,5, a = 'Hola', b = 'Mundo!')
persona1.mostrarDetalle() #Utilizando metodo mostrarDetalle
#Persona.mostrarDetalle(persona1) #Utilizando metodo mostrarDetalle a partir de la Clase
#Instancia de Objeto 2
persona2 = Persona("Geraldine", "Lobos", 27)
persona2.mostrarDetalle()
print(f"Objeto: {persona2.nombre} {persona2.apellido} {persona2.edad}")

#Modificar Atributos en un Objeto
persona1.nombre = "Miguel Angel"
persona1.apellido = "Hernandez Gonzalez"
persona1.edad = 36

print(persona1.nombre, persona1.apellido, persona1.edad)
