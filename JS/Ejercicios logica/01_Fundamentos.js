// Explicación sobre la programación y su importancia

// Imprimir un mensaje en la consola
console.log("Bienvenido a la programación");

var numero = 0;
numero = parseInt(prompt("Ingrese valor numérico: "));

// Conceptos básicos: Variables, tipos de datos y operadores

// Declaración de variables
let edad; // Declaramos una variable llamada "edad"

// Asignación de valor a una variable
edad = 25; // Asignamos el valor 25 a la variable "edad"
console.log(edad);
// Tipos de datos
let nombre = "Juan"; // Cadena de texto (string)
let cantidad = 10; // Número entero (number)
let precio = 99.99; // Número de punto flotante (number)
let esNuevo = true; // Valor booleano (boolean)

// Operadores aritméticos
let suma = 5 + 3; // Suma: 8
let resta = 10 - 4; // Resta: 6
let multiplicacion = 2 * 6; // Multiplicación: 12
let division = 15 / 3; // División: 5
let modulo = 7 % 2; // Módulo: 1 (resto de la división)

// Operadores de asignación
let x = 10; // Asignación: x tiene el valor 10
x += 5; // Asignación de suma: x tiene el valor 15 (equivalente a x = x + 5)
x -= 3; // Asignación de resta: x tiene el valor 12 (equivalente a x = x - 3)
x *= 2; // Asignación de multiplicación: x tiene el valor 24 (equivalente a x = x * 2)
x /= 6; // Asignación de división: x tiene el valor 4 (equivalente a x = x / 6)

// Operadores de comparación
let a = 10;
let b = 5;
let igualdad = a == b; // Igualdad: false
let mayorQue = a > b; // Mayor que: true
let menorQue = a < b; // Menor que: false
let mayorOIgual = a >= b; // Mayor o igual que: true
let menorOIgual = a <= b; // Menor o igual que: false

// Operadores lógicos
let p = true;
let q = false;
let and = p && q; // AND lógico: false
let or = p || q; // OR lógico: true
let not = !p; // NOT lógico: false

// Introducción a la resolución de problemas y algoritmos

// Algoritmo para determinar si un número es par o impar
let num = 7;
if (num % 2 === 0) {
  console.log("El número es par");
} else {
  console.log("El número es impar");
}
