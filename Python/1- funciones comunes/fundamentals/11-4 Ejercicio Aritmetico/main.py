class Aritmetica:
    """
    Clase Aritmetica para realizar operaciones de suma, resta, multiplicación y división.
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
        
    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB
    
    def multiplicar(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        if self.operandoB != 0:
            return self.operandoA / self.operandoB
        else:
            return "Error: No se puede dividir entre cero."


while True:
    print("------------- Operando ------------")
    print("Seleccione 1 para sumar:")
    print("Seleccione 2 para restar:")
    print("Seleccione 3 para multiplicar:")
    print("Seleccione 4 para dividir:")
    print("Seleccione 0 para salir:")
    print("-----------------------------------")
    operar = int(input("Esperando opción: "))
    
    if operar == 0:
        print("------ Fin de instrucción ------")
        break
    
    if operar not in range(1, 5):
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue

    num1 = int(input("Ingrese primer número a operar: "))
    num2 = int(input("Ingrese segundo número a operar: ")) 

    aritmetica = Aritmetica(num1, num2)
    
    if operar == 1:
        print("Resultado de la suma:", aritmetica.sumar())
    elif operar == 2:
        print("Resultado de la resta:", aritmetica.restar())
    elif operar == 3:
        print("Resultado de la multiplicación:", aritmetica.multiplicar())
    elif operar == 4:
        print("Resultado de la división:", aritmetica.dividir())
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
        continue