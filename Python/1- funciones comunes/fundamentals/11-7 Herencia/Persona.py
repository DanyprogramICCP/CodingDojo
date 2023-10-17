class Persona:
    def __init__(self, name, edad):
        self.nombre = name
        self.edad = edad
        
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}'
    
class Empleado(Persona):
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
        
    def __str__(self):
        return f'Empleado: {super().__str__()} Sueldo: {self.sueldo}'
    
empleado1 = Empleado("Juan", 39, 5000)
print(empleado1.nombre)

persona1 = Persona("Dany", 30)
print(f'Nombre: {persona1.nombre}\nEdad: {persona1.edad}')
empleado2 = Empleado("Dany", 30, 1000000)
print(f'Empleado: {empleado2.nombre}\nSueldo: {empleado2.sueldo} ')