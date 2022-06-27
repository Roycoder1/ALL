// Exercise 1:

let sentence = ["my","favorite","color","is","blue"];
let sent = sentence.toString()
console.log(sentence);

// Exercise2:

let var1= "mix";
let var2= "pod";

let slice = var1.slice(2,3); 
let slice2 = var2.slice(0,2);
let var3 = `${slice2}${slice}`;
console.log(var3);

// let slice3 = var1.slice(0,2);
// let slice4 = var2.slice(2,3);
// let var4 = `${slice3}${slice4}`;
// console.log (var4);

// Exercice3:


let value= prompt('Choisissez un nombre', 20);
let num1= parseInt(value);
console.log(value);
let value2 = prompt('Choisissez un second numero',20);
let num2 = parseInt(value2);
console.log (num2);
let num3 = num1+num2;
let num4 = num1*num2;
let num5 = num1-num2;
let num6 = num1/num2;
alert(num3);
alert(num4);
alert(num5);
alert(num6);

