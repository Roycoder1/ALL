
// Exercise 1:

let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];
let indexOfBanana = fruits.indexOf("Banana");
console.log(indexOfBanana);
fruits.splice(indexOfBanana,1);
// fruits.shift();
let b = fruits.sort();
console.log(b);
fruits.push("kiwi");
console.log(fruits);
fruits.splice(0,1);
console.log(fruits)
fruits.reverse()
console.log(fruits)

// Exercise 2: 

let moreFruits = ["Banana", 
[
"Apples", 
["Oranges"],
"Blueberries"
]
];
let oranges = moreFruits[1][1][0];
console.log(oranges);