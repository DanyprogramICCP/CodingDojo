// Sumar n numeros pares ingresados por teclado
var count = 0;
var arr = [];
var sum = 0;

n = parseInt(prompt("ingrese un numero limitante: "));
while(count < n){
    num = parseInt(prompt("Ingrese un numero par: "));
    if(num % 2 == 0){
        count++;
        sum = sum + num;
        arr.push(num);
    } else {
        num = parseInt(prompt("Ingrese un numero par: "));
    }
} 
console.log("El numero limitante es: " + n);
console.log("La suma de los pares: " + arr + " es --> " + sum);
