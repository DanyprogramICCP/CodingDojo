class Persona:
# Metodo de tipo donder o doble guion bajo __
    def __init__(self, nombre, apellido, edad):
# Atributos de instancia
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

# Instancia de la clase u objeto
persona1 = Persona("Dany","Hernandez", 29)
print(persona1.nombre, persona1.apellido, persona1.edad)

persona2 = Persona("Geraldine", "Lobos", 27)
print(f"Objeto: {persona2.nombre} {persona2.apellido} {persona2.edad}")
