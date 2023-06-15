# class Persona:
#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def saludar(self):
#         print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# # Crear un objeto de la clase Persona
# persona1 = Persona("Juan", 25)

# # Llamar al método saludar del objeto persona1
# persona1.saludar()

# Crear Clase persona con metodo presentar, atributos nombre, edad y profesión

class Persona:
    def __init__(self, nombre, edad, profesion):
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion 
        
    def presentar(self):
        print(f"Hola, mi nombre es {self.nombre}, tengo {self.edad}, y mi profesión es {self.profesion} ")
        
persona1 = Persona("Dany", 29,"Ingeniero")
persona1.presentar()