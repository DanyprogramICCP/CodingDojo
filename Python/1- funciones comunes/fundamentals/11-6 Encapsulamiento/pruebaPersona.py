from Persona import Persona

if __name__ == '__main__': #metodo opcional para comprobar  impresión de objetos
    print('Creación de Objetos'.center(30,'-'))
    persona1 = Persona('Karla', 'Lara', 21)
    persona1.mostrarDetalle()
    
    print('Eliminación de Objetos'.center(30,'-'))
    del persona1
    print(__name__) 