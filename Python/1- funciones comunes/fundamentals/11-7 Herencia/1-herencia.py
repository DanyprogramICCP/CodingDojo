class Persona:
    def __init__(self, name, edad):
        self.nombre = name
        self.edad = edad
        
class Empleado(Persona):
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
empleado1 = Empleado("Juan", 39, 5000)
print(empleado1.nombre)